import pygame as pg
import  random

background4 =[pg.image.load(f'спрайты/гг диалог 2/фонКомнаты4/фон{i}-1.png.png') for i in range(0,5)]

class Background4(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 2/нпс3/нпс3_8.png')
        self.rect = self.image.get_rect(center=(x, y))
    def anym(self):
        self.jump_time = pg.time.get_ticks()
        frame_duration = 450  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(background4)
        self.image = background4[frame_index]
    def update(self):
         self.anym()

class Unit(pg.sprite.Sprite):
    def __init__(self):
        self.last = pg.time.get_ticks()
        self.cooldown = 350
    def anym_background(self):
        now = pg.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.a = random.randint(0,4)
    def update(self):
         self.anym_background()
