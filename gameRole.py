# -*- coding: utf-8 -*-
"""
Original: Created on Wed Sep 11 16:36:03 2013
@author: Leo

2022-10-26
OSSProj team SGC
"""

import pygame
from pygame.locals import *

TYPE_SMALL = 1
TYPE_MIDDLE = 2
TYPE_BIG = 3

SCREEN = pygame.display.set_mode((480, 800), HWSURFACE | DOUBLEBUF | RESIZABLE)


# bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed


# player
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        # List to store player object sprite images
        self.image = []
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(
                player_rect[i]).convert_alpha())
        # Initialize the rectangle where the image is located
        self.rect = player_rect[0]
        # Initialize the coordinates of the upper left corner of the rectangle
        self.rect.topleft = init_pos
        # Initialize player speed, default is 8
        self.speed = 8
        # A collection of bullets fired by the player's aircraft
        self.bullets = pygame.sprite.Group()
        self.img_index = 0                              # Player sprite image index
        self.is_hit = False                             # whether the player was hit

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)                       # 0 500 1000 1500 2000
        self.speed = (SCREEN.get_size()[0]//500)+8     # 8  9   10   11   12
        if self.rect.top <= SCREEN.get_size()[1] - self.rect.height - 20:
            self.rect.top = SCREEN.get_size()[1] - self.rect.height - 20

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN.get_size()[0] - self.rect.width:
            self.rect.left = SCREEN.get_size()[0] - self.rect.width
        else:
            self.rect.left += self.speed


# enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_speed, init_pos, enemy_hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img[0]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos
        self.speed = enemy_speed
        self.down_index = 0
        self.hp = enemy_hp

    def move(self):
        self.rect.top += self.speed


# coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_img, coin_shine_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.shine_imgs = coin_shine_imgs
        self.speed = 10

    def move(self):
        self.rect.top += self.speed
        self.index = self.rect.top % 240
        self.image = self.shine_imgs[self.index // 40]


# landom box - star
class Star(pygame.sprite.Sprite):
    def __init__(self, star_img, star_spin_imgs, star_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = star_img
        self.rect = self.image.get_rect()
        self.rect.bottomright = [0, 0]
        self.spin_imgs = star_spin_imgs
        self.type = star_type

    def move(self):
        self.rect.top += (SCREEN.get_size()[1]//50)
        self.rect.left += (SCREEN.get_size()[0]//50)
        self.index = self.rect.top % 210
        self.image = self.spin_imgs[self.index // 30]
