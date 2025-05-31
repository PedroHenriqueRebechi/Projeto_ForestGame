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
    nome = str(input("""
==============================================================================
SEJA BEM-VINDO AO FOREST GAME - SOBREVIVENDO NA FLORESTA!
Este é um jogo de sobrevivência onde você precisa coletar recursos, enfrentar 
desafios e voltar para casa. Você começa o jogo com vida e energia máxima,
e ao decorrer do jogo você poderá restaurar esses atributos comendo e descansando.

Digite seu nome: """))
    print(f"""
Boa Sorte {nome}!
=============================================================================""")

    criar_pausa()
    return nome

def mostrar_atributos(vida, energia, mochila):
    print(f"=== Vida: {vida} ===")
    print(f"=== Energia: {energia} ===")
    print(f"=== Mochila: {mochila} ===\n")

def mostrar_opcoes():
    opcao = int(input("""
Digite sua opção:
"""))

while True:

    vida = 100
    energia = 100
    mochila = []

    # Introdução do jogo - Recebe nome do jogador
    jogador = enviar_introducao()

    # 1ª Situação
    print("\nVocê acorda em uma floresta densa e escura, não sabendo onde está e o que fazer. Você encontra ao seu redor uma mochila e prontamente pega ela\n")
    # mostrar_atributos(vida, energia, mochila)
    criar_pausa()

    opcao = int(input("""
[1] Olhar dentro da mochila
[2] Começa a explorar a floresta
[3] Grita por ajuda

[4] Ver atributos              
[5] Sair do jogo 

Digite sua opção: """))

    if opcao == 1:
        print('\nVocê olha dentro da mochila e encontra duas maças, elas parecem saborosas')
        mochila.append('maçã')
        mochila.append('maçã')
        continue

    elif opcao == 2:
        print('\nVocê começa a andar pela floresta, a princípio sem rumo algum.')
        criar_pausa()
        print('Depois de tanto andar, você finalmente encontra algo, pegadas de algum animal estão indo para uma caverna')
        continue

    elif opcao == 3:
        continue

    elif opcao == 4:
        mostrar_atributos(vida, energia, mochila)

    elif opcao == 5:
        print('Até logo!')
        break
    

        
