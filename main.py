import pygame as pg
import numpy as np
import sys
from floop import Floop
from pipe import Pipes
from score import Score
from settings import *


class Main:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        self.pipes = []
        self.last_pipe = pg.time.get_ticks()
    
    def new(self):
        self.bird = Floop()
        self.b = pg.sprite.Group()
        self.b.add(self.bird)

        self.p = pg.sprite.Group()
        self.pipes.append(Pipes())
        self.pipes[0].groupie(self.p)

        self.score = Score()

        self.running = True
        self.run()
    
    def run(self):
        while self.running:
            self.events()
            self.updates()
            if not self.bird.dead:
                self.collisions()
            self.draw()
            self.clock.tick(FPS)

    def collisions(self):
        hits = pg.sprite.spritecollide(self.bird, self.p, False)
        if hits:
            self.bird.death(self.pipes)
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                self.playing = False
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.bird.jump()
    
    def updates(self):
        self.bird.update(self.pipes)
        if pg.time.get_ticks() - self.last_pipe > DELAY and not self.bird.dead:
            self.last_pipe = pg.time.get_ticks()
            self.pipes.append(Pipes())
        for pipe in self.pipes:
            pipe.update(self.score)
            if pipe.destroyed == True:
                self.pipes.remove(pipe)

    def draw(self):
        self.screen.fill(BLACK)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.b.draw(self.screen)
        self.score.draw(self.screen)
        pg.display.flip()


m = Main()
while m.running:
    m.new()

pg.quit()
