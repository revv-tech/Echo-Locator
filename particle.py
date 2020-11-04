import pygame as pg
from random import randint


class Particle:
    def __init__(self):
        info = pg.display.Info()
        self.image = None
        pg.math.Vector2()
        self.pos = pg.Vector2(250,250)
        self.heading = 0
        self.vel = pg.math.Vector2((0, 0))

    def update(self, screen: pg.display):
        #self.move_random()
        self.image = pg.draw.circle(screen, pg.Color('white'), (250, 250), 4, 2)

    def move_random(self):
        info = pg.display.Info()

        self.pos += self.vel
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x += 5
        elif self.pos.x > info.current_w:
            self.pos.x = info.current_w - 1
            self.vel.x -= 5

        if self.pos.y < 0:
            self.pos.y = 0
            self.vel.y += 5
        elif self.pos.y > info.current_h:
            self.pos.y = info.current_h - 1
            self.vel.y -= 5

        self.vel.x += randint(-5, 5)
        self.vel.y += randint(-5, 5)