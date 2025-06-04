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
mochila = []
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
    dano = animais[animal]['dano']

    print(f'\nVocê é atacado por um(a) {animal} e perde {dano} pontos de vida!')
    vida_animal = animais[animal]['vida']
    print("Escolha sua ação:")
    print('(1) Atacar com facão')
    print('(2) Usar item da mochila')
    print('(3) Fugir')
    opcao = int(input('Digite o número da ação desejada: '))

    if opcao == 1:
        vida_animal -= itens['facão']['dano']
        print(f'\nVocê atacou o {animal} e agora a vida dele está em {vida_animal}')
        if vida_animal <= 0:
            print(f"\nParabéns, você derrotou o {animal}!!")
            criar_pausa()
            print(f'\nVocê ganhou -- ') #criar funcionamento de pontos 
        else:
            criar_pausa()
            print(f"\nO {animal} atacou você e tirou mais {dano} pontos de vida!!")
    
    elif opcao == 2:
        print(mochila)
        #terminar função

    elif opcao == 3:
        chance = random.randint(1,3)
        if chance == 1:
            print(f'\nVocê tentou fugir, mas o {animal} te atacou e tirou {dano} pontos de vida')
        elif chance == 2:
            print(f'\nEssa foi por pouco!! o {animal} errou o ataque, mas você não conseguiu fugir')
        else:
            print('\nVocê escapou dos ataques e conseguiu fugir!!')
    else:
        print("opção invalida, tente novamente")
        return

def mostrar_atributos(vida, energia, pontuacao, mochila):
    print(f"\nVida: {vida} | Energia: {energia} | Pontuação: {pontuacao} | Mochila: {mochila}\n")

def explorar(vida):
    print('\nVocê decide explorar a floresta e procurar por alguém')
    criar_pausa()
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem rastros indo para uma caverna, você se aproxima e ...')   

    animal = random.choice(list(animais.keys()))
    dano = animais[animal]['dano']

    print(f'Você é atacado por um(a) {animal} selvagem e perde {dano} pontos de vida!')
    
    print(f"Escolha sua ação:")
    print('(1) Atacar com facão ')
    print('(2) Usar item da mochila')
    print('(3) Fugir')
    opcao = int(input('Digite o número da ação desejada: '))
    
    if opcao == '1':
        # CRIAR FUNÇÂO
        return
    
    elif opcao == '2':
        # CRIAR FUNÇÂO
        return
    
    elif opcao == '3':
        # CRIAR FUNÇÂO
        return
    
def montar_abrigo():
    global abrigo
    nivel_exploracao = 0

    while True:
        print('\nVocê decide montar um abrigo')
        criar_pausa()
        print('Após um tempo de exploração, você encontra alguns galhos, pedras e folhas.')
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
            animal = random.choice(list(animais.keys()))
            dano = animais[animal]['dano']

            print(f'\nVocê é atacado por um(a) {animal} e perde {dano} pontos de vida!')
            print("Escolha sua ação:")
            print('(1) Atacar com facão')
            print('(2) Usar item da mochila')
            print('(3) Fugir')
            opcao = int(input('Digite o número da ação desejada: '))

            if opcao == 1:
                print("Você ataca com facão!")
                vida_animal= animais[animal]['vida']
                vida_animal= vida_animal - itens['facão']['dano']
            elif opcao == 2:
                print("Você tenta usar um item!")
            elif opcao == 3:
                print("Você tenta fugir!")
            else:
                print("Opção inválida.")

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
    comidas= random.choice(list(itens.keys()))
    encontrou_animal= random.choice([True,False])
    tipo_item= itens[comidas].get ('tipo')

    while tipo_item not in ['comida', 'bebida']:
         comidas= random.choice(list(itens.keys()))
         tipo_item= itens[comidas].get ('tipo')

    if encontrou_animal:
         animal_aleatorio= random.choice(list(animais.keys()))
         print(f'\nVocê avista um(a) {animal_aleatorio} e ele está com um monte de {comidas}')
         print(f'\n(1) Pegar escondido e fugir')
         print(f'(2) ataque surpresa no(a) {animal_aleatorio} e pegar mais de um item')
         print('(3) continuar explorando')
         escolha= int(input("Qual será sua escolha?"))
         
         if escolha == 1:
            criar_pausa()
            chance = random.randint(1, 4)
            if chance == 1:
                dano = animais[animal_aleatorio]['dano']
                vida -= dano
                print(f'\nO(a) {animal_aleatorio} te viu! Você foi atacado e perdeu {dano} de vida.') 
                print(f'\nVocê teve que fugir, mais sorte na próxima, o(a) {animal_aleatorio} não é brincadeira!!')
            else:
                if len(mochila) < TAMANHO_MOCHILA:
                    mochila.append(comidas)
                    print(f'\nVocê conseguiu pegar o(a) {comidas} e fugir sem ser visto!')
                else:
                    print('\nVocê conseguiu pegar, mas a mochila está cheia e teve que deixar o item para trás.')
         elif escolha == 2:
            criar_pausa()
            if 'facão' in mochila:
                vida_animal = animais[animal_aleatorio]['vida']
                dano = itens['facão']['dano']
                vida_animal -= dano
                print(f'\nVocê atacou com o facão e causou {dano} de dano ao {animal_aleatorio}.')
                print('Qual será sua próxima ação?')
                print("Escolha sua ação:")
                print('(1) Atacar com facão')
                print('(2) Usar item da mochila')
                print('(3) Fugir')
                opcao = int(input('Digite o número da ação desejada: '))

                if opcao == 1:
                    vida_animal -= itens['facão']['dano']
                    print(f'\nVocê atacou o {animal_aleatorio} e agora a vida dele está em {vida_animal}')
                    if vida_animal <= 0:
                        print(f'\nVocê derrotou o {animal_aleatorio} e pegou 2 {comidas}!')
                    for i in range(2):
                        if len(mochila) < TAMANHO_MOCHILA:
                            mochila.append(comidas)
                        else:
                            print("Mochila cheia. Não foi possível pegar mais.")
                    else:
                        criar_pausa()
                        print(f"\nO {animal_aleatorio} atacou você e tirou mais {dano} pontos de vida!!")
                
                elif opcao == 2:
                    print(mochila)
                    #terminar função

                elif opcao == 3:
                    chance = random.randint(1,3)
                    if chance == 1:
                        print(f'\nVocê tentou fugir, mas o {animal_aleatorio} te atacou e tirou {dano} pontos de vida')
                    elif chance == 2:
                        print(f'\nEssa foi por pouco!! o {animal_aleatorio} errou o ataque, mas você não conseguiu fugir')
                    else:
                        print('\nVocê escapou dos ataques e conseguiu fugir!!')
                else:
                    print("opção invalida, tente novamente")
                    return
         if escolha == 3: 
             criar_pausa()
             chance = random.randint(1,4)
             if chance == 4:
                 energia -= 10
                 print (f'\nVocê não encontrou nada e ainda perdeu 10 de energia, agora sua energia é {energia}')
             else:
                 banana = itens['banana']
                 energia -=10
                 print(f'\nVocê encontrou uma banana, parabens!')
                 if len (mochila) < TAMANHO_MOCHILA:
                    mochila.append('banana')
                 else:
                     print("sua mochila está cheia!!")
         else:
             criar_pausa()
             print("escolha invalida")
             return
            
                       
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
        buscar_comida()
        break
    elif acao == '2':
        montar_abrigo()
        break
    elif acao == '3':
        explorar(vida)
        
    elif acao == '4':
        # CRIAR FUNÇÃO ----> usar_item()
        break
    else:
        print("Ação inválida.")
