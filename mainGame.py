# -*- coding: utf-8 -*-
"""
Original: Created on Wed Sep 11 11:05:00 2013
@author: Leo

2022-10-26
OSSProj team SGC
"""

import pygame
from sys import exit
from pygame.locals import *
from gameRole import *
import random


# initial
pygame.init()
pygame.display.set_caption('PLAY')

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

# sounds
bullet_sound = pygame.mixer.Sound('resource/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('resource/sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('resource/sound/game_over.wav')
bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)
pygame.mixer.music.load('resource/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# images
background = []
background.append(pygame.image.load(
    'resource/image/space_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/chess_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/green_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/color_bg.png').convert())

widths = 3000
heights = 5000

bg_widths = -(3000-SCREEN_WIDTH)/2
bg_h = -(5000-SCREEN_HEIGHT)
bg_heights = [bg_h, bg_h, bg_h, bg_h]

game_over = pygame.image.load('resource/image/blackhole.png')

filename = 'resource/image/shoot.png'
plane_img = pygame.image.load(filename)

# display
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 650]
player = Player(plane_img, player_rect, player_pos)

# Define parameters ; bullet object
bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# Define parameters ; enemy aircraft object
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

enemies1 = pygame.sprite.Group()

# Store wrecked planes for rendering wreck sprite animations
enemies_down = pygame.sprite.Group()

# Define parameters ; coin object
coin1_img = pygame.image.load('resource/image/coin1.png')
coin_rect = coin1_img.get_rect()
coin_shine = coin1_img.subsurface(coin_rect)

coins = pygame.sprite.Group()

shoot_frequency = 0
enemy_frequency = 0

player_down_index = 16

score = 0

clock = pygame.time.Clock()
n = 0

running = True

while running:
    # set frame rate
    clock.tick(45)
    n += 1/45
    SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

    # set firing bullets
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            # bullet_sound.play()
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # set enemy planes
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    # move the bullet, and delete it
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    # move the enemy plane, and delete it
    for enemy in enemies1:
        enemy.move()
        # determine if the player has been hit
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)

    # add the hit enemy aircraft object
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    # set coins
    if enemies1_down:
        coin_pos = list(enemy.rect.topleft)
        coin = Coin(coin_shine, coin_pos)
        coins.add(coin)

    for coin in coins:
        coin.move()
        if pygame.sprite.collide_circle(coin, player):
            coins.remove(coin)
            score += 1000   # 또는 따로 체크
            # sound.play()

    # draw background
    SCREEN.fill(0)
    if n <= 20:
        SCREEN.blit(background[0], (bg_widths, bg_heights[0]))
        bg_heights[0] += 3
    elif n <= 40:
        SCREEN.blit(background[1], (bg_widths, bg_heights[1]))
        bg_heights[1] += 3
    elif n <= 60:
        SCREEN.blit(background[2], (bg_widths, bg_heights[2]))
        bg_heights[2] += 3
    else:
        SCREEN.blit(background[3], (bg_widths, bg_heights[3]))
        bg_heights[3] += 3

    # draw player plane
    if not player.is_hit:
        SCREEN.blit(player.image[player.img_index], player.rect)
        # Change the picture index to plane's animation effect
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        SCREEN.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            running = False
    if player.rect.left >= SCREEN_WIDTH - player.rect.height:
        # 화면 비율 축소시 플레이어 위치 화면 안으로 자동 조절
        player.rect.left = SCREEN_WIDTH - player.rect.height

    # draw wreck animation
    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            enemy1_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            # score += 1000   # 일단 코인 쪽에 넣음
            continue
        SCREEN.blit(
            enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
        enemy_down.down_index += 1

    # draw bullets and enemy planes and coins
    player.bullets.draw(SCREEN)  # background moving
    enemies1.draw(SCREEN)
    coins.draw(SCREEN)

    # draw score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    SCREEN.blit(score_text, text_rect)

    # update screen
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # keyboard events
    key_pressed = pygame.key.get_pressed()

    if not player.is_hit:
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()


font = pygame.font.Font(None, 48)
text = font.render('Score: ' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = SCREEN.get_rect().centerx
text_rect.centery = SCREEN.get_rect().centery + 24
SCREEN.blit(game_over, (0, 0))
SCREEN.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
