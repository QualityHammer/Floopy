import pygame as pg
from settings import *


class Score:

    def __init__(self):
        pg.font.init()
        self.score = 0
        self.font = pg.font.SysFont('impact', 36)
        self.font_render = self.font.render(str(self.score), True, BLUE)
    
    def update(self):
        self.score += 1
        self.font_render = self.font.render(str(self.score), True, BLUE)
    
    def draw(self, screen):
        screen.blit(self.font_render, SCORE_POS)