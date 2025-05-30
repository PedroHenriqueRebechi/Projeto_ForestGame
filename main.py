import time

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
TAMANHO_MOCHILA = 6

# Mensagem inicial - Solicita nome do jogador
jogador = str(input("""
======================================================================
SEJA BEM-VINDO AO FOREST GAME - SOBREVIVENDO NA FLORESTA!
Este é um jogo de sobrevivência onde você precisa coletar recursos,
enfrentar desafios e voltar para casa.

Digite seu nome: """))
print(f"""Boa Sorte {jogador}!
======================================================================
""")

time.sleep(2.5)

