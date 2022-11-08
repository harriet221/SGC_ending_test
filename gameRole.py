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
        # Initialize player speed, here is a definite value
        self.speed = 8
        # A collection of bullets fired by the player's aircraft
        self.bullets = pygame.sprite.Group()
        self.img_index = 0                              # Player sprite image index
        self.is_hit = False                             # whether the player was hit

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

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
        self.rect.topleft = init_pos
        self.speed = enemy_speed
        self.down_index = 0
        self.hp = enemy_hp

    def move(self):
        self.rect.top += self.speed


# coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_shine, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = coin_shine
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 10

    def move(self):
        self.rect.top += self.speed
