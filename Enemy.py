# coding: utf-8
import pygame
from pygame.locals import *
import sys

import Control as con

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.h = pygame.display.get_surface().get_height()
        #self.screen = pygame.display.get_surface()
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.e_hit = False
        self.move_count = 0
        self.hit_count = 0
        self.score = 0
        self.live_flag = False
        self.control = con.Control()

    def set_data(self, move, x, y):
        self.x = x
        self.y = y
        self.move = move
        self.life = self.maxlife
        self.live_flag = True
        self.e_hit = True

    def update(self):
        if self.live_flag == True:
            self.move_count += 1
            if self.move == 1:
                if self.move_count < 70:
                    self.y += self.e_speed
                elif self.move_count > 250:
                    if self.y < -self.ene_rad:
                        self.live_flag = False
                        self.move_count = 0
                    self.y -= self.e_speed
                elif self.move_count % self.interval == 0:
                    self.set_eshot()

            elif self.move == 2:
                if self.y > self.h or self.x > self.right:
                    self.live_flag = False
                self.x += self.e_speed
                self.y += self.e_speed/2
            elif self.move == 3:
                if self.y > self.h or self.x < self.left:
                    self.live_flag = False
                self.x -= self.e_speed
                self.y += self.e_speed/2
            else:
                if self.y > self.h:
                    self.live_flag = False
                self.y += self.e_speed

            self.rect.center = (self.x, self.y)

            #被ダメージ時の無敵時間の管理
            if self.e_hit == False:
                if self.hit_count / 2 % 2 == 0:
                    self.hit_count += 1
                    self.image = self.images[1]
                else:
                    self.hit_count += 1
                    self.image = self.images[0]
                if self.hit_count == 11:#奇数である必要がある
                    self.hit_count = 0
                    self.e_hit = True

    def e_damage(self, power):
        self.e_hit = False
        self.life -= power
        if self.life <= 0:
            self.live_flag = False
            self.control.score_plus(self.score)
            self.move_count = 0
            self.rect.center = (-50, -50)
            self.image = self.images[0]

    def all_kill_shot(self):
        for i in range(self.es_num):
            if self.eshot[i].es_flag():
                self.eshot[i].es_hit()
