import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Jogo')

#Código principal do Game
while True:
    relogio.tick(60)#Controle de FPS
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            elif event.key == K_d:
                x += 20
            elif event.key == K_s:
                y += 20
            elif event.key == K_w:
                y -= 20
    #Desenhando os objetos
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))


    pygame.display.update()