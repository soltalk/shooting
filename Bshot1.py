# coding: utf-8
import pygame
from pygame.locals import *
import sys
import math
import os

class Bshot1(pygame.sprite.Sprite):
    def __init__(self, speed_rate, angle_rate, left, right):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        bshot_path = os.path.join(os.getcwd(), "png/bshot1.png")
        self.images = self.split_image(pygame.image.load(bshot_path))
        self.image = self.images[0]
        self.flame = 1
        self.bshot_rad = 5
        self.bshot_speed = 0.0
        self.bshot_speed_rate = speed_rate
        self.angle_rate = angle_rate
        self.left = left - self.bshot_rad
        self.right = right + self.bshot_rad
        self.h += self.bshot_rad
        self.rect = self.image.get_rect()
        self.shot_flag = False
        self.angle = 0.0
        (self.x, self.y)  = (-40.0, -40.0)
        self.rect.center = (self.x, self.y)

    def set_shot(self, point, speed, angle, speed_rate):
        (self.x, self.y) = point
        self.shot_flag = True
        self.bshot_speed = speed
        self.angle = angle
        self.bshot_speed_rate = speed_rate

    def update(self):
        if self.shot_flag == True:
            if self.x < self.left or self.y < -self.bshot_rad or self.x > self.right or self.y > self.h:
                self.shot_flag = False
            self.x += round(math.cos(math.radians(self.angle)), 2) * self.bshot_speed
            self.y += round(math.sin(math.radians(self.angle)), 2) * self.bshot_speed
            self.bshot_speed += self.bshot_speed_rate
            self.rect.center = (self.x, self.y)

            self.image = self.images[int(self.flame / 5)]
            self.flame += 1
            if self.flame >= 15:
                self.flame = 0

    def split_image(self, image):	#画像を配列に分ける
        imageList=[]		#配列を作成
        for i in range(0,39,13):	#0～96を32ずつ進む（3回繰り返す）
            surface=pygame.Surface((13,13))	#カラのfurefacを作成
            surface.blit(image,(0,0),(i,0,13,13))	#(0,0)は画像の左上の場所　iはimageのx座標、0はy座標、32がwidthとheight
            surface.set_colorkey((0,0,0), RLEACCEL)
            surface.convert()		#ピクセル形式を変更
            imageList.append(surface)	#imageListに加える

        return imageList

    def bs_hit(self):
        self.shot_flag = False
        self.rect.center = (-40, -40)

    def bs_flag(self):
        return self.shot_flag

    def bs_point(self):
        return [self.x, self.y]

    def bs_rad(self):
        return self.bshot_rad
