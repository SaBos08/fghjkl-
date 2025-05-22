import random

import pygame as pg
from player import Player
from npc import Npc1, Npc2 , Npc3, Npc4
from lab import Lab
from Def import Background4,Unit

pg.init()
pg.font.init()
pg.mixer.init()

W = 1500
H = 800
room = 0
font = pg.font.Font('спрайты/шрифт.ttf', 32)

keys = pg.key.get_pressed()
pil = pg.image.load
pss = pg.surface.Surface

img = 'спрайты/гг диалог 2/фонКомнаты4/фон2-1.png.png'
background4_lst = [pg.image.load(f'спрайты/гг диалог 2/фонКомнаты4/фон{i}-1.png.png') for i in range(0, 5)]

'''jump_time = pg.time.get_ticks()
frame_duration = 450  # Задержка между кадрами в миллисекундах
current_time = pg.time.get_ticks()
frame_index = (current_time // frame_duration) % len(background4_lst)
image = background4_lst[frame_index]'''

background4_img = pil(img)
background4 = pss((1500, 800))

sound_door = pg.mixer.Sound('спрайты/гг диалог 1/домсп/открытие двери.mp3')

labf_img = pil('спрайты/гг диалог 1/лабсп/фон лабиринта.png')
labf = pss((1500, 800))

tropa_img = pil('спрайты/гг диалог 1/босссп/тропа.png')
tropa = pss((1500, 800))

home_img = pil('спрайты/гг диалог 1/домсп/дом.png')
home = pss((1500, 800))

clock = pg.time.Clock()

bg_img = pil('спрайты/гг диалог 1/фон.png')
bg = pss((1500, 800))

homi_img = pil('спрайты/гг диалог 1/домсп/дом внутри.png')
home_inside = pss((1500, 800))

player = Player(1470, 650)
npc1 = Npc1(950, 620)
npc2 = Npc2(300, 650)
npc3 = Npc3(200,300)
npc4 = Npc4(700,500)
lab = Lab(750, 400)
all_sprite = pg.sprite.Group(player)
screen = pg.display.set_mode((W, H))


pr = player.rect

room = 4

def upd():
    if player.rect.bottom > 815:
        player.rect.bottom = 815
    if player.rect.top < 0:
        player.rect.top = 0
    if player.rect.left < -15:
        player.rect.left = -15
    if player.rect.right > 1535:
        player.rect.right = 1535
    clock.tick(60)
    all_sprite.draw(screen)
    all_sprite.update()
    pg.display.update()

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if room == 0:

        all_sprite = pg.sprite.Group(player)
        bg.blit(bg_img, (0, 0))
        screen.blit(bg, (0, 0))
        home.blit(home_img, (110, -120))
        screen.blit(home_img, (110, -120))
        if player.rect.top < 400:
            player.rect.top = 400

        if player.rect.right >= 1530:
            room = 2

        if 600 <= player.rect.x <= 650 and 480 <= player.rect.y <= 550:
            room = 1
            player.rect.x = 965
            player.rect.y = 610
            sound_door.play()

        upd()

    if room == 1:

        if pr.top < 600:
            pr.top = 600
        if 100 < pr.x < 386 and pr.y == 690:
            pr.y = 690

        if 1000 < player.rect.x < 1100 and player.rect.y == 600:
            room = 0
            player.rect.x = 665
            player.rect.y = 570
            sound_door.play()


        pg.draw.rect(homi_img, 'brown', (415, 645, 10, 10))
        pg.draw.rect(homi_img, 'brown', (980, 645, 45, 7))
        home_inside.blit(homi_img, (0, 0))
        screen.blit(home_inside, (0, 0))
        all_sprite = pg.sprite.Group(npc1, npc2, player)

        if pr.x < 384 and 592 < pr.y < 690:
            pr.x = 384
            text = font.render(f'f"шутейка"', False, 'white', 'black')
            screen.blit(text, (50, 500))

        upd()

    if room == 2:

        labf.blit(labf_img, (0, 0))
        screen.blit(labf, (0, 0))
        all_sprite = pg.sprite.Group(lab, player)

        upd()

    if room == 3:   #грибы с триггером босса

        player.rect.x = 637
        player.rect.y = 740

        tropa.blit(tropa_img, (0, 0))
        screen.blit(tropa, (0, 0))

        if player.rect.left < 569:
            player.rect.left = 569
        if player.rect.right > 805:
            player.rect.right = 805
        if player.rect.top < 425:
            player.rect.top = 425
    if room == 4:
        anym_background = random.randint(0,4)
        img = f'спрайты/гг диалог 2/фонКомнаты4/фон{anym_background}-1.png.png'
        background4_img = pil(img)

        background4.blit(background4_img, (0,0))
        screen.blit(background4_img, (0,0))



        if player.rect.x < 428 and player.rect.y < 450 and player.rect.x > 15 and player.rect.y > 74:
            text = font.render(f'Хм… что Знания шлемы GFCGJHN. ваших Жителей',False, 'white', 'black')
            text1 = font.render(f' Практически всё, вам d cj,fxm',False, 'white', 'black')
            text2 = font.render (f' нужно. этой книги Клинки, ntktgjhnbhetnmcz',False, 'white', 'black')
            text3 = font.render(f'.наделяют Cke;,e силой! ОреаРСФ',False, 'white', 'black')
            screen.blit(text, (50, 522))
            screen.blit(text1, (50, 548))
            screen.blit(text2, (50, 580))
            screen.blit(text3, (50, 612))


        if player.rect.x < 764 and player.rect.y < 586 and player.rect.x > 508 and player.rect.y > 364:
            text = font.render(f'Символ яме и убирал B dc`;tt и что,', False, 'white', 'black')
            text1 = font.render(f' которого за выгребной и как, Короля правителя ', False, 'white', 'black')
            text2 = font.render(f'На этой бога неделе я так y почитали  ', False, 'white', 'black')
            text3 = font.render(f'kexitt vtcnj/, чувствую Халлоунеста так, будто ', False, 'white', 'black')
            text4 = font.render(f'работаю в больным. ‘nj lfktrj себя как', False, 'white', 'black')
            screen.blit(text, (50, 522))
            screen.blit(text1, (50, 548))
            screen.blit(text2, (50, 580))
            screen.blit(text3, (50, 612))
            screen.blit(text4, (50, 640))

        all_sprite =pg.sprite.Group(npc4,npc3, player)
        upd()

        if player.rect.x < 418 and player.rect.y < 440 and player.rect.x > 30 and player.rect.y > 94:
            keys = pg.key.get_pressed()
            if keys[pg.K_w] or keys[pg.KSCAN_W]:

                player.rect.y -= player.vector
                player.rect.y -= player.vector

            if keys[pg.K_a] or keys[pg.KSCAN_A]:

                player.rect.x -= player.vector
                player.rect.x -= player.vector

            if keys[pg.K_s] or keys[pg.KSCAN_S]:

                player.rect.y += player.vector
                player.rect.y += player.vector

            if keys[pg.K_d] or keys[pg.KSCAN_D]:

                player.rect.x += player.vector
                player.rect.x += player.vector

        if player.rect.x < 744 and player.rect.y < 566 and player.rect.x > 538 and player.rect.y > 384:
            keys = pg.key.get_pressed()

            if keys[pg.K_w] or keys[pg.KSCAN_W]:

                player.rect.y -= player.vector
                player.rect.y -= player.vector

            if keys[pg.K_a] or keys[pg.KSCAN_A]:

                player.rect.x -= player.vector
                player.rect.x -= player.vector

            if keys[pg.K_s] or keys[pg.KSCAN_S]:

                player.rect.y += player.vector
                player.rect.y += player.vector

            if keys[pg.K_d] or keys[pg.KSCAN_D]:

                player.rect.x += player.vector
                player.rect.x += player.vector

pg.quit()