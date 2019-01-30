import pygame as pg
import numpy as np
from settings import *


class Pipe(pg.sprite.Sprite):

    WIDTH = 100

    def __init__(self, y, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Pipe.WIDTH, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH, y)
        self.frozen = False
    
    def update(self):
        if not self.frozen:
            self.rect.x += -PIPE_SPEED


class Pipes:

    def __init__(self):
        self.gap = np.random.randint(MIN_GAP, MAX_GAP)
        self.bx = np.random.randint(100 + self.gap, HEIGHT - 100)
        self.top = Pipe(0, self.bx - self.gap)
        self.bottom = Pipe(self.bx, HEIGHT - self.bx)
        self.destroyed = False
        self.passed = False
    
    def draw(self, screen):
        screen.blit(self.top.image, (self.top.rect.x, self.top.rect.y))
        screen.blit(self.bottom.image, (self.bottom.rect.x, self.bottom.rect.y))
    
    def freeze(self):
        self.top.frozen = True
        self.bottom.frozen = True
    
    def groupie(self, group):
        group.add(self.top)
        group.add(self.bottom)
    
    def update(self, score):
        self.top.update()
        self.bottom.update()
        if self.top.rect.right < 0:
            self.top.kill
            self.bottom.kill
            self.destroyed = True
        if self.top.rect.right < 100 and not self.passed:
            self.passed = True
            score.update()
