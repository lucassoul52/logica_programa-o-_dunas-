import pygame # type: ignore
import random

# Inicialização do Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (169, 169, 169)

# Tamanho da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Corrida 2D")

# Parâmetros do carro
carro_width = 50
carro_height = 100
carro_x = LARGURA_TELA // 2 - carro_width // 2
carro_y = ALTURA_TELA - carro_height - 20
carro_velocidade = 10

# Obstáculos - Definindo como variável global
obstaculos = []

# Parâmetros do obstáculo
obstaculo_width = 50
obstaculo_height = 50
obstaculo_velocidade = 5  # Variável global de velocidade do obstáculo

# Configuração do relógio
clock = pygame.time.Clock()

# Função para desenhar o carro
def desenhar_carro(x, y):
    pygame.draw.rect(tela, AZUL, (x, y, carro_width, carro_height))

# Função para desenhar os obstáculos
def desenhar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, VERDE, (obstaculo[0], obstaculo[1], obstaculo_width, obstaculo_height))

# Função para criar novos obstáculos
def gerar_obstaculo():
    x = random.randint(0, LARGURA_TELA - obstaculo_width)
    y = -obstaculo_height
    return [x, y]

# Função de colisão
def colisao(car_x, car_y, obstaculos):
    for obstaculo in obstaculos:
        if car_x < obstaculo[0] + obstaculo_width and car_x + carro_width > obstaculo[0]:
            if car_y < obstaculo[1] + obstaculo_height and car_y + carro_height > obstaculo[1]:
                return True
    return False

# Função principal do jogo
def jogo():
    global carro_x, carro_y, obstaculos, obstaculo_velocidade  # Tornando obstaculos e obstaculo_velocidade globais

    obstaculos.clear()  # Agora funciona corretamente
    distancia = 0
    run = True

    while run:
        clock.tick(60)  # FPS (frames por segundo)
        
        # Checando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Movimentação do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and carro_x > 0:
            carro_x -= carro_velocidade
        if keys[pygame.K_RIGHT] and carro_x < LARGURA_TELA - carro_width:
            carro_x += carro_velocidade
        
        # Atualizando obstáculos
        for obstaculo in obstaculos:
            obstaculo[1] += obstaculo_velocidade

        # Remover obstáculos que saíram da tela
        obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo[1] < ALTURA_TELA]
        
        # Gerar novos obstáculos aleatórios
        if random.randint(1, 100) <= 3:
            obstaculos.append(gerar_obstaculo())

        # Verificar colisões
        if colisao(carro_x, carro_y, obstaculos):
            run = False  # Finaliza o jogo se houve colisão

        # Aumentar pontuação e dificuldade
        distancia += 1
        if distancia % 100 == 0:  # Aumenta a velocidade a cada 100 metros
            obstaculo_velocidade += 1
        
        # Preencher a tela com cor de fundo
        tela.fill(CINZA)
        
        # Desenhar elementos do jogo
        desenhar_carro(carro_x, carro_y)
        desenhar_obstaculos(obstaculos)

        # Mostrar pontuação na tela
        font = pygame.font.SysFont("Arial", 30)
        texto_pontuacao = font.render(f"Distância: {distancia}", True, PRETO)
        tela.blit(texto_pontuacao, (10, 10))

        # Atualizar a tela
        pygame.display.update()

    # Exibir mensagem de fim de jogo
    tela.fill(BRANCO)
    font_game_over = pygame.font.SysFont("Arial", 50)
    texto_game_over = font_game_over.render("GAME OVER", True, PRETO)
    tela.blit(texto_game_over, (LARGURA_TELA // 2 - texto_game_over.get_width() // 2, ALTURA_TELA // 2 - 50))
    pygame.display.update()

    # Esperar para fechar a janela
    pygame.time.wait(2000)

    pygame.quit()

# Iniciar o jogo
jogo()

