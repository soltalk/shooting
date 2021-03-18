# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

class Item(pygame.sprite.Sprite):
    def __init__(self):
        self.dia = 500
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        bomb_path = os.path.join(os.getcwd(),"png/bomb.png")
        self.image = pygame.image.load(bomb_path)
        self.image_sub = pygame.image.load(bomb_path)
        self.bomb_size = 20
        #self.bomb_count = 0
        #self.bomb_rate = 1.3
        self.power = 3
        self.rect = self.image.get_rect()
        self.bomb_flag = False
        (self.x, self.y) = (0, 0)
        self.rect.center  = (-30, -30)
        #self.i_flag = False
        #self.wait_time = 0

    def set_bomb(self):
        #(self.x, self.y) = point
        #self.rect.center  = (self.x, self.y)
        #self.rect.center  = point
        self.i_flag = True
        self.bomb_flag = True

    def update(self):
        if self.bomb_flag == True:
            #self.rect.size = (self.bomb_size+1, self.bomb_size+1)
            #self.rect.inflate_ip(self.bomb_rate, self.bomb_rate)
            self.image = pygame.transform.scale(self.image, (self.bomb_size*2, self.bomb_size*2))
            #self.image = pygame.transform.scale2x(self.image)
            self.rect = self.image.get_rect()
            self.rect.center  = (self.x, self.y)
            self.bomb_size += 40
            #self.bomb_count += 1
            #if self.bomb_size > 500:
            #    self.bomb_flag = False
            #    self.bomb_size = 20
                #self.bomb_count = 0
            #    self.image = self.image_sub
            #    self.rect = self.image.get_rect()
                #self.rect.center  = (-30, -30)
        #elif self.i_flag == True:
        #    self.wait_time += 1
        #    if self.wait_time > 9:
        #        self.i_flag = False
        #        self.wait_time = 0

    def bomb_end(self):
        self.bomb_flag = False
        self.bomb_size = 20
        self.image = self.image_sub
        self.rect = self.image.get_rect()

    def set_point(self, point):
        (self.x, self.y) = point
        self.rect.center  = (self.x, self.y)
        #self.rect.center  = point

    def set_out(self):
        self.rect.center  = (-30, -30)

    def item_flag(self):
        return self.i_flag

    #def ps_point(self):
    #    (x, y) = self.rect.center
    #    return [x, y]

    #def ps_rad(self):
    #    return self.bomb_size

    def bomb_power(self):
        return self.power
