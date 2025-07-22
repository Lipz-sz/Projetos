import pygame
import time



def music_menu():
    # inicializador da música
    pygame.mixer.init()
    menu_music = pygame.mixer.music.load('sons_wav/musica tema menu (online-audio-converter.com).wav'
        )
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

def music_in_game():
    pygame.mixer.init()
    music_game = pygame.mixer.music.load("sons_wav/04.-Crystals.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(10)

def tiro_som():
    blaster_sound = pygame.mixer.Sound('sons_wav/blaster.wav')
    blaster_sound.play()
    blaster_sound.set_volume(0.5)

def som_troca_dificuldade():
    troca_dificuldade = pygame.mixer.Sound('sons_wav/som_troca_dificuldade.wav')
    troca_dificuldade.play()
    troca_dificuldade.set_volume(0.5)

def som_tela_pontuacao():
    tela_pontuacao = pygame.mixer.Sound('sons_wav/som_tabela_pontuacao.wav')
    tela_pontuacao.play()
    tela_pontuacao.set_volume(0.5)

def som_erro_tiro():
    erro_tiro = pygame.mixer.Sound('sons_wav/erro-win-7.wav')
    erro_tiro.play()
    erro_tiro.set_volume(2)