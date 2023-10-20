###
# Tanggal Dibuat: 11/10/2023
# Author: FandyFr
# APP Version: v1.5
###

import pygame as pg
from pygame import mixer as musik
from random import randrange
# Load Game
pg.init()
# Settings Game & In - Game
LAYAR = 1000
pg.display.set_caption('Game Ular Nokia by Fandy Fathurrohman')
UKURAN_PANJANG = 50
JANGKAUAN = (UKURAN_PANJANG // 2, LAYAR - UKURAN_PANJANG // 2, UKURAN_PANJANG)
posisi_random = lambda: [randrange(*JANGKAUAN), randrange(*JANGKAUAN)]
arah = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
ular = pg.rect.Rect([0, 0, UKURAN_PANJANG - 2, UKURAN_PANJANG -2])
ular.center = posisi_random()
penempatan_ular = (0, 0)
makanan = ular.copy()
makanan.center = posisi_random()
panjang = 1
segments = [ular.copy()]
waktu, step_waktu = 0, 110
layar = pg.display.set_mode([LAYAR] * 2)
jam = pg.time.Clock()
keluar = exit

# Skor Game
skor = 0
skor_tertinggi = 0

# Musik Di dalam Game (ALPHA VERSION)
musik.init()
musik.music.load('musik/idol.wav')
musik.music.play()


# Pengkodean Pakai Bahasa Campuran Indonesia & Inggris
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keluar()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and arah[pg.K_w]:
                penempatan_ular = (0, -UKURAN_PANJANG)
                arah = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and arah[pg.K_s]:
                penempatan_ular = (0, UKURAN_PANJANG)
                arah = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and arah[pg.K_a]:
                penempatan_ular = (-UKURAN_PANJANG, 0)
                arah = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and arah[pg.K_d]:
                penempatan_ular = (UKURAN_PANJANG, 0)
                arah = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
            
    layar.fill('black')
    """ # Pen
    pen = turtle.Turtle()
    pen.write("Skor: {}  Skor tertinggi: {}".format(skor, skor_tertinggi), align="center", font=("Courier", 24, "normal")) """
    
    # Ngecheck Makanan
    if ular.center == makanan.center:
        makanan.center = posisi_random()
        panjang += 1
        skor += 10
    # check apakah keluar dari border
    makan_sendiri = pg.Rect.collidelist(ular, segments[:-1]) != -1
    if ular.left < 0 or ular.right > LAYAR or ular.top < 0 or ular.bottom > LAYAR or makan_sendiri:
        ular.center, makanan.center = posisi_random(), posisi_random()
        panjang, penempatan_ular = 1, (0, 0)
        segments = [ular.copy()]
        """ pen.clear() """
        skor = 0
        
    # Gambar Ular
    [pg.draw.rect(layar, 'green', segments) for segments in segments]
    # Gambar Makanannya
    pg.draw.rect(layar, 'red', makanan)
    # Reset Skor
    """ pen.clear()
    pen.write("Skor: {}  Skor tertinggi: {}".format(skor, skor_tertinggi), align="center", font=("Courier", 24, "normal")) """
    
    # Pergerakan Ular
    waktu_sekarang = pg.time.get_ticks()
    if waktu_sekarang - waktu > step_waktu:
        waktu = waktu_sekarang
        ular.move_ip(penempatan_ular)
        segments.append(ular.copy())
        segments = segments[-panjang:]
    pg.display.flip()
    jam.tick(60)