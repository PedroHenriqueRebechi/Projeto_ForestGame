import time
import random

# Constantes
VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_MAXIMA = 100
TAMANHO_MOCHILA = 6

vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = ['facão']
abrigo = 0

itens = {
    'biscoito': {'tipo':'comida','regeneração': 25, 'energia': 30},
    'energético': {'tipo':'bebida','regeneração': 15, 'energia': 50},
    'facão': {'tipo':'arma','dano': 35},
    'banana': {'tipo':'comida','regeneração': 20, 'energia': 30}
}

animais = {
    'lobo': {'dano': 10, 'vida': 90},
    'cobra': {'dano': 5, 'vida': 50},
    'urso': {'dano': 15, 'vida': 130}
}

durabilidade_abrigo = {
    'abrigo fraco': {'durabilidade': 20},
    'abrigo médio': {'durabilidade': 45},
    'abrigo forte': {'durabilidade': 60}
}

def criar_pausa():
    for i in range(3):
        print(".", end="")
        time.sleep(0.5)

def criar_pausa_maior():
    for i in range(3):
        print(".", end="")
        time.sleep(0.10)

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

def combate():
    global vida
    animal = random.choice(list(animais.keys()))
    dano = itens['facão']['dano']
    dano_do_animal = animais[animal]['dano']
    vida_animal = animais[animal]['vida']

    print(f'\nVocê é atacado por um(a) {animal} e perde {dano_do_animal} pontos de vida!')

    vida -= dano_do_animal
    mostrar_atributos()

    while vida_animal > 0:
        print("Escolha sua ação:")
        print('(1) Atacar com facão')
        print('(2) Usar item da mochila')
        print('(3) Fugir')
        opcao = int(input('Digite o número da ação desejada: '))

        if opcao == 1:

            if vida_animal <= 0:
                print(f"\nParabéns {nome}, você derrotou o(a) {animal}!!")
                criar_pausa()
                print(f'\nVocê ganhou -- ') #criar funcionamento de pontos 
            else:
                criar_pausa()
                print(f"\nVocê atacou o(a) {animal} e causou {dano} pontos de dano!")
                vida_animal -= itens['facão']['dano']
                print(f'\nAgora a vida do(a) {animal} está em {vida_animal}')

            chance_de_ataque_animal = random.choice([True,False])
            if chance_de_ataque_animal:
                print(f'\nVocê é atacado pelo(a) {animal} novamente e perde {dano_do_animal} pontos de vida!')
                vida -= dano_do_animal
                mostrar_atributos()
            else:
                print(f'Você desviou do ataque do(a) {animal}!\n')
        
        elif opcao == 2:
            usar_item()
            return

        elif opcao == 3:
            chance = random.randint(1,3)
            if chance == 1:
                print(f'\nVocê tentou fugir, mas o {animal} te atacou e tirou {dano_do_animal} pontos de vida')
                mostrar_atributos()
            elif chance == 2:
                print(f'\nEssa foi por pouco!! o {animal} errou o ataque, mas você não conseguiu fugir')
            else:
                print('\nVocê escapou dos ataques e conseguiu fugir!!')
                return
        else:
            print("opção invalida, tente novamente")
            return

def mostrar_atributos():
    global vida
    global energia
    global pontuacao
    global mochila

    return print(f"\nVida: {vida} | Energia: {energia} | Pontuação: {pontuacao} | Mochila: {mochila}")

def explorar():
    print('\nVocê decide explorar a floresta e procurar por alguém')
    criar_pausa()
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem rastros indo para uma caverna, você se aproxima e\n',)
    criar_pausa()   
    combate()
    # mostrar_atributos()
    
def montar_abrigo():
    global abrigo
    nivel_exploracao = 0

    while True:
        print('\nVocê decide montar um abrigo')
        criar_pausa()
        print('\nApós um tempo de exploração, você encontra alguns galhos, pedras e folhas.')
        print('Deseja criar um abrigo agora ou continuar explorando para conseguir mais recursos?')

        print("\nEscolha sua ação:")
        print('(1) Criar abrigo')
        print('(2) Continuar explorando')
        escolha = input('Digite o número da ação desejada: ')

        if escolha == '1':
            if nivel_exploracao == 0:
                tipo = 'abrigo fraco'
            elif nivel_exploracao == 1:
                tipo = 'abrigo médio'
            else:
                tipo = 'abrigo forte'

            abrigo = durabilidade_abrigo[tipo]['durabilidade']
            print(f'\nVocê construiu um {tipo}.')
            print(f'Durabilidade do abrigo: {abrigo}')
            break

        elif escolha == '2':
            combate()
            nivel_exploracao += 1
            if nivel_exploracao > 2:
                print("\nVocê já explorou o suficiente para construir o abrigo mais forte possível.")
            else:
                print("\nVocê decide explorar mais para melhorar a qualidade do seu abrigo.")
            criar_pausa()
        else:
            print("Escolha inválida. Tente novamente.")

def buscar_comida():
    global vida, energia, mochila
    print('\nVocê decide sair em busca de comida')
    criar_pausa()
    while True:
        item = random.choice(list(itens.keys()))
        if itens[item].get('tipo') in ('comida', 'bebida'):
            break

    encontrou_animal = random.choice([True, False])

    if encontrou_animal:
        animal = random.choice(list(animais.keys()))
        print(f'\nVocê avista um(a) {animal} e ele está com um monte de {item}')
        print('\n(1) Pegar escondido e fugir')
        print('(2) Ataque surpresa')
        print('(3) Continuar explorando')
        try:
            escolha = int(input("Qual será sua escolha? "))
        except ValueError:
            print("Escolha inválida!")
            return

        if escolha == 1:
            criar_pausa()
            if random.randint(1, 4) == 1:
                dano = animais[animal]['dano']
                vida -= dano
                print(f'\nO {animal} te viu! Você perdeu {dano} de vida.')
            else:
                if len(mochila) < TAMANHO_MOCHILA:
                    mochila.append(item)
                    print(f'\nVocê pegou {item} e fugiu!')
                else:
                    print('\nMochila cheia; teve que deixar o item.')
            return
        elif escolha == 2:
            criar_pausa()
            if 'facão' not in mochila:
                print('\nVocê não tem um facão! Impossível atacar.')
                return

            vida_animal = animais[animal]['vida']
            dano_fac = itens['facão']['dano']
            while vida_animal > 0 and vida > 0:
                vida_animal -= dano_fac
                print(f'\nVocê acerta com facão! Vida do {animal}: {vida_animal}')

                if vida_animal <= 0:
                    print(f'\nVocê derrotou o {animal} e pegou 2x {item}!')
                    for _ in range(2):
                        if len(mochila) < TAMANHO_MOCHILA:
                            mochila.append(item)
                        else:
                            print("Mochila cheia, não pegou mais.")
                    break  
                dano_animal = animais[animal]['dano']
                vida -= dano_animal
                print(f'\nO {animal} contra-ataca e tira {dano_animal} de vida. Sua vida: {vida}')

                if vida <= 0:
                    print('\nVocê foi derrotado!')
                    break  
                criar_pausa()
                mostrar_atributos()
                print('(1) Atacar com facão\n(2) Usar item\n(3) Fugir')
                try:
                    opcao = int(input('Sua ação: '))
                except ValueError:
                    print("Escolha inválida!")
                    break

                if opcao == 1:
                    continue  
                elif opcao == 2:
                    usar_item()
                    break
                elif opcao == 3:
                    if random.randint(1, 3) == 3:
                        print('\nVocê escapou!')
                    else:
                        vida -= dano_animal
                        print(f'\nFalhou em fugir. O {animal} te atingiu de novo e tira {dano_animal} de vida.')
                    break
                else:
                    print("Opção inválida.")
                    break
            return
        elif escolha == 3:
            criar_pausa()
            if random.randint(1, 4) == 4:
                energia -= 10
                print(f'\nVocê não achou nada e perdeu 10 de energia (energia: {energia}).')
            else:
                energia -= 10
                print('\nVocê encontrou uma banana!')
                if len(mochila) < TAMANHO_MOCHILA:
                    mochila.append('banana')
                else:
                    print("Mochila cheia!")
            return

        else:
            print("Escolha inválida.")
            return

    criar_pausa()
    energia -= 10
    print(f'\nVocê sai, mas não encontra nada. Energia -10 (agora {energia}).')
    return

def usar_item():
    global vida, energia, mochila
    if not mochila:
        print("\nSua mochila está vazia!")
        return False

    print("\nItens disponíveis na mochila:")
    for i, item in enumerate(mochila):
        print(f"({i}) {item}")

    try:
        escolha = int(input("Digite o número do item que deseja usar: "))
        if 0 <= escolha < len(mochila):
            item = mochila.pop(escolha)
            dados_item = itens.get(item, {})

            if dados_item.get('tipo') in ['comida', 'bebida']:
                vida = min(VIDA_MAXIMA, vida + dados_item.get('regeneração', 0))
                energia = min(ENERGIA_MAXIMA, energia + dados_item.get('energia', 0))
                print(f"\nVocê usou {item}. Vida atual: {vida}, Energia atual: {energia}")
                return True
            else:
                print(f"\n{item} não pode ser usado diretamente.")
                mochila.append(item)
                return False
        else:
            print("\nEscolha inválida.")
            return False
    except ValueError:
        print("\nEntrada inválida. Use um número.")
        return False
                          
nome = enviar_introducao()

while True:
    mostrar_atributos()
    if vida <= 0:
        print(f"\n{nome}, você morreu na floresta... ☠️")
        print("GAME OVER")
        break
    else:
        print("Escolha sua ação:")
        print("(1) Buscar comida")
        print("(2) Montar abrigo")
        print("(3) Explorar a floresta")
        print("(4) Usar item da mochila")
        acao = input("Digite o número da ação desejada: ")

        if acao == '1':
            buscar_comida()
        elif acao == '2':
            montar_abrigo()
        elif acao == '3':
            explorar()
            
        elif acao == '4':
            usar_item()
        else:
            print("Ação inválida.")
