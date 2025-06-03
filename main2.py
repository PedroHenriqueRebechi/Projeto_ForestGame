# Outra tentativa
import time

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_MAXIMA = 100
TAMANHO_MOCHILA = 6

vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = []

animais = {
    'lobo': {'dano': 10},
    'cobra': {'dano': 5},
    'urso': {'dano': 15}
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
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem pegadas indo para uma caverna, você se aproxima e ...')
    print('Você é atacado por um lobo selvagem e perde 10 pontos de vida!')
    dano = 10
    return vida - dano

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
        #buscar_comida()
    elif acao == '2':
        break
        #montar_abrigo()
    elif acao == '3':
        explorar(vida)
        
    elif acao == '4':
        #usar_item()
        break
    else:
        print("Ação inválida.")
