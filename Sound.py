# coding: utf-8
import pygame
from pygame.locals import *
import sys
import os

class Sound():
    def __init__(self):
        pygame.mixer.init()
        self.bgm_path = os.path.join(os.getcwd(), "sounds/cyber39.mp3")
        pygame.mixer.music.load(self.bgm_path)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def start(self):
        pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
