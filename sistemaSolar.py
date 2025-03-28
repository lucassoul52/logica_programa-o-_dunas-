import pygame # type: ignore
import math

# Inicializando o Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
LARANJA = (255, 165, 0)
CINZA = (169, 169, 169)
BRANCO = (255, 255, 255)

# Dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600

# Inicializando a tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Simulador do Sistema Solar")

# Definindo o Sol no centro
sol_pos = (LARGURA_TELA // 2, ALTURA_TELA // 2)
sol_raio = 40

# Planetas (posição, raio, cor e distância do Sol)
planetas = [
    {"cor": CINZA, "raio": 6, "distancia": 60, "velocidade_orbita": 0.01},
    {"cor": AZUL, "raio": 10, "distancia": 100, "velocidade_orbita": 0.008},
    {"cor": VERDE, "raio": 15, "distancia": 150, "velocidade_orbita": 0.005},
    {"cor": VERMELHO, "raio": 12, "distancia": 200, "velocidade_orbita": 0.003},
    {"cor": LARANJA, "raio": 18, "distancia": 250, "velocidade_orbita": 0.002},
]

# Função para desenhar o Sol
def desenhar_sol():
    pygame.draw.circle(tela, AMARELO, sol_pos, sol_raio)

# Função para desenhar os planetas
def desenhar_planetas():
    for planeta in planetas:
        x = sol_pos[0] + planeta["distancia"] * math.cos(planeta["angulo"])
        y = sol_pos[1] + planeta["distancia"] * math.sin(planeta["angulo"])
        pygame.draw.circle(tela, planeta["cor"], (int(x), int(y)), planeta["raio"])

# Função para atualizar a posição dos planetas (órbitas)
def atualizar_orbitas():
    for planeta in planetas:
        planeta["angulo"] += planeta["velocidade_orbita"]

# Função principal do jogo
def jogo():
    # Inicializando os ângulos dos planetas
    for planeta in planetas:
        planeta["angulo"] = 0

    # Loop principal do jogo
    rodando = True
    while rodando:
        # Processando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Preenchendo a tela com a cor preta
        tela.fill(PRETO)

        # Desenhando o Sol
        desenhar_sol()

        # Atualizando e desenhando os planetas
        atualizar_orbitas()
        desenhar_planetas()

        # Atualizando a tela
        pygame.display.flip()

        # Controlando o FPS
        pygame.time.Clock().tick(60)

    pygame.quit()

# Iniciando o jogo
jogo()
