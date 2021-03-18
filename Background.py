# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

class Background(pygame.sprite.Sprite):
    def __init__(self, start, code, left, right):
        self.h = pygame.display.get_surface().get_height()
        pygame.sprite.Sprite.__init__(self, self.containers)
        #self.image = pygame.image.load("../png/bg.png")
        if code == 1:
            bg_path = os.path.join(os.getcwd(),"png/bg.png")
        self.image = pygame.image.load(bg_path)
        if start == 0:
            self.rect = Rect(left, 0, right - left, self.h)
        else:
            self.rect = Rect(left, -self.h, right - left, self.h)

        self.speed = 5

    def set_data(self):
        self.speed = 0

    def update(self):
        self.rect.top += self.speed
        if self.rect.top >= self.h:
            self.rect.bottom = 0
