# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

class Pshot(pygame.sprite.Sprite):
    def __init__(self, left, right):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        pshot_path = os.path.join(os.getcwd(),"png/pshot.png")
        self.image = pygame.image.load(pshot_path)
        self.pshot_rad = 5
        self.pshot_speed = 10
        self.power = 1
        self.left = left
        self.right = right
        self.rect = self.image.get_rect()
        self.shot_flag = False
        self.rect.center = (-30, -30)

    def set_shot(self, point):
        self.rect.center = point
        self.shot_flag = True

    def update(self):
        if self.shot_flag == True:
            if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right or self.rect.top > self.h:
                self.shot_flag = False
            self.rect.top -= self.pshot_speed

    def ps_hit(self):
        self.shot_flag = False
        self.rect.center = (-30, -30)

    def ps_flag(self):
        return self.shot_flag

    def ps_point(self):
        (x, y) = self.rect.center
        return [x, y]

    def ps_rad(self):
        return self.pshot_rad

    def ps_power(self):
        return self.power
