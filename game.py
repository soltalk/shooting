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
    pygame.display.set_caption("GAME")

    bg_path = os.path.join(os.getcwd(), "png/bg.png")
    bg = pygame.image.load(bg_path)
    #bg = pygame.image.load("../png/bg.png")
    #rect_bg = bg.get_rect()
    #rect_bg.topleft = (150, 0)

    fream_path = os.path.join(os.getcwd(), "png/non_board.png")
    fream = pygame.image.load(fream_path)

    title_path = os.path.join(os.getcwd(), "png/title.png")
    title = pygame.image.load(title_path)
    rect_title = title.get_rect()
    rect_title.center = (300, 150)

    start_path = os.path.join(os.getcwd(), "png/start.png")
    start = pygame.image.load(start_path)
    rect_start = start.get_rect()
    rect_start.center = (200, 350)

    exit_path = os.path.join(os.getcwd(), "png/Exit.png")
    exit = pygame.image.load(exit_path)
    rect_exit = exit.get_rect()
    rect_exit.center = (400, 350)

    font = pygame.font.SysFont(None, 25)

    running = True
    screen.blit(bg, (150, 0))
    screen.blit(fream, (0, 0))

    screen.blit(title, rect_title)
    screen.blit(start, rect_start)
    screen.blit(exit, rect_exit)
    pygame.display.update()

    while (running):
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    screen.blit(title, rect_title)
                    screen.blit(start, rect_start)
                    screen.blit(exit, rect_exit)
                    pygame.display.update()
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    screen.blit(title, rect_title)
                    screen.blit(start, rect_start)
                    screen.blit(exit, rect_exit)
                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_start.collidepoint(event.pos):
                    select(screen, bg, fream)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    screen.blit(title, rect_title)
                    screen.blit(start, rect_start)
                    screen.blit(exit, rect_exit)
                    pygame.display.update()
                if rect_exit.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

def select(screen, bg, fream):
    button = pygame.Rect(250, 50, 100, 50)
    #button2 = pygame.Rect(250, 150, 100, 50)
    button3 = pygame.Rect(350, 350, 100, 50)
    button4 = pygame.Rect(150, 350, 100, 50)

    font = pygame.font.SysFont(None, 25)

    text1 = font.render("STAGE1", True, (0,0,0))
    #text2 = font.render("STAGE2", True, (0,0,0))
    text3 = font.render("EQUIP", True, (0,0,0))
    text4 = font.render("BACK", True, (0,0,0))

    screen.blit(bg, (150, 0))
    screen.blit(fream, (0, 0))

    pygame.draw.rect(screen, (0, 255, 0), button)
    #pygame.draw.rect(screen, (0, 255, 0), button2)
    pygame.draw.rect(screen, (0, 255, 0), button3)
    pygame.draw.rect(screen, (0, 255, 0), button4)

    screen.blit(text1, (260, 60))
    #screen.blit(text2, (260,160))
    screen.blit(text3, (360,360))
    screen.blit(text4, (160,360))

    running = True
    pygame.display.update()
    while (running):
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 0)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    pygame.draw.rect(screen, (0, 255, 0), button)
                    #pygame.draw.rect(screen, (0, 255, 0), button2)
                    pygame.draw.rect(screen, (0, 255, 0), button3)
                    pygame.draw.rect(screen, (0, 255, 0), button4)

                    screen.blit(text1, (260, 60))
                    #screen.blit(text2, (260,160))
                    screen.blit(text3, (360,360))
                    screen.blit(text4, (160,360))
                    pygame.display.update()
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    pygame.draw.rect(screen, (0, 255, 0), button)
                    #pygame.draw.rect(screen, (0, 255, 0), button2)
                    pygame.draw.rect(screen, (0, 255, 0), button3)
                    pygame.draw.rect(screen, (0, 255, 0), button4)

                    screen.blit(text1, (260, 60))
                    #screen.blit(text2, (260,160))
                    screen.blit(text3, (360,360))
                    screen.blit(text4, (160,360))
                    pygame.display.update()

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
                if button3.collidepoint(event.pos):
                    equip(screen)
                    screen.blit(bg, (150, 0))
                    screen.blit(fream, (0, 0))
                    pygame.draw.rect(screen, (0, 255, 0), button)
                    #pygame.draw.rect(screen, (0, 255, 0), button2)
                    pygame.draw.rect(screen, (0, 255, 0), button3)
                    pygame.draw.rect(screen, (0, 255, 0), button4)

                    screen.blit(text1, (260, 60))
                    #screen.blit(text2, (260,160))
                    screen.blit(text3, (360,360))
                    screen.blit(text4, (160,360))
                    pygame.display.update()
                if button4.collidepoint(event.pos):
                    running = False

def equip(screen):
    pygame.draw.rect(screen, (90, 90, 90), (150, 0, 300, 400))

    shot_path = os.path.join(os.getcwd(),"data/shotfile.txt")
    f = open(shot_path, 'r')
    data = f.readlines()
    shot_a = int(data[0].rstrip('\n')) - 1
    shot_b = int(data[1]) - 1
    f.close()

    #shot_list = [True, True, True, True]
    rect_list = []

    no_path = os.path.join(os.getcwd(), "png/no_button.png")
    no = pygame.image.load(no_path)
    #rect_no = no.get_rect()
    rect_list.append(no.get_rect())
    #rect_no.topleft = (160, 200)
    rect_list[0].topleft = (160, 200)

    la_path = os.path.join(os.getcwd(), "png/la_button.png")
    la = pygame.image.load(la_path)
    rect_list.append(la.get_rect())
    rect_list[1].topleft = (230, 200)

    ra_path = os.path.join(os.getcwd(), "png/ra_button.png")
    ra = pygame.image.load(ra_path)
    rect_list.append(ra.get_rect())
    rect_list[2].topleft = (300, 200)

    way_path = os.path.join(os.getcwd(), "png/3w_button.png")
    way = pygame.image.load(way_path)
    rect_list.append(way.get_rect())
    rect_list[3].topleft = (370, 200)

    pre_path = os.path.join(os.getcwd(), "png/preset.png")
    pre1 = pygame.image.load(pre_path)
    rect_pre1 = pre1.get_rect()
    rect_pre1.topleft = (220, 85)
    pre2 = pygame.image.load(pre_path)
    rect_pre2 = pre2.get_rect()
    rect_pre2.topleft = (310, 85)

    menu_path = os.path.join(os.getcwd(), "png/shotmenu.png")
    menu = pygame.image.load(menu_path)

    enter_path = os.path.join(os.getcwd(), "png/enter.png")
    enter = pygame.image.load(enter_path)
    rect_enter = enter.get_rect()
    rect_enter.topleft = (300, 75)

    button = pygame.Rect(150, 350, 100, 50)
    font = pygame.font.SysFont(None, 25)
    text = font.render("BACK", True, (0,0,0))

    enter_flag = True

    pygame.draw.rect(screen, (0, 255, 0), button)
    screen.blit(text, (160,360))

    rect_list[shot_a].topleft = (220, 85)
    rect_pre1.topleft = (160 + 70 * shot_a, 200)

    rect_list[shot_b].topleft = (310, 85)
    rect_pre2.topleft = (160 + 70 * shot_b, 200)


    running = True
    while (running):
        screen.blit(menu, (210,35))
        screen.blit(enter, rect_enter)

        screen.blit(no, rect_list[0])
        screen.blit(la, rect_list[1])
        screen.blit(ra, rect_list[2])
        screen.blit(way, rect_list[3])

        screen.blit(pre1, rect_pre1)
        screen.blit(pre2, rect_pre2)

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
                if rect_enter.collidepoint(event.pos):
                    if enter_flag:#Trueで左、Falseで右
                        rect_enter.left = 210
                        enter_flag = False
                    else:
                        rect_enter.left = 300
                        enter_flag = True
                for i in range(4):
                    if rect_list[i].collidepoint(event.pos):
                        if enter_flag:
                            if shot_a != i:
                                rect_list[shot_a].topleft = (160 + 70 * shot_a, 200)
                                rect_list[i].topleft = (220, 85)
                                rect_pre1.topleft = (160 + 70 * i, 200)
                                shot_a = i
                        else:
                            if shot_b != i:
                                rect_list[shot_b].topleft = (160 + 70 * shot_b, 200)
                                rect_list[i].topleft = (310, 85)
                                rect_pre2.topleft = (160 + 70 * i, 200)
                                shot_b = i
                if button.collidepoint(event.pos):
                    f = open(shot_path, 'w')
                    datalist = [str(shot_a + 1), '\n', str(shot_b + 1)]
                    f.writelines(datalist)
                    f.close()
                    running = False

if __name__ == "__main__":
    main()
