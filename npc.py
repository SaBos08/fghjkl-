import pygame as pg
import  random


Npc3_img =[pg.image.load(f'спрайты/гг диалог 2/нпс3/нпс3_{i}.png') for i in range(0,9)]
Npc4_img =[pg.image.load(f'спрайты/гг диалог 2/нпс4/нпс4_{i}.png') for i in range(0,9)]

class Npc1(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/домсп/нпс стойка.png')
        self.rect = self.image.get_rect(center=(x, y))


class Npc2(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/домсп/стол.png')
        self.rect = self.image.get_rect(center=(x, y))


class Npc3(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 2/нпс3/нпс3_8.png')
        self.rect = self.image.get_rect(center=(x, y))
    def anym(self):
        self.jump_time = pg.time.get_ticks()
        frame_duration = 300  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(Npc3_img)
        self.image = Npc3_img[frame_index]
    def update(self):
         self.anym()
class Npc4(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 2/нпс4/нпс4_8.png')
        self.rect = self.image.get_rect(center=(x, y))
    def anym(self):
        self.jump_time = pg.time.get_ticks()
        frame_duration = 100  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(Npc4_img)
        self.image = Npc4_img[frame_index]
    def update(self):
         self.anym()