# coding: utf-8
import pygame
from pygame.locals import *
import sys
import math
import os

class Eshot(pygame.sprite.Sprite):
    def __init__(self, speed, left, right):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        eshot_path = os.path.join(os.getcwd(),"png/eshot1.png")
        self.image = pygame.image.load(eshot_path)
        self.eshot_rad = 5
        self.eshot_speed = speed
        self.left = left - self.eshot_rad
        self.right = right + self.eshot_rad
        self.h += self.eshot_rad
        self.rect = self.image.get_rect()
        self.shot_flag = False
        self.angle = 0.0
        (self.x, self.y)  = (0.0, 0.0)
        self.rect.center = (-40.0, -40.0)

    def set_shot(self, point, angle):
        (self.x, self.y) = point
        self.rect.center = (self.x, self.y)
        self.shot_flag = True
        self.angle = angle

    def update(self):
        if self.shot_flag == True:
            if self.rect.right < self.left or self.rect.bottom < 0 or self.rect.left > self.right or self.rect.top > self.h:
                self.shot_flag = False
            self.x += round(math.cos(math.radians(self.angle)), 2) * self.eshot_speed
            self.y += round(math.sin(math.radians(self.angle)), 2) * self.eshot_speed
            self.rect.center = (self.x, self.y)

    def es_hit(self):
        self.shot_flag = False
        self.rect.center = (-40.0, -40.0)

    def es_flag(self):
        return self.shot_flag

    def es_point(self):
        #(x, y) = self.rect.center
        #return [x, y]
        return [self.x, self.y]

    def es_rad(self):
        return self.eshot_rad
