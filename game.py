# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

import Control as con
WIDTH = 600
HEIGHT = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    #screen = pygame.display.get_surface()
    pygame.display.set_caption("GAME")

    stagecode = 1
    e_num = 12
    e_kind = [1,1,1,1,1,1,2,2,2,2,2,2]

    bg_path = os.path.join(os.getcwd(), "png/bg.png")
    bg = pygame.image.load(bg_path)
    #bg = pygame.image.load("../png/bg.png")
    rect_bg = bg.get_rect()
    rect_bg.topleft = (150, 0)

    fream_path = os.path.join(os.getcwd(), "png/non_board.png")
    fream = pygame.image.load(fream_path)
    #bg = pygame.image.load("../png/bg.png")
    rect_fream = fream.get_rect()
    rect_fream.topleft = (0, 0)

    #title = pygame.image.load("../png/title.png")
    title_path = os.path.join(os.getcwd(), "png/title.png")
    title = pygame.image.load(title_path)
    rect_title = title.get_rect()
    rect_title.center = (300, 150)

    #start = pygame.image.load("../png/start.png")
    start_path = os.path.join(os.getcwd(), "png/start.png")
    start = pygame.image.load(start_path)
    rect_start = start.get_rect()
    rect_start.center = (200, 350)

    #exit = pygame.image.load("../png/Exit.png")
    exit_path = os.path.join(os.getcwd(), "png/Exit.png")
    exit = pygame.image.load(exit_path)
    rect_exit = exit.get_rect()
    rect_exit.center = (400, 350)

    font = pygame.font.SysFont(None, 25)

    running = True
    while (running):
        #screen.fill((0,0,255))  #画面を黒で塗りつぶす

        screen.blit(bg, rect_bg)
        screen.blit(fream, rect_fream)

        screen.blit(title, rect_title)

        screen.blit(start, rect_start)

        screen.blit(exit, rect_exit)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_start.collidepoint(event.pos):
                    control = con.Control()
                    control.set_data(stagecode, e_num, e_kind)
                    control.control()
                if rect_exit.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
