# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Control as con
import Pshot_normal as psno
import Pshot_laser as psls
import Pshot_rapid as psra
import Pshot_3way as ps3w
import Item as it

class Player(pygame.sprite.Sprite):
    def __init__(self, left, right):
        self.h = pygame.display.get_surface().get_height()
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = list()
        jiki_path = os.path.join(os.getcwd(),"png/jiki.png")
        self.images.append(pygame.image.load(jiki_path))
        jiki_path = os.path.join(os.getcwd(),"png/jiki2.png")
        self.images.append(pygame.image.load(jiki_path))
        jiki_path = os.path.join(os.getcwd(),"png/jiki3.png")
        self.images.append(pygame.image.load(jiki_path))
        self.images.append(pygame.Surface((1,1)))
        self.next = 1
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (300,200)
        self.p_hit = True
        self.hit_count = 0
        self.control = con.Control()
        self.play_rad = 4
        self.left = left
        self.right = right
        self.p_speed = 3
        self.life = 10
        #ショット関連
        self.shot_pattern = True
        self.reload_timer = 0
        shot_path = os.path.join(os.getcwd(),"data/shotfile.txt")
        f = open(shot_path, 'r')
        data = f.readlines()
        self.shot_type_a = int(data[0].rstrip('\n'))
        self.shot_type_b = int(data[1])
        f.close()
        self.make_shot(left, right)
        #アイテム関連
        self.item = it.Item()
        self.item_flag = False
        self.wait = 0
        self.item_count = 0

    def update(self):
        if self.p_hit == False:
            if self.hit_count / 2 % 2 == 0:
                self.hit_count += 1
                self.image = self.images[3]
            else:
                self.hit_count += 1
                self.image = self.images[0]
            if self.hit_count == 31:#奇数である必要がある
                self.hit_count = 0
                self.p_hit = True
        else:
            self.image = self.images[int(self.next/3)]
            if self.next != 8:
                self.next += 1
            else:
                self.next = 0

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
                self.control.bomb_hit()
            elif self.wait > 30:
                self.wait = 0
                self.item.set_out()
                self.item_flag = False

    def p_damage(self):
        self.p_hit = False
        self.life -= 1
        if self.life <= 0:
            self.image = self.images[3]
            self.control.game_end()

    def make_shot(self, left, right):

        #A
        if self.shot_type_a == 1:
            self.reload_time_a = 5  # リロード時間
            self.pshot_a = []
            self.ps_num_a = 10
            for _ in range(self.ps_num_a):
                self.pshot_a.append(psno.Pshot_normal(left, right))
        elif self.shot_type_a == 2:
            self.reload_time_a = 20  # リロード時間
            self.pshot_a = []
            self.ps_num_a = 6
            for _ in range(3):
                self.pshot_a.append(psls.Pshot_laser(left, right, True))
                self.pshot_a.append(psls.Pshot_laser(left, right, False))
        elif self.shot_type_a == 3:
            self.reload_time_a = 2  # リロード時間
            self.pshot_a = []
            self.ps_num_a = 15
            self.shot_way_a = 0
            for _ in range(15):
                self.pshot_a.append(psra.Pshot_rapid(left, right))
        elif self.shot_type_a == 4:
            self.reload_time_a = 7  # リロード時間
            self.pshot_a = []
            self.ps_num_a = 15
            for _ in range(15):
                self.pshot_a.append(ps3w.Pshot_3way(left, right))
        #B
        if self.shot_type_b == 1:
            self.reload_time_b = 5  # リロード時間
            self.pshot_b = []
            self.ps_num_b = 10
            for _ in range(self.ps_num_b):
                self.pshot_b.append(psno.Pshot_normal(left, right))
        elif self.shot_type_b == 2:
            self.reload_time_b = 20  # リロード時間
            self.pshot_b = []
            self.ps_num_b = 6
            for _ in range(3):
                self.pshot_b.append(psls.Pshot_laser(left, right, True))
                self.pshot_b.append(psls.Pshot_laser(left, right, False))
        elif self.shot_type_b == 3:
            self.reload_time_b = 2  # リロード時間
            self.pshot_b = []
            self.ps_num_b = 15
            self.shot_way_b = 0
            for _ in range(15):
                self.pshot_b.append(psra.Pshot_rapid(left, right))
        elif self.shot_type_b == 4:
            self.reload_time_b = 7  # リロード時間
            self.pshot_b = []
            self.ps_num_b = 15
            for _ in range(15):
                self.pshot_b.append(ps3w.Pshot_3way(left, right))

    def set_pshot(self):
        if self.shot_pattern:
            if self.shot_type_a < 3:
                if self.shot_type_a == 1:
                    for i in range(self.ps_num_a):
                        if self.pshot_a[i].ps_flag() == False:
                            self.pshot_a[i].set_shot(self.rect.center)
                            break
                else:
                    for i in range(0, self.ps_num_a, 2):
                        if self.pshot_a[i].ps_flag() == False:
                            self.pshot_a[i].set_shot((self.rect.centerx, self.rect.top))
                            self.pshot_a[i + 1].set_shot((self.rect.centerx, self.rect.top - 45))
                            break
            else:
                if self.shot_type_a == 3:
                    for i in range(self.ps_num_a):
                        if self.pshot_a[i].ps_flag() == False:
                            self.pshot_a[i].set_shot((self.rect.centerx + self.shot_way_a, self.rect.top))
                            if self.shot_way_a >= 3:
                                self.shot_way_a = -3
                            else:
                                self.shot_way_a += 3
                            break
                else:
                    for i in range(0, self.ps_num_a, 3):
                        if self.pshot_a[i].ps_flag() == False:
                            self.pshot_a[i].set_shot((self.rect.centerx, self.rect.top))
                            self.pshot_a[i + 1].set_shot((self.rect.centerx, self.rect.top))
                            self.pshot_a[i + 2].set_shot((self.rect.centerx, self.rect.top))
                            break
            self.reload_timer = self.reload_time_a
        else:
            if self.shot_type_b < 3:
                if self.shot_type_b == 1:
                    for i in range(self.ps_num_b):
                        if self.pshot_b[i].ps_flag() == False:
                            self.pshot_b[i].set_shot(self.rect.center)
                            break
                else:
                    for i in range(0, self.ps_num_b, 2):
                        if self.pshot_b[i].ps_flag() == False:
                            self.pshot_b[i].set_shot((self.rect.centerx, self.rect.top))
                            self.pshot_b[i + 1].set_shot((self.rect.centerx, self.rect.top - 45))
                            break
            else:
                if self.shot_type_b == 3:
                    for i in range(self.ps_num_b):
                        if self.pshot_b[i].ps_flag() == False:
                            self.pshot_b[i].set_shot((self.rect.centerx + self.shot_way_b, self.rect.top))
                            if self.shot_way_b >= 3:
                                self.shot_way_b = -3
                            else:
                                self.shot_way_b += 3
                            break
                else:
                    for i in range(0, self.ps_num_b, 3):
                        if self.pshot_b[i].ps_flag() == False:
                            self.pshot_b[i].set_shot((self.rect.centerx, self.rect.top), 0)
                            self.pshot_b[i + 1].set_shot((self.rect.centerx, self.rect.top), 1)
                            self.pshot_b[i + 2].set_shot((self.rect.centerx, self.rect.top), 2)
                            break
            self.reload_timer = self.reload_time_b

    def p_point(self):
        (x,y) = self.rect.center
        return [x, y]

    def p_rad(self):
        return self.play_rad

    def p_life(self):
        return self.life

    def p_health(self):
        return self.p_hit

    def change_shot(self):
        if self.shot_pattern:
            self.shot_pattern = False
            self.reload_timer = self.reload_time_b
        else:
            self.shot_pattern = True
            self.reload_timer = self.reload_time_a

    def p_pshot_num(self):
        return self.ps_num_a, self.ps_num_b

    def p_pshot_flag_a(self, id):
        return self.pshot_a[id].ps_flag()

    def p_pshot_flag_b(self, id):
        return self.pshot_b[id].ps_flag()

    def p_bomb_power(self):
        return self.item.bomb_power()

    def p_item(self):
        return self.item_count
