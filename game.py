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

    bg_path = os.path.join(os.getcwd(), "png/bg.png")
    bg = pygame.image.load(bg_path)
    #bg = pygame.image.load("../png/bg.png")
    #rect_bg = bg.get_rect()
    #rect_bg.topleft = (150, 0)

    fream_path = os.path.join(os.getcwd(), "png/non_board.png")
    fream = pygame.image.load(fream_path)
    #bg = pygame.image.load("../png/bg.png")

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
    screen.blit(bg, (150, 0))
    screen.blit(fream, (0, 0))

    screen.blit(title, rect_title)

    #screen.blit(start, rect_start)

    #screen.blit(exit, rect_exit)
    while (running):
        #screen.fill((0,0,255))  #画面を黒で塗りつぶす

        #screen.blit(bg, rect_bg)
        #screen.blit(fream, rect_fream)
        #screen.blit(title, rect_title)
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
                    select(screen, bg, fream)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    screen.blit(title, rect_title)
                if rect_exit.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

def select(screen, bg, fream):
    button = pygame.Rect(250, 50, 100, 50)  # creates a rect object
    #button2 = pygame.Rect(250, 150, 100, 50)  # creates a rect object
    #button3 = pygame.Rect(350, 350, 100, 50)  # creates a rect object
    button4 = pygame.Rect(150, 350, 100, 50)  # creates a rect object

    font = pygame.font.SysFont(None, 25)

    text1 = font.render("STAGE1", True, (0,0,0))
    #text2 = font.render("STAGE2", True, (0,0,0))
    #text3 = font.render("EQUIP", True, (0,0,0))
    text4 = font.render("BACK", True, (0,0,0))

    #screen.fill((255,255,255))  #画面を黒で塗りつぶす

    running = True
    while (running):
        #screen.blit(bg, rect_bg)
        #screen.blit(self.fream, self.rect_fream)

        pygame.draw.rect(screen, (0, 255, 0), button)
        #pygame.draw.rect(screen, (0, 255, 0), button2)
        #pygame.draw.rect(screen, (0, 255, 0), button3)
        pygame.draw.rect(screen, (0, 255, 0), button4)

        screen.blit(text1, (260, 60))
        #screen.blit(text2, (260,160))
        #screen.blit(text3, (360,360))
        screen.blit(text4, (160,360))

        pygame.display.update()
        screen.blit(bg, (150, 0))
        screen.blit(fream, (0, 0))
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
                if button.collidepoint(event.pos):
                    control = con.Control()
                    control.set_data(1, 12, [1,1,1,1,1,1,2,2,2,2,2,2])
                    control.control()
                    running = False
                #if button2.collidepoint(event.pos):
                #    control = con.Control()
                #    control.set_data(2, 12, [1,1,1,1,1,1,2,2,2,2,2,2])
                #    control.control()
                #    running = False
                if button4.collidepoint(event.pos):
                    running = False

if __name__ == "__main__":
    main()
