import pygame as pg
import numpy as np
from settings import *


class Floop(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.acc = 0
        self.xvel = 0
        self.vel = 0
        self.image = pg.Surface((2 * BIRD_RADIUS, 2 * BIRD_RADIUS))
        pg.draw.circle(self.image, BIRD_COLOR, (BIRD_RADIUS, BIRD_RADIUS), BIRD_RADIUS)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.dead = False

    def death(self, pipes):
        self.dead = True
        self.vel = np.random.choice([-1, 1]) * 10
        self.xvel = 10
        for pipe in pipes:
            pipe.freeze()

    def jump(self):
        if not self.dead:
            self.vel = JFORCE
    
    def update(self, pipes):
        if not self.dead:
            self.acc = GRAV
            self.vel += self.acc
        self.rect.y += self.vel
        self.rect.x += self.xvel
        if not self.dead:
            if self.rect.bottom > HEIGHT or self.rect.top < 0:
                self.death(pipes)
        else:
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.vel = -self.vel
            elif self.rect.top < 0:
                self.rect.top = 0
                self.vel = -self.vel
            if self.rect.left < 0:
                self.rect.left = 0
                self.xvel = -self.xvel
            elif self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.xvel = -self.xvel
