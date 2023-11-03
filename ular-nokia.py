###
# Tanggal Dibuat: 11/10/2023
# Author: FandyFr
# APP Version: v1.5
###

from tkinter import font
import pygame as pg
from pygame import mixer as musik
from random import randrange
# Load Game
pg.init()
pg.font.init()
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

# Font
font = pg.font.Font(None, 36)

# Skor Game
skor = 0
skor_tertinggi = 0

# Nyawa di Dalam Game (Beta Version)
nyawa = 5 # Saya kasih 5 Nyawa

# Musik Di dalam Game
musik.init()
musik.music.load('suara/theme.wav')
musik.music.set_volume(0.2)
musik.music.play()

# Sound Effect di dalam Game
makan_suara = pg.mixer.Sound("suara/coins.mp3")
nyawa_suara = pg.mixer.Sound("suara/nyawa.mp3")
game_over_suara = pg.mixer.Sound("suara/game-over.mp3")

# System Reset Ketika Game Over
def reset_permainan():
    musik.music.play()
    global skor, nyawa
    skor = 0
    nyawa = 5  # Atur jumlah nyawa kembali ke nilai awal
    ular.center = posisi_random()
    makanan.center = posisi_random()
    panjang = 1
    segments = [ular.copy()]

# Tampilan Nyawa Pada Game
def tampilkan_nyawa():
    font = pg.font.Font(None, 36)
    nyawa_text = font.render(f"Nyawa: {nyawa}", True, (255, 255, 255))
    layar.blit(nyawa_text, (LAYAR - 150, 10))
    
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
    tampilkan_nyawa()
    skor_text = font.render(f"Skor: {skor}  Skor Tertinggi: {skor_tertinggi}", True, (255, 255, 255))
    font = pg.font.Font(None, 36)
    text_rect = skor_text.get_rect()
    text_rect.center = (LAYAR // 2, 26)
    layar.blit(skor_text, text_rect)
    
    # Ngecheck Makanan
    if ular.center == makanan.center:
        makan_suara.play()
        makanan.center = posisi_random()
        # Tambah Skor
        panjang += 1
        skor += 1
        if skor > skor_tertinggi:
            skor_tertinggi = skor
            
            
    # check apakah keluar dari border
    makan_sendiri = pg.Rect.collidelist(ular, segments[:-1]) != -1
    if ular.left < 0 or ular.right > LAYAR or ular.top < 0 or ular.bottom > LAYAR or makan_sendiri:
        musik.music.play()
        ular.center, makanan.center = posisi_random(), posisi_random()
        panjang, penempatan_ular = 1, (0, 0)
        segments = [ular.copy()]
        # Reset Skor
        skor = 0
        #  Nyawa Akan Berkurang
        nyawa -= 1
        nyawa_suara.play()
        if nyawa <= 0:
            layar.fill('black')
            # Suara Game Over dan Pause Tema lagu
            musik.music.pause()
            game_over_suara.play()
            # Akan Display Game Over
            font =  pg.font.Font(None, 72)
            game_over_text = font.render("Game Over !", True, (255, 0, 0))
            text_rect = game_over_text.get_rect()
            text_rect.center = (LAYAR // 2, LAYAR // 2)
            layar.blit(game_over_text, text_rect)
            pg.display.flip()
            skor_tertinggi = 0
            pg.time.wait(3000) # Menunggu 3 Detik
            reset_permainan()
            
        
    # Gambar Ular
    [pg.draw.rect(layar, 'green', segments) for segments in segments]
    # Gambar Makanannya
    pg.draw.rect(layar, 'red', makanan)
    
    # Pergerakan Ular
    waktu_sekarang = pg.time.get_ticks()
    if waktu_sekarang - waktu > step_waktu:
        waktu = waktu_sekarang
        ular.move_ip(penempatan_ular)
        segments.append(ular.copy())
        segments = segments[-panjang:]
    pg.display.flip()
    jam.tick(60)