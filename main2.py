# Outra tentativa
import time
import random

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_MAXIMA = 100
TAMANHO_MOCHILA = 6

vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = []

itens = {
    'biscoito': {'regeneração': 25, 'energia': 30},
    'energético': {'regeneração': 15, 'energia': 50},
    'facão': {'dano': 35},
    'banana': {'regeneração': 20, 'energia': 30}
}

animais = {
    'lobo': {'dano': 10, 'vida': 90},
    'cobra': {'dano': 5, 'vida': 50},
    'urso': {'dano': 15, 'vida': 130}
}

def criar_pausa():
    for i in range(3):
        print(".", end="")
        time.sleep(0.5)

def enviar_introducao():
    # Mensagem inicial - Solicita nome do jogador
    nome = str(input("""
==============================================================================
SEJA BEM-VINDO AO FOREST GAME - SOBREVIVENDO NA FLORESTA!
Você está perdido(a) na floresta após uma tempestade. Seu objetivo é sobreviver, coletar recursos e encontrar o caminho de volta para casa. Para isso, acumule pontos e encontre o mapa da saída.

Digite seu nome: """))
    print(f"""
Boa Sorte {nome}!
=============================================================================""")

    criar_pausa()
    return nome

def mostrar_atributos(vida, energia, pontuacao, mochila):
    print(f"\nVida: {vida} | Energia: {energia} | Pontuação: {pontuacao} | Mochila: {mochila}\n")

def explorar(vida):
    print('\nVocê decide explorar a floresta e procurar por alguém')
    criar_pausa()
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem rastros indo para uma caverna, você se aproxima e ...')   

    animal = random.choice(list(animais.keys()))
    dano = animais[animal]['dano']

    print(f'Você é atacado por um(a) {animal} selvagem e perde {dano} pontos de vida!')
    
    opcao = int(input("""
Escolha sua ação:


"""))
    

nome = enviar_introducao()

while True:
    mostrar_atributos(vida, energia, pontuacao, mochila)
    print("Escolha sua ação:")
    print("(1) Buscar comida")
    print("(2) Montar abrigo")
    print("(3) Explorar a floresta")
    print("(4) Usar item da mochila")
    acao = input("Digite o número da ação desejada: ")

    if acao == '1':
        break
        # CRIAR FUNÇÃO ----> buscar_comida()
    elif acao == '2':
        break
        # CRIAR FUNÇÃO ----> montar_abrigo()
    elif acao == '3':
        explorar(vida)
        
    elif acao == '4':
        # CRIAR FUNÇÃO ----> usar_item()
        break
    else:
        print("Ação inválida.")
