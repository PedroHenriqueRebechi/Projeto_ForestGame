import time

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
TAMANHO_MOCHILA = 6


def criar_pausa():
    for i in range(3):
        print(".", end="")
        time.sleep(0.5)


def enviar_introducao():
    # Mensagem inicial - Solicita nome do jogador
    nome = str(
        input(
            """
======================================================================
SEJA BEM-VINDO AO FOREST GAME - SOBREVIVENDO NA FLORESTA!
Este é um jogo de sobrevivência onde você precisa coletar recursos,
enfrentar desafios e voltar para casa.

Digite seu nome: """
        )
    )
    print(
        f"""
Boa Sorte {nome}!
======================================================================"""
    )

    criar_pausa()
    return nome


def mostrar_atributos(vida, energia, mochila):
    print(f"=== Vida: {vida} ===")
    print(f"=== Energia: {energia} ===")
    print(f"=== Mochila: {mochila} ===\n")


while True:

    vida = 100
    energia = 100
    mochila = []

    # Introdução do jogo - Recebe nome do jogador
    jogador = enviar_introducao()

    # 1ª Situação
    print(
        "\nVocê acorda em uma floresta densa e escura, não sabendo onde está e o que fazer. Você encontra ao seu redor uma mochila e prontamente pega ela.\n"
    )
    mostrar_atributos(vida, energia, mochila)
    criar_pausa()

    
    opcao = int(
        input(
            """
[1] Olhar dentro da mochila
[2] Começa a explorar a floresta
[3] Grita por ajuda

Digite sua opção: """
        )
    )

    # if opcao == 1:
