import pygame
import random
import time

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_GALAXIA = (65, 107, 239)
ROXO_ESCURO = (72, 41, 83)
CINZA = (50, 50, 50)


# PARA O ARQUIVO 'main.py'
def botao_menu_rect(display, button_rect):

    # Fonte
    fonte = pygame.font.SysFont("comicsansms", 36)

    # botão de interação
    # pygame.draw.rect(surface, color, rect)
    mouse = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(display, BRANCO, button_rect)
    else:
        pygame.draw.rect(display, AZUL_GALAXIA, button_rect)

    # texto no botão
    text = fonte.render("JOGAR", True, PRETO)
    text_rect = text.get_rect(center=button_rect.center)
    display.blit(text, text_rect)


def icon():
    icon = pygame.image.load('imagens_png/icon.png')
    pygame.display.set_icon(icon)


def background_menu(display):
    imagem = pygame.image.load("imagens_png/Treinador de Reflexos Cósmico.png")
    display.blit(imagem, (35, -50))


def acerte_os_alvos_texto(display, fonte):
    jogo = pygame.Rect(800, 50, 0, 0)
    text = fonte.render("ACERTE O ALVO", True, BRANCO)
    text_rect = text.get_rect(center=jogo.center)
    display.blit(text, text_rect)


def acertos_e_vida(acertos, vidas, display):

    # acertos
    fonte = pygame.font.SysFont("comicsansms", 15)
    jogo = pygame.Rect(100, 10, 0, 0)
    text = fonte.render(f"ALVOS ACERTADOS: {acertos}", True, VERMELHO)
    text_rect = text.get_rect(center=jogo.center)
    display.blit(text, text_rect)

    # vidas
    text1 = fonte.render(f"VIDAS: {vidas}", True, AZUL)
    jogo2 = pygame.Rect(50, 30, 0, 0)
    text1_rect = text1.get_rect(center=jogo2.center)
    display.blit(text1, text1_rect)


def pontuacao_tela(display, score):

    fonte = pygame.font.SysFont("comicsansms", 15)
    jogo = pygame.Rect(800, 400, 0, 0)
    text = fonte.render(f"Pontuação máxima: {score:.0f}", True, VERMELHO)
    text_rect = text.get_rect(center=jogo.center)
    display.blit(text, text_rect)


def botao_voltar_menu(display, fonte, button_menu):

    # pygame.draw.rect(surface, color, rect)
    mouse = pygame.mouse.get_pos()
    if button_menu.collidepoint(mouse):
        pygame.draw.rect(display, AZUL, button_menu)
    else:
        pygame.draw.rect(display, VERMELHO, button_menu)

    # texto no botão
    text = fonte.render("Voltar para o menu", True, BRANCO)
    text_rect = text.get_rect(center=button_menu.center)
    display.blit(text, text_rect)


def alvo(display, circle_x, circle_y, raio_preto, cor, raio, raio_menor, raio_menor_ainda, raio_menor_menor_ainda):
    pygame.draw.circle(
        display, PRETO, (circle_x, circle_y), raio_preto)

    pygame.draw.circle(
        display, cor, (circle_x, circle_y), raio)

    pygame.draw.circle(
        display, AZUL, (circle_x, circle_y), raio_menor)

    pygame.draw.circle(
        display, VERMELHO, (circle_x, circle_y), raio_menor_ainda)

    pygame.draw.circle(
        display, BRANCO, (circle_x, circle_y), raio_menor_menor_ainda)


def background_jogo(display):
    imagem = pygame.image.load('imagens_png/background_jogo.png')
    display.blit(imagem, (35, -50))


def tabela_de_pontuacao(display, tabela_caixa, pontuacao_tabela):

    fonte = pygame.font.SysFont("comicsansms", 15)

    pygame.draw.rect(display, BRANCO, tabela_caixa)

    # TEXTO
    rect_texto = pygame.Rect(1300, 6, 215, 33)
    pygame.draw.rect(display, BRANCO, rect_texto)
    text = fonte.render('PONTUAÇÃO', True, PRETO)
    text_tabela = text.get_rect(center=rect_texto.center)
    display.blit(text, text_tabela)

    # --------ARRUMAR O CASO DE NUMEROS INFINITOS NA TABELA------
    for i, numero in enumerate(pontuacao_tabela):
        texto = fonte.render((f'{numero:.0f}'), True, PRETO)
        texto_rect = texto.get_rect(
            topleft=(tabela_caixa.left + 20, tabela_caixa.top + 10 + i * 20))
        display.blit(texto, texto_rect)
