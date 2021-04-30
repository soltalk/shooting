# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Eshot as es
import Enemy

class Enemy2(Enemy.Enemy):
    def __init__(self, left, right):
        super().__init__()
        self.id = 2
        self.images = list()
        enemy_path = os.path.join(os.getcwd(),"png/enemy2.png")
        #enemy_d_path = os.path.join(os.getcwd(),"png/enemy_d30.png")
        self.images.append(pygame.image.load(enemy_path))
        #self.images.append(pygame.image.load(enemy_d_path))
        self.images.append(pygame.Surface((1,1)))
        self.image = self.images[0]
        self.ene_rad = 15
        self.left = left - self.ene_rad
        self.right = right + self.ene_rad
        self.h += self.ene_rad
        self.e_speed = 2
        self.maxlife = 5
        self.score = 100
        self.rect = self.image.get_rect()
        self.rect.center = (-50, -50)
        #弾の処理
        self.interval = 4  #発射間隔
        self.eshot_speed = 2.5  #弾速
        self.shotcount = 2  #発射方向
        self.angle = 0  #発射角度
        self.angle_rate = 15  #発射各速度変更
        self.eshot = []
        self.es_num = 60
        for _ in range(self.es_num):
            self.eshot.append(es.Eshot(self.eshot_speed, left, right))

    def set_data(self, move, x, y):
        super().set_data(move, x, y)

    def update(self):
        super().update()

    def e_damage(self, power):
        super().e_damage(power)

    def set_eshot(self):
        for i in range(self.shotcount):
            for j in range(self.es_num):
                if self.eshot[j].es_flag() == False:
                    self.eshot[j].set_shot(self.rect.center, self.angle + 360*float(i)/self.shotcount)
                    break
        self.angle -= self.angle_rate
        if self.angle < 0:
            self.angle += 360

    def all_kill_shot(self):
        super().all_kill_shot()

    def e_id(self):
        return self.id

    def e_point(self):
        return [self.x, self.y]

    def e_rad(self):
        return self.ene_rad

    def e_health(self):
        return self.e_hit

    def e_live(self):
        return self.live_flag

    def e_eshot_num(self):
        return self.es_num

    def e_eshot_flag(self, id):
        return self.eshot[id].es_flag()

    def e_eshot_data(self, id):
        return self.eshot[id].es_rad(), self.eshot[id].es_point()
