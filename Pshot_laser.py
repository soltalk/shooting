# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Control as con

class Pshot_laser(pygame.sprite.Sprite):
    def __init__(self, left, right, body):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        if body:
            pshot_path = os.path.join(os.getcwd(),"png/laser.png")
            self.image = pygame.image.load(pshot_path)
        else:
            self.image = pygame.Surface((1,1))
        self.pshot_rad = 5
        self.pshot_speed = 10
        self.power = 3
        self.left = left
        self.right = right
        self.rect = self.image.get_rect()
        self.shot_flag = False
        self.rect.center = (-30, -30)
        self.control = con.Control()

    def set_shot(self, point):
        (self.rect.centerx, self.rect.bottom) = point
        self.shot_flag = True

    def update(self):
        if self.shot_flag == True:
            #if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right or self.rect.top > self.h:
            if self.rect.bottom < 0:
                self.shot_flag = False
            self.rect.top -= self.pshot_speed
            if(self.control.hit(self.pshot_rad, self.rect.center, self.power)):
                pass

    def ps_flag(self):
        return self.shot_flag
