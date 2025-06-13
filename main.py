from modulosTimer import criar_pausa, criar_pausa_maior
import random


# Constantes
VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_MAXIMA = 100
TAMANHO_MOCHILA = 6

vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = ['facao', 'banana']
abrigo = 0
abrigo_montado= False
introducao_enviada = False 

itens = {
    'biscoito': {'tipo':'comida','regeneração': 25, 'energia': 30},
    'energetico': {'tipo':'bebida','regeneração': 15, 'energia': 50},
    'facao': {'tipo':'arma','dano': 35},
    'banana': {'tipo':'comida','regeneração': 20, 'energia': 30},
    'laranja': {'tipo':'comida','regeneração': 20, 'energia': 30},
    'mapa': {'tipo': 'mapear'},     
}

animais = {
    'lobo': {'dano': 10, 'vida': 90},
    'cobra': {'dano': 5, 'vida': 50},
    'urso': {'dano': 15, 'vida': 130},
    'javali': {'dano': 10, 'vida': 100}
}

durabilidade_abrigo = {
    'abrigo fraco': {'durabilidade': 20},
    'abrigo medio': {'durabilidade': 45},
    'abrigo forte': {'durabilidade': 60}
}

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
    global pontuacao
    global energia
    animal = random.choice(list(animais.keys()))
    dano = itens['facao']['dano']
    dano_do_animal = animais[animal]['dano']
    vida_animal = animais[animal]['vida']
    

    print(f'\nVocê é atacado por um(a) {animal} e perde {dano_do_animal} pontos de vida!')
    vida -= dano_do_animal

    if vida <= 0:
        print(f"\n{nome}, você morreu por um(a) {animal}... ☠️")
        print("GAME OVER")
        with open('statusFinal.txt', 'a') as arquivo:
            arquivo.write(f'\nVoce perdeu o jogo ForestGame...\nVida: {vida} | Energia: {energia} | Pontuacao: {pontuacao} | Mochila: {mochila}')
        exit()
    
    mostrar_atributos()

    
    while vida_animal > 0:
        print("Escolha sua ação:")
        print('(1) Atacar com facao')
        print('(2) Usar item da mochila')
        print('(3) Fugir')
        opcao = int(input('Digite o número da ação desejada: '))

        if opcao == 1:
            criar_pausa()
            chance_de_ataque_animal = random.choice([True,False])
            if chance_de_ataque_animal:
                print(f'\nVocê é atacado pelo(a) {animal} novamente e perde {dano_do_animal} pontos de vida!')
                vida -= dano_do_animal
                mostrar_atributos()
            else:
                print(f'\nVocê desviou do ataque do(a) {animal}!\n')
            criar_pausa()
            print(f"\nVocê atacou o(a) {animal} e causou {dano} pontos de dano!\nVocê gastou 10 de energia")
            energia -= 10
            vida_animal -= itens['facao']['dano']
            print(f'Agora a vida do(a) {animal} está em {vida_animal}')

            
            
        elif opcao == 2:
            usar_item()
            chance_de_ataque_animal = random.choice([True,False])
            if chance_de_ataque_animal:
                print(f'\nVocê é atacado pelo(a) {animal} novamente e perde {dano_do_animal} pontos de vida!')
                vida -= dano_do_animal
                mostrar_atributos()
            else:
                print(f'\nVocê desviou do ataque do(a) {animal}!\n')
            
            #return

        elif opcao == 3:
            chance = random.randint(1,3)
            if chance == 1:
                vida -= dano_do_animal
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
        
    print(f"\nParabéns {nome}, você derrotou o(a) {animal}!!")
    criar_pausa()
    pontuacao += 35
    print(f'\nVocê ganhou 35 pontos ') 
    return

def mostrar_atributos():
    global vida
    global energia
    global pontuacao
    global mochila

    return print(f"\nVida: {vida} | Energia: {energia} | Pontuação: {pontuacao} | Mochila: {mochila}")

def encontrar_saida_com_mapa():
    global vida, energia, mochila, pontuacao
    print('\nVocê vê no mapa o caminho de saída da floresta e consegue sair dela!')
    print(f'Parabéns! Você ganhou o jogo com {pontuacao} pontos!')
    
    # Salvar status final do jogo com pontuacao
    with open('statusFinal.txt', 'a') as arquivo:
        arquivo.write(f'\nVoce venceu o jogo ForestGame!\nVida: {vida} | Energia: {energia} | Pontuacao: {pontuacao} | Mochila: {mochila}')
        
    exit()

def explorar():
    global pontuacao
    print('\nVocê decide explorar a floresta e procurar por alguém')
    criar_pausa()
    pontuacao += 10
    print('\nDepois de andar por um tempo, você finalmente encontra algo. Existem rastros indo para uma caverna, você se aproxima e entra nela. Parabéns! Você ganho mais 10 pontos por descobrir um lugar novo!\n',)
    criar_pausa()   
    print('\nMas...')
    combate()
    
def montar_abrigo():
    global abrigo,energia,abrigo_montado
    nivel_exploracao = 0

    while True:
        print('\nVocê pensa que seria bom ter um abrigo')
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
                tipo = 'abrigo medio'
            else:
                tipo = 'abrigo forte'

            abrigo = durabilidade_abrigo[tipo]['durabilidade']
            print(f'\nVocê construiu um {tipo}.')
            print(f'Durabilidade do abrigo: {abrigo}')
            energia -=10
            print(f'\nVocê usou 10 de energia para construir esse abrigo, agora sua energia é {energia}\n')
            abrigo_montado = True
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
 
def acessar_abrigo():
    global energia, abrigo, abrigo_montado
    if abrigo_montado == True:
        print("\nVocê escolheu acessar seu abrigo para descansar e recuperar energia") 
        abrigo -= 10
        # energia += 20
        print("Você acorda e tem um tempo tranquilo e ganha 20 de energia")
        if energia + 20 >= ENERGIA_MAXIMA :
            energia = ENERGIA_MAXIMA
        elif energia == ENERGIA_MAXIMA:
            print('\nSua energia está cheia')
        else:
            energia += 20
        if abrigo == 0:
            print("\nSeu abrigo está muito velho e desabou, construa um novo para recuperar energia\n")
    else:
        print("\nVocê não tem um abrigo construido\n")

def buscar_comida():
    global vida, energia, mochila
    print('\nVocê decide sair em busca de comida')
    criar_pausa()
    comidas = random.choice(list(itens.keys()))
    encontrou_animal = random.choice([True,False])
    tipo_item = itens[comidas].get ('tipo')

    while tipo_item not in ['comida', 'bebida']:
         comidas = random.choice(list(itens.keys()))
         tipo_item = itens[comidas].get ('tipo')

    if encontrou_animal:
        animal_aleatorio = random.choice(list(animais.keys()))
        print(f'\nVocê avista um(a) {animal_aleatorio} e, atrás dele(a), há um monte de {comidas}s\n')
        print('Escolha sua ação:')
        print(f'(1) Pegar escondido e fugir')
        print(f'(2) Atacar o(a) {animal_aleatorio} e tentar pegar mais de um(a) {comidas}')
        print('(3) continuar explorando')
        escolha = int(input("Qual será sua escolha? "))
         
        if escolha == 1:
            criar_pausa()
            chance = random.randint(1, 4)
            if chance == 1:
                dano = animais[animal_aleatorio]['dano']
                vida -= dano
                print(f'\nO(a) {animal_aleatorio} te viu! Você foi atacado e perdeu {dano} de vida.') 
                print(f'Você teve que fugir, mais sorte na próxima, o(a) {animal_aleatorio} não é brincadeira!!')
            else:
                if len(mochila) < TAMANHO_MOCHILA:
                    mochila.append(comidas)
                    print(f'\nVocê conseguiu pegar o(a) {comidas} e fugir sem ser visto!')
                else:
                    print('\nVocê conseguiu pegar, mas a mochila está cheia e teve que deixar o item para trás.')
        elif escolha == 2:
            criar_pausa()
            if 'facao' in mochila:
                vida_animal = animais[animal_aleatorio]['vida']
                dano = itens['facao']['dano']
                vida_animal -= dano
                print(f'\nVocê atacou com o facao e causou {dano} de dano ao {animal_aleatorio}.')
                print('Qual será sua próxima ação?')
                mostrar_atributos()
                print("Escolha sua ação:")
                print('(1) Atacar com facao')
                print('(2) Usar item da mochila')
                print('(3) Fugir')
                opcao = int(input('Digite o número da ação desejada: '))
                if opcao == 1:
                    vida_animal -= itens['facao']['dano']
                    print(f'\nVocê atacou o {animal_aleatorio} e agora a vida dele está em {vida_animal}')
                    energia -= 10 
                    if vida_animal <= 0:
                        print(f'\nVocê derrotou o {animal_aleatorio} e pegou 2 {comidas}!')
                    for i in range(2):
                        if len(mochila) < TAMANHO_MOCHILA:
                            mochila.append(comidas)
                        else:
                            print("Mochila cheia. Não foi possível pegar mais.")
                    else:
                        criar_pausa()
                        print(f"\nO(a) {animal_aleatorio} atacou você e tirou mais {dano} pontos de vida!!")
                elif opcao == 2:
                    usar_item()
                    return
                elif opcao == 3:
                    chance = random.randint(1,3)
                    if chance == 1:
                        print(f'\nVocê tentou fugir, mas o(a) {animal_aleatorio} te atacou e tirou {dano} pontos de vida')
                    elif chance == 2:
                        print(f'\nEssa foi por pouco! o(a) {animal_aleatorio} errou o ataque, mas você não conseguiu fugir')
                    else:
                        print('\nVocê escapou dos ataques e conseguiu fugir!!')
                else:
                    print("opção invalida, tente novamente")
                    return
        elif escolha == 3: 
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
             print("escolha inválida!")
             return
        
    else:
        print('\nVocê procurou por comida mas não encontrou nada')
        criar_pausa()
        print('\nA floresta parece cada vez mais assustadora')
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
                if vida != VIDA_MAXIMA or energia != ENERGIA_MAXIMA:
                    vida = min(VIDA_MAXIMA, vida + dados_item.get('regeneração', 0))
                    energia = min(ENERGIA_MAXIMA, energia + dados_item.get('energia', 0))
                    print(f"\nVocê usou {item}. Vida atual: {vida}, Energia atual: {energia}")
                    return True
                elif vida == VIDA_MAXIMA and energia == ENERGIA_MAXIMA:
                    print('\nSua vida e energia estão cheias')
            elif dados_item.get('tipo') in ['mapear']:
                encontrar_saida_com_mapa()

            else:
                print(f"\nVocê olha para o(a) {item}, isto vai ser útil")
                mochila.append(item)
                #return False
                return
        else:
            print("\nEscolha inválida.")
            return False
    except ValueError:
        print("\nEntrada inválida. Use um número.")
        return False 

def encontrar_escoteiros():
    global mochila
    print('\nVocê decide ir atrás da fumaça, com medo mas também esperança.')
    criar_pausa()
    print('\nVocê encontra um acampamento! A fumaça estava vindo de uma fogueira, rapidamente você fica eufórico mas')
    criar_pausa()
    print('\nNão tem ninguém aqui, isso é estranho. Por que deixariam tudo para trás?')

    print('Escolha sua ação:')
    print('(1) Sentar perto da fogueira e esperar pelos escoteiros')
    print('(2) Roubar os suprimentos e itens')
    acao = int(input('Digite o número da ação desejada: '))

    if acao == 1:
        print('\nVocê decide esperar')
        criar_pausa_maior()
        print('\nVocê esperou por horas e ninguém apareceu. Realmente algo estranho está acontecendo')
    
    if acao == 2:
        print('\nMesmo se sentindo mal, você pensa que isso é a unica opcão para a sobrevivência')
        criar_pausa()
        print('\nSeu coração está acelerado e entrando na cabana você encontra um mapa! ')
        mochila.append('mapa')

nome = enviar_introducao()

while True:
    mostrar_atributos()
    if vida <= 0:
        print(f"\n{nome}, você morreu na floresta... ☠️")
        print("GAME OVER")
        with open('statusFinal.txt', 'a') as arquivo:
            arquivo.write(f'\nVoce perdeu o jogo ForestGame...\nVida: {vida} | Energia: {energia} | Pontuacao: {pontuacao} | Mochila: {mochila}')
        break
    else:
        if pontuacao < 100:
            if abrigo_montado == False:
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
            elif abrigo_montado == True:
                print("Escolha sua ação:")
                print("(1) Buscar comida")
                print("(2) Acessar abrigo")
                print("(3) Explorar a floresta")
                print("(4) Usar item da mochila")
                acao = input("Digite o número da ação desejada: ")

                if acao == '1':
                    buscar_comida()
                elif acao == '2':
                    acessar_abrigo()
                elif acao == '3':
                    explorar()
                    
                elif acao == '4':
                    usar_item()
                else:
                    print("Ação inválida.")
        elif pontuacao >= 100: # Quando atinge 100 pontos, libera nova ação para o final do jogo
            
            # introducao_enviada = False 
            
            if abrigo_montado == False:
                if introducao_enviada == False:
                    criar_pausa()
                    print('\nVocê viu isso? Uma fumaça está subindo, algo está por perto...')
                    criar_pausa()
                    
                    print("\nEscolha sua ação:")
                    print("(1) Buscar comida")
                    print("(2) Montar abrigo")
                    print("(3) Explorar a floresta")
                    print("(4) Usar item da mochila")
                    print('(5) Ir atrás da fumaça')
                    acao = input("Digite o número da ação desejada: ")
                    

                    if acao == '1':
                        buscar_comida()
                    elif acao == '2':
                        montar_abrigo()
                    elif acao == '3':
                        explorar()
                    elif acao == '4':
                        usar_item()
                    elif acao == '5':
                        encontrar_escoteiros()
                    else:
                        print("Ação inválida.")
                    introducao_enviada = True
                else:
                    print("\nEscolha sua ação:")
                    print("(1) Buscar comida")
                    print("(2) Montar abrigo")
                    print("(3) Explorar a floresta")
                    print("(4) Usar item da mochila")
                    print('(5) Ir atrás da fumaça')
                    acao = input("Digite o número da ação desejada: ")
                    

                    if acao == '1':
                        buscar_comida()
                    elif acao == '2':
                        montar_abrigo()
                    elif acao == '3':
                        explorar()
                    elif acao == '4':
                        usar_item()
                    elif acao == '5':
                        encontrar_escoteiros()
                    else:
                        print("Ação inválida.")
                        
            elif abrigo_montado == True:
                if introducao_enviada == False:
                    criar_pausa()
                    print('Você viu isso? Uma fumaça está subindo, algo está por perto...')
                    criar_pausa()
                    print("Escolha sua ação:")
                    print("(1) Buscar comida")
                    print("(2) Acessar abrigo")
                    print("(3) Explorar a floresta")
                    print("(4) Usar item da mochila")
                    print('(5) Ir atrás da fumaça')
                    acao = input("Digite o número da ação desejada: ")
                    

                    if acao == '1':
                        buscar_comida()
                    elif acao == '2':
                        acessar_abrigo()
                    elif acao == '3':
                        explorar()
                    elif acao == '4':
                        usar_item()
                    elif acao == '5':
                        encontrar_escoteiros()
                    else:
                        print("Ação inválida.")
                    introducao_enviada = True
                else:
                    print("Escolha sua ação:")
                    print("(1) Buscar comida")
                    print("(2) Acessar abrigo")
                    print("(3) Explorar a floresta")
                    print("(4) Usar item da mochila")
                    print('(5) Ir atrás da fumaça')
                    acao = input("Digite o número da ação desejada: ")
                    

                    if acao == '1':
                        buscar_comida()
                    elif acao == '2':
                        acessar_abrigo()
                    elif acao == '3':
                        explorar()
                    elif acao == '4':
                        usar_item()
                    elif acao == '5':
                        encontrar_escoteiros()
                    else:
                        print("Ação inválida.")
        
                






            # print(f'Você atingiu {pontuacao} pontos e agora mais uma ação foi liberada!')
            # criar_pausa()
            # print("Escolha sua ação:")
            # print("(1) Buscar comida")
            # print("(2) Montar abrigo")
            # print("(3) Explorar a floresta")
            # print("(4) Usar item da mochila")
            # print('(5) TESTE ')
            # acao = input("Digite o número da ação desejada: ")

            # if acao == '1':
            #     buscar_comida()
            # elif acao == '2':
            #     montar_abrigo()
            # elif acao == '3':
            #     explorar()
                
            # elif acao == '4':
            #     usar_item()
            # else:
            #     print("Ação inválida.")
