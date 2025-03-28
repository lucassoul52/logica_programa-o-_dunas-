import pygame # type: ignore
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definindo as dimensões da tela
LARGURA_TELA = 600
ALTURA_TELA = 400

# Tamanho das raquetes e da bola
RAQUETE_LARGURA = 15
RAQUETE_ALTURA = 100
BOLA_TAMANHO = 15

# Velocidade da bola
velocidade_bola_x = 7
velocidade_bola_y = 7

# Inicializando a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong - Jogue contra a IA")

# Função para desenhar as raquetes
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, BRANCO, [x, y, RAQUETE_LARGURA, RAQUETE_ALTURA])

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.rect(tela, BRANCO, [x, y, BOLA_TAMANHO, BOLA_TAMANHO])

# Função para exibir a pontuação
def exibir_pontuacao(pontos_1, pontos_2):
    fonte = pygame.font.SysFont("arial", 30)
    texto = fonte.render(f"{pontos_1} - {pontos_2}", True, BRANCO)
    tela.blit(texto, [LARGURA_TELA // 2 - texto.get_width() // 2, 20])

# Função principal do jogo
def jogo():
    global velocidade_bola_x, velocidade_bola_y  # Declaração das variáveis globais

    # Posições iniciais
    x_raquete1 = 20
    y_raquete1 = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2
    x_raquete2 = LARGURA_TELA - 20 - RAQUETE_LARGURA
    y_raquete2 = ALTURA_TELA // 2 - RAQUETE_ALTURA // 2
    x_bola = LARGURA_TELA // 2 - BOLA_TAMANHO // 2
    y_bola = ALTURA_TELA // 2 - BOLA_TAMANHO // 2

    # Velocidade da raquete
    velocidade_raquete1 = 0
    velocidade_raquete2 = 0

    # Pontuação
    pontos_1 = 0
    pontos_2 = 0

    # Controlando o loop do jogo
    jogo_em_andamento = True
    while jogo_em_andamento:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_em_andamento = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    velocidade_raquete1 = -10
                if event.key == pygame.K_s:
                    velocidade_raquete1 = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    velocidade_raquete1 = 0

        # Movimentação da raquete do jogador
        y_raquete1 += velocidade_raquete1

        # Movimentação da raquete da IA
        if y_raquete2 + RAQUETE_ALTURA / 2 < y_bola + BOLA_TAMANHO / 2:
            velocidade_raquete2 = 7
        elif y_raquete2 + RAQUETE_ALTURA / 2 > y_bola + BOLA_TAMANHO / 2:
            velocidade_raquete2 = -7
        else:
            velocidade_raquete2 = 0

        y_raquete2 += velocidade_raquete2

        # Garantindo que as raquetes não saiam da tela
        if y_raquete1 < 0:
            y_raquete1 = 0
        if y_raquete1 > ALTURA_TELA - RAQUETE_ALTURA:
            y_raquete1 = ALTURA_TELA - RAQUETE_ALTURA
        if y_raquete2 < 0:
            y_raquete2 = 0
        if y_raquete2 > ALTURA_TELA - RAQUETE_ALTURA:
            y_raquete2 = ALTURA_TELA - RAQUETE_ALTURA

        # Movimentação da bola
        x_bola += velocidade_bola_x
        y_bola += velocidade_bola_y

        # Colisão com o topo e a parte inferior
        if y_bola <= 0 or y_bola >= ALTURA_TELA - BOLA_TAMANHO:
            velocidade_bola_y = -velocidade_bola_y

        # Colisão com as raquetes
        if x_bola <= x_raquete1 + RAQUETE_LARGURA and y_bola + BOLA_TAMANHO >= y_raquete1 and y_bola <= y_raquete1 + RAQUETE_ALTURA:
            velocidade_bola_x = -velocidade_bola_x
        if x_bola >= x_raquete2 - BOLA_TAMANHO and y_bola + BOLA_TAMANHO >= y_raquete2 and y_bola <= y_raquete2 + RAQUETE_ALTURA:
            velocidade_bola_x = -velocidade_bola_x

        # Verificando se a bola saiu da tela (pontos)
        if x_bola <= 0:
            pontos_2 += 1
            x_bola = LARGURA_TELA // 2 - BOLA_TAMANHO // 2
            y_bola = ALTURA_TELA // 2 - BOLA_TAMANHO // 2
            velocidade_bola_x = -velocidade_bola_x

        if x_bola >= LARGURA_TELA - BOLA_TAMANHO:
            pontos_1 += 1
            x_bola = LARGURA_TELA // 2 - BOLA_TAMANHO // 2
            y_bola = ALTURA_TELA // 2 - BOLA_TAMANHO // 2
            velocidade_bola_x = -velocidade_bola_x

        # Atualizando a tela
        tela.fill(PRETO)
        desenhar_raquete(x_raquete1, y_raquete1)
        desenhar_raquete(x_raquete2, y_raquete2)
        desenhar_bola(x_bola, y_bola)
        exibir_pontuacao(pontos_1, pontos_2)

        pygame.display.update()

        # Controlando o FPS
        pygame.time.Clock().tick(60)

    pygame.quit()

# Iniciando o jogo
jogo()
