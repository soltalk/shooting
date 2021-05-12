# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os
import math

import Control as con

class Pshot_3way(pygame.sprite.Sprite):
    def __init__(self, left, right):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        pshot_path = os.path.join(os.getcwd(),"png/3way.png")
        self.image = pygame.image.load(pshot_path)
        self.pshot_rad = 5
        self.pshot_speed = 7
        self.power = 1
        self.left = left
        self.right = right
        self.angle = 0.0
        self.rect = self.image.get_rect()
        self.shot_flag = False
        (self.x, self.y)  = (0.0, 0.0)
        self.rect.center = (-3, -3)
        self.control = con.Control()

    def set_shot(self, point, way):
        (self.x, self.y) = point
        self.rect.center = (self.x, self.y)
        self.shot_flag = True
        if way == 0:
            self.angle = -110
        elif way == 1:
            self.angle = -90
        else:
            self.angle = -70

    def update(self):
        if self.shot_flag == True:
            #if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right or self.rect.top > self.h:
            if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right:
                self.shot_flag = False
            self.x += round(math.cos(math.radians(self.angle)), 2) * self.pshot_speed
            self.y += round(math.sin(math.radians(self.angle)), 2) * self.pshot_speed
            self.rect.center = (self.x, self.y)
            #self.rect.centerx += round(math.cos(math.radians(self.angle)), 2) * self.pshot_speed
            #self.rect.centery += round(math.sin(math.radians(self.angle)), 2) * self.pshot_speed
            if(self.control.hit(self.pshot_rad, self.rect.center, self.power)):
                self.shot_flag = False
                self.rect.center = (-3, -3)

    def ps_flag(self):
        return self.shot_flag
