# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

class Backboard(pygame.sprite.Sprite):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_size()
        pygame.sprite.Sprite.__init__(self, self.containers)
        fream_path = os.path.join(os.getcwd(),"png/board.png")
        self.image = pygame.image.load(fream_path)
        self.rect = Rect(0, 0, self.w, self.h)
        self.font = pygame.font.SysFont(None, 40)
        self.score = 0
        self.score_txt = self.font.render(str('{:0=7}'.format(self.score)), True, (255,255,255))
        self.cover = pygame.Rect(470, 5, 80, 25)
        self.hp_long = 1
        self.hp_long2 = 1
        self.hp = pygame.Rect(131, 292, 1, 27)
        self.hp2 = pygame.Rect(131, 263, 1, 27)
        self.item_n = 5
        self.item_txt = self.font.render(str(self.item_n), True, (255,255,255))

    def set_score(self, s):
        self.score += s
        self.score_txt = self.font.render(str('{:0=7}'.format(self.score)), True, (255,255,255))

    def set_hp(self):
        if self.hp_long < 125:
            self.hp_long += 26
            self.hp = pygame.Rect(131 - self.hp_long, 292, self.hp_long, 27)
            #self.hp.move_ip(-self.hp_n, 0)
            #self.hp.inflate_ip(self.hp_n, 0)
        else:
            self.hp_long2 += 26
            self.hp2 = pygame.Rect(131 - self.hp_long2, 263, self.hp_long2, 27)
            #self.hp2.move_ip(-self.hp_n2, 0)
            #self.hp2.inflate_ip(self.hp_n2, 0)

    def set_item(self):
        self.item_n -= 1
        self.item_txt = self.font.render(str(self.item_n), True, (255,255,255))

    def update(self):
        self.screen.blit(self.score_txt, (470, 275))
        self.screen.blit(self.item_txt, (68, 354))
        pygame.draw.rect(self.screen, (0,0,0), self.cover)
        pygame.draw.rect(self.screen, (0,0,0), self.hp)
        pygame.draw.rect(self.screen, (0,0,0), self.hp2)
