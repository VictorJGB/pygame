import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

LARGURA = 640
ALTURA = 480

vel_y = 10  

rect_vermelho_x = LARGURA
rect_verde_y = ALTURA - 80

pos_chao = ALTURA - 80

pulo = False

vida = 3
pontos = 1
fonte = pygame.font.SysFont('comicsansms', 40, bold=True, italic=False)#VARIÁVEL COM O TIPO DE FONTE

musica_fundo = pygame.mixer.music.load('Github_Pygame\sons\BoxCat Games - Epic Song.mp3')
pygame.mixer.music.play(-1)

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Jogo Horizontal")

while True:
    relogio.tick(50)#FPS
    tela.fill((255,255,255))#PREENCHENDO A COR DA TELA

    #MENSAGENS DA TELA
    mensg_vida = f'VIDA: {vida}'
    mensg_pontos = f'PONTOS: {pontos}'
    texto_vida = fonte.render(mensg_vida, True, (255,0,0))
    texto_pontos = fonte.render(mensg_pontos, True, (255,0,0))

    rect_verde = pygame.draw.rect(tela, (0,255,0), (40, rect_verde_y, 40, 50))
    rect_vermelho = pygame.draw.rect(tela, (255,0,0), (rect_vermelho_x, pos_chao, 40, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #CHECANDO SE O PERSONAGEM ESTÁ COM 0 DE VIDA
    if vida <= 0:
            pygame.quit()

    #VARIÁVEL QUE RECEBE O COMANDO DE TECLA PRESSIONADA
    tecla_pressionada = pygame.key.get_pressed()

    #AÇÃO DO PULO  
    if pulo is False and tecla_pressionada[pygame.K_SPACE]:
        pulo = True
    if pulo is True:
        rect_verde_y -= vel_y*3
        vel_y -= 1
        if vel_y < -10:
            pulo = False
            vel_y = 10

    #MOVIMENTO DO RETÂNGULO VERMELHO DA DIREITA PRA ESQUERDA
    rect_vermelho_x -= 10

    if rect_vermelho_x < 0:
        rect_vermelho_x = LARGURA

    #COLISÃO ENTRE OS RETÂNGULOS VERDE E VERMELHO
    if rect_vermelho.colliderect(rect_verde):
            rect_vermelho_x = 640
            vida -= 1
    else:
        pontos += 1
    
    if pontos == 400:
        pygame.quit()

    tela.blit(texto_vida, (20,60))
    tela.blit(texto_pontos, (20,120))
    pygame.display.update()