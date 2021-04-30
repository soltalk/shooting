# coding: utf-8
import pygame
from pygame.locals import *
import sys
import math
import os

import Control as con
import Bshot1 as bs

class Boss1(pygame.sprite.Sprite):
    def __init__(self, left, right):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = list()
        boss1_path = os.path.join(os.getcwd(), "png/boss1.png")
        self.images.append(pygame.image.load(boss1_path))
        #boss_d_path = os.path.join(os.getcwd(), "png/boss_d61.png")
        #self.images.append(pygame.image.load(boss_d_path))
        self.images.append(pygame.Surface((1,1)))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.x, self.y = (300.0, -50.0)
        self.rect.center = (300.0, -50.0)
        self.score = 1000
        self.live_flag = False
        self.control = con.Control()
        #体力の処理
        self.b_hit = False
        self.bos_rad = [15, 15, 15]
        self.bos_point = [[0, 0],[0, 0],[0, 0]]
        self.life = 75
        self.hit_count = 0
        #移動の処理
        self.b_speed = 1
        self.move = 0
        self.move_count = 0
        self.move_angle = 90
        self.move_pattern = 0
        #弾の処理
        self.shot_pattern = 0
        self.shot_time = 0 #カウント用の変数
        self.interval = 3  #発射間隔
        self.shotcount = 3 #発射方向数
        self.angle = -90 #発射角度
        self.angle_rate = 10 #発射角度変更
        self.bshot_angle_rate = 5 #弾丸角速度変更
        self.bshot_speed = 3.3 #弾速
        self.bshot_speed_rate = 0.02 #弾速変更
        self.bshot = []
        self.bs_num = 400
        for _ in range(self.bs_num):
            self.bshot.append(bs.Bshot1(self.bshot_speed_rate, self.bshot_angle_rate, left, right))

    def set_data(self):
        self.live_flag = True
        self.b_hit = True

    def opening(self):
        self.move_angle -= 1
        self.y += round(math.sin(math.radians(self.move_angle)), 2) * 3
        self.rect.center = (self.x, self.y)
        if self.move_angle == 0:
            self.control.op_end()

    def update(self):
        if self.live_flag == True:
            self.move_count += 1
            self.shot_time += 1
            if self.move_pattern == 0:
                self.move_angle += 1
                self.x += round(math.cos(math.radians(self.move_angle)), 2) * self.b_speed

            if self.move_count < 340:
                if self.shot_time == self.interval:
                    self.set_bshot()
                    self.shot_time = 0
            elif self.move_count >= 360:
                if self.shot_pattern == 0:
                    self.shot_pattern = 1
                    self.bshot_speed_rate *= -1
                else:
                    self.shot_pattern = 0
                    self.bshot_speed_rate *= -1
                self.move_count = 0
                self.shot_time = 0
                self.move_angle = 0
                #self.control.rocordAidata(0)

            self.rect.center = (self.x, self.y)
            self.bos_point = [[self.x - 15, self.y - 15],[self.x + 15, self.y - 15],[self.x, self.y + 15]]

            #被ダメージ時の無敵時間の管理
            if self.b_hit == False:
                if self.hit_count / 2 % 2 == 0:
                    self.hit_count += 1
                    self.image = self.images[1]
                else:
                    self.hit_count += 1
                    self.image = self.images[0]
                if self.hit_count == 11:#奇数である必要がある
                    self.hit_count = 0
                    self.b_hit = True

    def b_damage(self, power):
        self.b_hit = False
        self.life -= power
        if self.life <= 0:
            self.live_flag = False
            self.control.game_clear()
            self.control.score_plus(self.score)
            self.rect.center = (0, -100)

    def set_bshot(self):
        if self.shot_pattern == 0:
            for i in range(self.shotcount):
                for j in range(self.bs_num):
                    if self.bshot[j].bs_flag() == False:
                        self.bshot[j].set_shot(self.rect.center, self.bshot_speed, self.angle + 360*float(i)/self.shotcount, self.bshot_speed_rate)
                        break
            self.angle += self.angle_rate
            if self.angle > 360:
                self.angle -= 360
        else:
            for i in range(self.shotcount):
                for j in range(self.bs_num):
                    if self.bshot[j].bs_flag() == False:
                        self.bshot[j].set_shot(self.rect.center, self.bshot_speed, self.angle + 360*float(i)/self.shotcount, self.bshot_speed_rate)
                        break
            self.angle -= self.angle_rate
            if self.angle < 0:
                self.angle += 360

    def all_kill_shot(self):
        for i in range(self.bs_num):
            if self.bshot[i].bs_flag():
                self.bshot[i].bs_hit()

    def b_point(self):
        return self.bos_point

    def b_rad(self):
        return self.bos_rad

    def b_health(self):
        return self.b_hit

    def b_bshot_num(self):
        return self.bs_num

    def b_bshot_flag(self, id):
        return self.bshot[id].bs_flag()

    def b_bshot_data(self, id):
        return self.bshot[id].bs_rad(), self.bshot[id].bs_point()
