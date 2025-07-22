'''
1 - Menu princial
        criar 
        - um menu com o nome do jogo
        - um botão de começar que levará para a parte do jogo 
        - colocar um musica de fundo (tema do star wars)

2 - Jogo
        criar:
            - um sistema random que faça o alvo aparecer em locais aleatorios da tela
            - um sistema que limite o tempo que o alvo fique na tela
            - um sistema para limitar o espaço em que os alvos parecera
        colocar:
            - musica tema (pré feito, mas com bugs)
            - efeitos de acerto e erro dos alvos

3 - placar
        usar:
            - usar o time.time() para medir o tempo decorrido em cada alvo, ou time.perf_counter().
'''


'''
#RELATORIO DA ULTIMA ATUALIZAÇÃO DO REFLEX TRAINER
07/05/25
-Tentei fazer o sistema de randomização do circulo e funcionou e também consegui delimitar o
espaço de randomização, agora só falta delimitar o tempo que um alvo fica na tela e
fazer ele detectar o click e sumir o alvo.
-resolver bug da def musica_in_game()

10/05/25
-Consegui fazer o circulo mudar depois de alguns segundos, podendo personalizar a vontade o tempo.
-Preciso fazer um jeito de sumir e aparecer um local aleatório da tela depois do mouse ter acertado
o alvo.

20/05/25
-
'''


'''
[]JOGO
    []MENU PRINCIPAL
        []BOTÃO PARA IR PARA O JOGO
        []CONFIGURAÇÕES

    []GAMEPLAY
        []ALVOS
            []RANDOMIZAR ALVOS
            []TEMPORIZAR OS ALVOS
            []DIFICULDADE DINÂMICA
            []CONTADOR DE VIDAS
            []CONTADOR DE ACERTOS

    []TELA PONTUAÇÃO (GAME OVER)
        []PONTUAÇÃO
        []BOTÃO PARA VOLTAR PARA O MENU PRINCIPAL
        []BOTÃO PARA JOGAR NOVAMENTE
    []PONTO DE SALVAMENTO DE PONTUAÇÃO(OPCIONAL)

'''

import math
import sys
import time
import pygame
import random
from imagens.imagens import botao_menu_rect, acerte_os_alvos_texto, icon, background_menu, acertos_e_vida, pontuacao_tela, botao_voltar_menu, alvo, background_jogo, tabela_de_pontuacao
from sons.sounds import tiro_som, som_troca_dificuldade, som_tela_pontuacao, som_erro_tiro, music_in_game, music_menu
# from tela_jogo import jogo

# TAMANHO DA TELA
LARGURA = 1600
ALTURA = 900


# ----------------CORES------------------#
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_GALAXIA = (65, 107, 239)
ROXO_ESCURO = (72, 41, 83)
CINZA = (50, 50, 50)


# TIMERS
tempo_troca_de_alvo = 2.5
tempo_de_duracao_circulo = 4.5
tela_pontuacao = 0

# ACERTOS
acertos = 0

# dificuldade
medio = True
hard = True

# VIDAS
vidas = 3

# PONTUAÇÃO
score = 0

# TELA
tela = 0

# CONTADOR FOR
contador = 0


# INICIAR O PYGAME
pygame.init()


# CRIA UMA JANELA
display = pygame.display.set_mode([LARGURA, ALTURA])


# AJUDA A CRIAR UMA TAXA DE QUADROS
clock = pygame.time.Clock()


# listas
circulos = []
acertos_tempo = []
pontuacao = []
pontuacao_tabela = []

# nome do jogo
nome = pygame.display.set_caption('Treino de Reflexo')

# Fonte
fonte = pygame.font.SysFont("comicsansms", 25)

# botões
button_rect = pygame.Rect(600, 730, 320, 90)
button_menu = pygame.Rect(660, 500, 300, 50)

# formas
tabela_caixa = pygame.Rect(1300, 62, 215, 550)


# icon
icon()
music_menu()
background_menu(display)
botao_menu_rect(display, button_rect)


# 1 - LOOPING PRINCIPAL
gameloop = True
isPressingW = False
isPressingMouse = False
mostrar_circulo = True


while gameloop:
    # parte 2 para a janela não fechar instantâniamente
    if tela == 0:
        tela += 1
    if tela == 1:
        tela_atual = 'menu'
    elif tela == 2:
        tela_atual = 'jogo'
    elif tela == 3:
        tela_atual = 'pontuação'

    # events
    for event in pygame.event.get():
        if gameloop == True:
            # fechar o programa no 'X'
            if event.type == pygame.QUIT:
                gameloop = False
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if tela_atual == 'menu':
                background_menu(display)

                if button_rect.collidepoint(mouse_pos):
                    tela = 2
                    music_in_game()

            # syntax de acerto no alvo (onde ficava)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            qt_circulos = sum(1 for circu in circulos if len(circu))

            for c in circulos:
                circle_x, circle_y, raio_preto, raio, raio_menor, raio_menor_ainda, raio_menor_ainda, cor, pika = c
                # calculo de distância de pontos
                contador += 1
                acerto = ((mouse_x - circle_x)**2 +
                          (mouse_y - circle_y)**2)**0.5

                if acerto <= raio:
                    acertos += 1
                    circulos.remove(c)

                    tiro_som()

                # calculo de pontuação
                    sumico_circulo = time.time()
                    cal = sumico_circulo - finalizacao
                    acertos_tempo.append(cal)
                    soma_lista = sum(acertos_tempo)
                    score = ((soma_lista * acertos)*100)**2

            # sistema de dificuldade progressiva
                if acertos < 5:
                    tempo_troca_de_alvo = 1.5
                    tempo_de_duracao_circulo = 3.5
                    score = ((soma_lista * acertos)*50)**2  # score facil
                    if acerto > raio:
                        circulos.remove(c)
                        som_erro_tiro()
                        if qt_circulos == 1:
                            vidas -= 1
                        else:
                            vidas -= 1

                if acertos == 5:
                    som_troca_dificuldade()

                if acertos >= 5:
                    tempo_troca_de_alvo = 1
                    tempo_de_duracao_circulo = 2

                    # score medio e dificil
                    score = ((soma_lista * acertos)*100)**2
                    if acerto > raio:
                        som_erro_tiro()
                        circulos.remove(c)
                        if qt_circulos == 1:
                            vidas -= 1
                        if qt_circulos == 2:
                            vidas -= 1

                if acertos == 20:
                    som_troca_dificuldade()

                if acertos >= 20:
                    tempo_troca_de_alvo = 0.5

                if vidas <= 0:
                    tela = 3

            if contador == 1:
                contador = 0

            # posição de click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Posição do click: ', mouse_pos)
                print(pontuacao_tabela)

    # diz qual o botão que deve clicar para sair do menu
    if tela_atual == 'menu':
        botao_menu_rect(display, button_rect)

        tabela_de_pontuacao(display, tabela_caixa, pontuacao_tabela)
        inicializacao = time.time()
    # tela de jogo

    if tela_atual == 'jogo':
        finalizacao = time.time()
        display.fill(CINZA)
        background_jogo(display)
        acerte_os_alvos_texto(display, fonte)
        acertos_e_vida(acertos, vidas, display)

    # ----------------------------------ALVO--------------------------------------------------#
    # termina a contagem de tempo para o alvo sumir
    # usar o tempo surgimento do alvo menos o tempo de desaparecimento
    # para manter ele na tela

        if finalizacao - inicializacao >= tempo_troca_de_alvo:
            circle_x = random.randint(40, LARGURA - 200)
            circle_y = random.randint(45, ALTURA - 100)

            raio_preto = 45
            raio = 40
            raio_menor = 30
            raio_menor_ainda = 20
            raio_menor_menor_ainda = 10
            cor = 255, 0, 0
            circulos.append((circle_x, circle_y, raio_preto, raio, raio_menor,
                            raio_menor_ainda, raio_menor_ainda, cor, finalizacao))
            inicializacao = finalizacao

        # método de filtragem de lista, que permite que um item da lista se mantenha nela até que o tempo de vida dela ultrapasse o tempo_de_duracao_circulo
        circulos = [c for c in circulos if finalizacao -
                    c[8] < tempo_de_duracao_circulo]
        for circle_x, circle_y, raio_preto, raio, raio_menor, raio_menor_ainda, raio_menor_ainda, cor, _ in circulos:

            alvo(display, circle_x, circle_y, raio_preto, cor, raio,
                 raio_menor, raio_menor_ainda, raio_menor_menor_ainda)

    if tela_atual == 'pontuação':
        tela_pontuacao += 1
        if tela_pontuacao <= 1:  # --> faz com que rode apenas uma vez
            som_tela_pontuacao()
            pontuacao_tabela.append(score)

        if len(pontuacao_tabela) > 15:
            pontuacao_tabela = pontuacao_tabela[-15:]
        display.fill(BRANCO)
        acerte_os_alvos_texto(display, fonte)
        acertos_e_vida(acertos, vidas, display)
        pontuacao_tela(display, score)
        botao_voltar_menu(display, fonte, button_menu)
        vidas = 3
        acertos = 0

        if button_menu.collidepoint(mouse_pos):

            background_menu(display)
            tela = 1
            music_menu()
            tela_pontuacao = 0
        # calculo criar uma área de acerto para o alvo

        # jogo(display, mostrar_circulo, inicializacao)


# atualiza o pygame
    pygame.display.flip()
    clock.tick(60)


# fecha o pygame
pygame.quit()
pygame.mixer.quit()
sys.exit()


# chama a função main para que ela execute se ela for true
