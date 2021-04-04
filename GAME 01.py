import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = int(largura / 2)
y = int(altura / 2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

musica_fundo = pygame.mixer.music.load('Github_pygame\sons\BoxCat Games - Epic Song.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

som_colisao = pygame.mixer.Sound('Github_pygame\sons\smw_coin.wav')
som_colisao.set_volume(1.0)

pontos = 0
fonte = pygame.font.SysFont("arial", 40, True, True)#(FONTE, TAMANHO, NEGRITO, ITALICO)

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

#Código principal do Game
while True:
    relogio.tick(30)#Controle de FPS
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    text0_formatado = fonte.render(mensagem, True, (255,255,255))#(MENSAGEM, SERRILHAMENTO, COR)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            elif event.key == K_d:
                x += 20
            elif event.key == K_s:
                y += 20
            elif event.key == K_w:
                y -= 20
        '''
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    elif pygame.key.get_pressed()[K_d]:
        x += 20
    elif pygame.key.get_pressed()[K_s]:
        y += 20
    elif pygame.key.get_pressed()[K_w]:
        y -= 20

    #Desenhando os objetos
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela ,(0,0,255), (x_azul,y_azul,40,50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        som_colisao.play()

    tela.blit(text0_formatado, (450, 40))#(TEXTO, POSIÇÃO(x,y)) MOSTRANDO TEXTO NA TELA
    pygame.display.update()