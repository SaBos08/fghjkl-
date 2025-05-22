import pygame as pg


class Lab(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(f'спрайты/гг диалог 1/лабсп/стена4.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 0

'''
for i in range(1, 6):
    class Lab(pg.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pg.image.load(f'спрайты/гг диалог 1/лабсп/стена{0}.png')
            self.rect = self.image.get_rect(center=(x, y))
for i in range(1, 59):
    wall = walls(750, 400)
    



'''