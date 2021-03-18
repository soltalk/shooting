# coding: utf-8
import pygame
from pygame.locals import *
import sys
import math
#import pandas as pd
import csv
import random
import os

import Background as bg
import Backboard as bb
import Player
import Pshot as ps
import Item as it
import Enemy1 as ene1
import Enemy2 as ene2
import Eshot as es
import Boss1 as bo1
import Bshot1 as bs1
import Sound

FPS = 30

WIDTH = 600
HEIGHT = 400

class Control(object):
    singleton = None
    def __new__( cls, *args, **kwargs ):
        if cls.singleton == None:
            cls.singleton = super().__new__( cls )

        return cls.singleton

    def set_data(self, code, num, kind):
        self.left, self.right = 150, 450
        self.screen = pygame.display.get_surface()
        self.game_exit = True
        self.clear_flag = False
        self.over_flag = True
        self.boss_flag = False
        self.pose_flag = False
        self.stagecode = code
        self.e_num = num
        self.e_kind = kind

    def control(self):
        enemy = []
        hit_count = 0
        time = 0
        data1_path = os.path.join(os.getcwd(), "data/stage" + str(self.stagecode) + "data.csv")
        with open(data1_path) as f:
            reader = csv.reader(f)
            line = [row for row in reader]

        #start_path = os.path.join(os.getcwd(), "png/start.png")
        #start = pygame.image.load(start_path)
        #rect_start = start.get_rect()

        exit_path = os.path.join(os.getcwd(), "png/Exit.png")
        self.exit = pygame.image.load(exit_path)
        self.rect_exit = self.exit.get_rect()

        next = 1
        columns = len(line) - 1
        set_data = [int(s) for s in line[next]]

        #BS = pygame.sprite.Group()
        road = pygame.sprite.LayeredUpdates()
        last = pygame.sprite.LayeredUpdates()
        clear = pygame.sprite.LayeredUpdates()
        Player.Player.containers = road, last, clear
        bg.Background.containers = road, last, clear
        bb.Backboard.containers = road, last, clear
        ps.Pshot.containers = road, last, clear
        it.Item.containers = road, last, clear
        ene1.Enemy1.containers = road
        ene2.Enemy2.containers = road
        es.Eshot.containers = road
        bo1.Boss1.containers = last
        bs1.Bshot1.containers = last

        self.player = Player.Player(self.left, self.right)
        self.p_rad = self.player.p_rad()
        #self.n_rad = self.player.pn_rad()
        self.ps_num = self.player.p_pshot_num()
        #self.life = self.player.p_life()
        self.bomb_flag = False

        self.makeEnemy(enemy)

        boss = self.makeBoss()

        back = bg.Background(0, self.stagecode, self.left, self.right)
        back2 = bg.Background(1, self.stagecode, self.left, self.right)
        road.move_to_back(back)
        road.move_to_back(back2)
        last.move_to_back(back)
        last.move_to_back(back2)
        clear.move_to_back(back)
        clear.move_to_back(back2)

        self.fream = bb.Backboard()
        self.sound = Sound.Sound()

        #pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 35)
        self.pause_txt = self.font.render('PAUSE', True, (255,255,255))

        # ゲームのメイン部分
        while (self.game_exit):
            road.draw(self.screen)

            road.update()

            if time == int(set_data[0]):
                if set_data[1] == 0:
                    for i in range(self.e_num):
                        if enemy[i].e_live() == False and enemy[i].e_id() == set_data[2]:
                            enemy[i].set_data(set_data[3], set_data[4], set_data[5])
                            break
                else:
                    self.boss_flag = True
                    self.game_exit = False
                if next < columns:
                    next += 1
                    set_data = [int(s) for s in line[next]]

            self.hit(enemy)

            if self.bomb_flag:
                self.bomb_e_hit(enemy)
                self.bomb_flag = False
                self.fream.set_item()

            time += 1

            clock.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    #pygame.mixer.music.stop()
                    self.game_end()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                    if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                    if event.key == K_q:
                        #pygame.mixer.music.stop()
                        self.pause()

        if self.boss_flag:
            del enemy
            while(self.boss_flag):
                last.draw(self.screen)
                clear.update()
                boss.opening()

                clock.tick(FPS)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        #pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                        # qキーなら終了
                        if event.key == K_q:
                            #pygame.mixer.music.stop()
                            self.pause()

            self.game_exit = True
            boss.set_data()
            while (self.game_exit):
                last.draw(self.screen)

                last.update()
                self.boss_hit(boss)

                if self.bomb_flag:
                    self.bomb_b_hit(boss)
                    self.bomb_flag = False
                    self.fream.set_item()

                clock.tick(FPS)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        #pygame.mixer.music.stop()
                        self.game_end()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                        if event.key == K_q:
                            #pygame.mixer.music.stop()
                            self.pause()

        if self.clear_flag:
            self.score_plus(500 * self.player.p_life())
            clear_txt = self.font.render('CLEAR', True, (255,255,255))
            while(self.clear_flag):
                clear.draw(self.screen)
                clear.update()
                clock.tick(FPS)

                self.rect_exit.center = (300, 350)
                self.screen.blit(self.exit, self.rect_exit)

                self.screen.blit(clear_txt, (250, 150))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        #pygame.mixer.music.stop()
                        #self.saveAidata()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.rect_exit.collidepoint(event.pos):
                            self.clear_flag = False
        if self.over_flag:
            over_txt = self.font.render('GAME OVER', True, (255,255,255))
            while(self.over_flag):
                self.rect_exit.center = (300, 350)
                self.screen.blit(self.exit, self.rect_exit)

                self.screen.blit(over_txt, (220, 150))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        #pygame.mixer.music.stop()
                        #self.saveAidata()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.rect_exit.collidepoint(event.pos):
                            self.over_flag = False
        #self.saveAidata()

    def pause(self):
        self.pose_flag = True
        self.sound.pause()
        while(self.pose_flag):
            self.rect_exit.center = (300, 350)
            self.screen.blit(self.exit, self.rect_exit)

            self.screen.blit(self.pause_txt, (260, 150))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    #pygame.mixer.music.stop()
                    #self.saveAidata()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                    if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                    if event.key == K_q:
                        #pygame.mixer.music.stop()
                        self.pose_flag = False
                        self.sound.start()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_exit.collidepoint(event.pos):
                        self.game_end()
                        self.over_flag = False
                        self.pose_flag = False

    def hit(self, enemy):
        if self.player.p_health():
            p_p = self.player.p_point()
            for i in range(self.e_num):
                if enemy[i].e_live():
                    e_p = enemy[i].e_point()
                    e_rad = enemy[i].e_rad()
                    distance = self.get_distance(float(p_p[0]), float(p_p[1]), float(e_p[0]), float(e_p[1]))
                    if self.p_rad + e_rad > distance:
                        self.player.p_damage()
                        #self.life_txt = self.font.render(str(self.player.p_life()), True, (255,255,255))
                        self.fream.set_hp()
                        break
                    #if self.n_rad + e_rad > distance:
                    #    self.near_hit += 1
                es_num = enemy[i].e_eshot_num()
                for j in range(es_num):
                    if enemy[i].e_eshot_flag(j):
                        es_rad,es_p = enemy[i].e_eshot_data(j)
                        distance = self.get_distance(float(p_p[0]), float(p_p[1]), float(es_p[0]), float(es_p[1]))
                        if self.p_rad + es_rad > distance:
                            self.player.p_damage()
                            #self.life_txt = self.font.render(str(self.player.p_life()), True, (255,255,255))
                            self.fream.set_hp()
                            break
                        #if self.n_rad + es_rad > distance:
                        #    self.near_hit += 1;
                else:
                    continue
                break

        for i in range(self.e_num):
            if enemy[i].e_health():
                e_p = enemy[i].e_point()
                e_rad = enemy[i].e_rad()
                for j in range(self.ps_num):
                    if self.player.p_pshot_flag(j):
                        ps_rad,ps_p,ps_pow = self.player.p_pshot_data(j)
                        distance = self.get_distance(float(ps_p[0]), float(ps_p[1]), float(e_p[0]), float(e_p[1]))
                        if ps_rad + e_rad > distance:
                            enemy[i].e_damage(ps_pow)
                            self.player.kill_shot(j)
                            break

    def boss_hit(self, boss):
        b_p = boss.b_point()
        b_rad = boss.b_rad()
        b_num = len(b_rad)

        if self.player.p_health():
            p_p = self.player.p_point()
            bs_num = boss.b_bshot_num()
            for i in range(bs_num):
                if boss.b_bshot_flag(i):
                    bs_rad,bs_p = boss.b_bshot_data(i)
                    distance = self.get_distance(float(p_p[0]), float(p_p[1]), float(bs_p[0]), float(bs_p[1]))
                    if self.p_rad + bs_rad > distance:
                        self.player.p_damage()
                        #self.life_txt = self.font.render(str(self.player.p_life()), True, (255,255,255))
                        self.fream.set_hp()
                        break
                    #if self.n_rad + bs_rad > distance:
                    #    self.near_hit += 1;
        if self.player.p_health():
            for i in range(b_num):
                distance = self.get_distance(float(p_p[0]), float(p_p[1]), float(b_p[i][0]), float(b_p[i][1]))
                if self.p_rad + b_rad[i] > distance:
                    self.player.p_damage()
                    #self.life_txt = self.font.render(str(self.player.p_life()), True, (255,255,255))
                    self.fream.set_hp()
                    break

        if boss.b_health():
            for i in range(b_num):
                for j in range(self.ps_num):
                    if self.player.p_pshot_flag(j):
                        ps_rad,ps_p,ps_pow = self.player.p_pshot_data(j)
                        distance = self.get_distance(float(ps_p[0]), float(ps_p[1]), float(b_p[i][0]), float(b_p[i][1]))
                        if ps_rad + b_rad[i] > distance:
                            boss.b_damage(ps_pow)
                            self.player.kill_shot(j)
                            break

    def bomb_e_hit(self, enemy):
        bomb_pow = self.player.p_bomb_power()
        for i in range(self.e_num):
            if enemy[i].e_health():
                enemy[i].e_damage(bomb_pow)
            enemy[i].all_kill_shot()

    def bomb_b_hit(self, boss):
        bomb_pow = self.player.p_bomb_power()
        if boss.b_health():
            boss.b_damage(bomb_pow)
        boss.all_kill_shot()

    def get_distance(self, x1, y1, x2, y2):
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d

    def game_end(self):
        self.game_exit = False
        self.sound.stop()

    def op_end(self):
        self.boss_flag = False

    def game_clear(self):
        self.clear_flag = True
        self.game_exit = False
        self.over_flag = False

    def score_plus(self, s):
        #self.score += s
        #self.score_txt = self.font.render(str(self.score), True, (255,255,255))
        self.fream.set_score(s)

    def bomb(self):
        self.bomb_flag = True

    def makeEnemy(self, enemy):
        for i in range(self.e_num):
            #enemy.append(ene.Enemy1(e_df.loc[self.e_kind[i]]))
            if self.e_kind[i] == 1:
                enemy.append(ene1.Enemy1(self.left, self.right))
            elif self.e_kind[i] == 2:
                enemy.append(ene2.Enemy2(self.left, self.right))

    def makeBoss(self):
        if self.stagecode == 1:
            return bo1.Boss1(self.left, self.right)

'''
    def rocordAidata(self, check):
        if check == 1:
            self.ai_enemy1data.append([self.life - self.player.p_life()])
            self.ai_enemy1data[len(self.ai_enemy1data)-1].append(self.near_hit)
            self.life = self.player.p_life()
        elif check == 2:
            self.ai_enemy2data.append([self.life - self.player.p_life()])
            self.ai_enemy2data[len(self.ai_enemy2data)-1].append(self.near_hit)
            self.life = self.player.p_life()
        else:
            self.ai_bossdata.append([self.life - self.player.p_life()])
            self.ai_bossdata[len(self.ai_bossdata)-1].append(self.near_hit)
            self.life = self.player.p_life()
        self.near_hit = 0

    def saveAidata(self):
        ene1 = []
        for i in range(len(self.ai_enemy1data)):
            ene1.append(self.enemy1data + self.ai_enemy1data[i-1] + ['e1'])

        ene2 = []
        for i in range(len(self.ai_enemy2data)):
            ene2.append(self.enemy2data + self.ai_enemy2data[i-1] + ['e2'])

        bos = []
        for i in range(len(self.ai_bossdata)):
            bos.append(self.bossdata + self.ai_bossdata[i-1] + ['bos'])

        ai_data1_path = os.path.join(os.getcwd(), "data/stage" + str(self.stagecode) + "Aidata.csv")
        with open(ai_data1_path, 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(ene1)
            writer.writerows(ene2)
            writer.writerows(bos)
'''
