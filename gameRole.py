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

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN.get_size()[1] - self.rect.height:
            self.rect.top = SCREEN.get_size()[1] - self.rect.height
        else:
            self.rect.top += self.speed

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
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed
