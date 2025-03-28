import pygame # type: ignore
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Largura e altura da tela
largura_tela = 600
altura_tela = 400

# Criando a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobra')

# Definindo o relógio para controlar o FPS
clock = pygame.time.Clock()

# Tamanho da cobra e a velocidade
tamanho_cobra = 10
velocidade_cobra = 15

# Função para desenhar a cobra
def desenhar_cobra(tamanho_cobra, lista_corpo_cobra):
    for segmento in lista_corpo_cobra:
        pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_cobra, tamanho_cobra])

# Função para exibir a pontuação
def nossa_pontuacao(pontos):
    fonte = pygame.font.SysFont("bahnschrift", 25)
    texto = fonte.render("Pontuação: " + str(pontos), True, preto)
    tela.blit(texto, [0, 0])

# Função principal do jogo
def jogo():
    fim_de_jogo = False
    jogo_em_andamento = True

    # Posições iniciais da cobra
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    # Movimento da cobra
    x_cobra_mudar = 0
    y_cobra_mudar = 0

    # Lista para armazenar o corpo da cobra
    corpo_cobra = []
    comprimento_cobra = 1

    # Posições da comida
    x_comida = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
    y_comida = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0

    # Pontuação
    pontos = 0

    # Loop do jogo
    while jogo_em_andamento:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_em_andamento = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_cobra_mudar = -tamanho_cobra
                    y_cobra_mudar = 0
                elif event.key == pygame.K_RIGHT:
                    x_cobra_mudar = tamanho_cobra
                    y_cobra_mudar = 0
                elif event.key == pygame.K_UP:
                    y_cobra_mudar = -tamanho_cobra
                    x_cobra_mudar = 0
                elif event.key == pygame.K_DOWN:
                    y_cobra_mudar = tamanho_cobra
                    x_cobra_mudar = 0

        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            fim_de_jogo = True

        x_cobra += x_cobra_mudar
        y_cobra += y_cobra_mudar
        tela.fill(azul)

        pygame.draw.rect(tela, vermelho, [x_comida, y_comida, tamanho_cobra, tamanho_cobra])
        lista_cabeca_cobra = []
        lista_cabeca_cobra.append(x_cobra)
        lista_cabeca_cobra.append(y_cobra)
        corpo_cobra.append(lista_cabeca_cobra)

        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == lista_cabeca_cobra:
                fim_de_jogo = True

        desenhar_cobra(tamanho_cobra, corpo_cobra)
        nossa_pontuacao(pontos)

        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
            y_comida = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1
            pontos += 1

        clock.tick(velocidade_cobra)

    # Quando o jogo termina
    while fim_de_jogo:
        tela.fill(branco)
        fonte = pygame.font.SysFont("bahnschrift", 35)
        mensagem = fonte.render("Fim de Jogo! Pressione C para jogar novamente ou Q para sair", True, vermelho)
        tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
        nossa_pontuacao(pontos)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    fim_de_jogo = False
                    jogo_em_andamento = False
                if event.key == pygame.K_c:
                    jogo()

    pygame.quit()

# Iniciar o jogo
jogo()
