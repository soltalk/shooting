# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Control as con

class Pshot_rapid(pygame.sprite.Sprite):
    def __init__(self, left, right):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        pshot_path = os.path.join(os.getcwd(),"png/rapid.png")
        self.image = pygame.image.load(pshot_path)
        self.pshot_rad = 3
        self.pshot_speed = 15
        self.power = 1
        self.left = left
        self.right = right
        self.rect = self.image.get_rect()
        self.shot_flag = False
        self.rect.center = (-3, -3)
        self.control = con.Control()

    def set_shot(self, point):
        self.rect.center = point
        self.shot_flag = True
        #self.shot_way = way

    def update(self):
        if self.shot_flag == True:
            #if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right or self.rect.top > self.h:
            if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right:
                self.shot_flag = False
            self.rect.top -= self.pshot_speed
            if(self.control.hit(self.pshot_rad, self.rect.center, self.power)):
                self.shot_flag = False
                self.rect.center = (-3, -3)

    def ps_flag(self):
        return self.shot_flag
