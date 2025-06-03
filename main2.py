# Outra tentativa
import time

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_MAXIMA = 100
TAMANHO_MOCHILA = 6
vida = 100

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

def mostrar_atributos(vida, energia, pontuacao,mochila):
    print(f"\nVida: {vida} | Energia: {energia} | Pontuação: {pontuacao} | Mochila: {mochila}\n")

def explorar():
    print('\nVocê decide explorar a floresta e procurar por alguém')
    criar_pausa()
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem pegadas indo para uma caverna, você se aproxima e ...')
    print('\nVocê é atacado por um lobo selvagem e perde 10 pontos de vida!')
    vida -= 10
    

nome = enviar_introducao()

