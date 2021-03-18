# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Control as con
import Pshot as ps
import Item as it

class Player(pygame.sprite.Sprite):
    def __init__(self, left, right):
        self.h = pygame.display.get_surface().get_height()
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = list()
        #self.images.append(pygame.image.load("../png/jiki.png"))
        #self.images.append(pygame.image.load("../png/jiki_d.png"))
        jiki_path = os.path.join(os.getcwd(),"png/jiki.png")
        jiki_d_path = os.path.join(os.getcwd(),"png/jiki_d.png")
        self.images.append(pygame.image.load(jiki_path))
        self.images.append(pygame.image.load(jiki_d_path))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #(self.x, self.y)  = (300,200)
        self.rect.center = (300,200)
        self.p_hit = True
        self.hit_count = 0
        self.control = con.Control()
        self.play_rad = 4
        #self.near_rad = self.play_rad + 6
        self.left = left
        self.right = right
        self.p_speed = 3
        self.life = 10
        #ショット関連
        self.reload_time = 5  # リロード時間
        self.reload_timer = 0
        self.pshot = []
        self.ps_num = 10
        for i in range(self.ps_num):
            self.pshot.append(ps.Pshot(left, right))
        #アイテム関連
        self.item = it.Item()
        self.item_flag = False
        self.wait = 0
        self.item_count = 0

    def update(self):
        if self.p_hit == False:
            if self.hit_count / 2 % 2 == 0:
                self.hit_count += 1
                self.image = self.images[1]
            else:
                self.hit_count += 1
                self.image = self.images[0]
            if self.hit_count == 31:#奇数である必要がある
                self.hit_count = 0
                self.p_hit = True

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_c]:
            self.p_speed = 1
        else:
            self.p_speed = 3
        if pressed_key[K_LEFT]:
            self.rect.left -= self.p_speed
            if self.rect.left < self.left:
                self.rect.left = self.left
        if pressed_key[K_RIGHT]:
            self.rect.right += self.p_speed
            if self.rect.right > self.right:
                self.rect.right = self.right
        if pressed_key[K_UP]:
            self.rect.top -= self.p_speed
            if self.rect.top < 0:
                self.rect.top = 0
        if pressed_key[K_DOWN]:
            self.rect.bottom += self.p_speed
            if self.rect.bottom > self.h:
                self.rect.bottom = self.h

        if pressed_key[K_SPACE]:
            # リロード時間が0になるまで再発射できない
            if self.reload_timer > 0:
                # リロード中
                self.reload_timer -= 1
            else:
                # 発射
                self.set_pshot()
                self.reload_timer = self.reload_time

        if pressed_key[K_x]:
            if self.item_count < 5 and self.item_flag == False:
                self.item.set_bomb()
                self.item_flag = True
                self.item_count += 1

        if self.item_flag == True:
            self.wait += 1
            self.item.set_point(self.rect.center)
            if self.wait == 15:
                self.item.bomb_end()
                self.control.bomb()
            elif self.wait > 30:
                self.wait = 0
                self.item.set_out()
                self.item_flag = False

    def p_damage(self):
        self.p_hit = False
        self.life -= 1
        if self.life <= 0:
            self.image = self.images[1]
            self.control.game_end()

    def set_pshot(self):
        for i in range(self.ps_num):
            if self.pshot[i].ps_flag() == False:
                self.pshot[i].set_shot(self.rect.center)
                break

    def slow(self):
        self.p_speed = 1

    def quick(self):
        self.p_speed = 3

    def kill_shot(self, id):
        self.pshot[id].ps_hit()

    def p_point(self):
        (x,y) = self.rect.center
        return [x, y]

    def p_rad(self):
        return self.play_rad

    def p_life(self):
        return self.life

    def p_health(self):
        return self.p_hit

    def p_pshot_num(self):
        return self.ps_num

    def p_pshot_flag(self, id):
        return self.pshot[id].ps_flag()

    def p_pshot_data(self, id):
        return self.pshot[id].ps_rad(), self.pshot[id].ps_point(), self.pshot[0].ps_power()

    def p_bomb_power(self):
        return self.item.bomb_power()

    def p_item(self):
        return self.item_count
