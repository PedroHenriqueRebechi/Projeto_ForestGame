import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa a caixa de mensagens do Tkinter
import random  # Para gerar escolhas e eventos aleatórios

# Define os valores máximos
VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
TAMANHO_MOCHILA = 6

# Estado inicial do jogador
vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = []

# Criação da janela principal do jogo
janela = tk.Tk()  # Cria a janela principal
janela.title("Forest Game - Sobrevivendo na Floresta")  # Define o título da janela
janela.geometry("800x500")  # Define o tamanho da janela
janela.configure(bg="#0d1b1e")  # Define a cor de fundo da janela (floresta escura)

# Define a fonte e a cor padrão para textos
fonte_padrao = ("Courier", 12)
cor_texto = "#e0e0e0"

# Criação de um frame para os status do jogador (vida, energia, etc.)
frame_status = tk.Frame(janela, bg="#0d1b1e")  # Cria um container para os rótulos
frame_status.pack(pady=10)  # Exibe o frame com um pequeno espaçamento vertical

# Rótulo da vida
label_vida = tk.Label(frame_status, text=f"Vida: {vida}", font=fonte_padrao, fg="red", bg="#0d1b1e")
label_vida.pack(side=tk.LEFT, padx=10)  # Exibe o rótulo à esquerda com espaçamento

# Rótulo da energia
label_energia = tk.Label(frame_status, text=f"Energia: {energia}", font=fonte_padrao, fg="yellow", bg="#0d1b1e")
label_energia.pack(side=tk.LEFT, padx=10)

# Rótulo da pontuação
label_pontuacao = tk.Label(frame_status, text=f"Pontuação: {pontuacao}", font=fonte_padrao, fg="white", bg="#0d1b1e")
label_pontuacao.pack(side=tk.LEFT, padx=10)

# Rótulo da mochila
label_mochila = tk.Label(janela, text=f"Mochila: {mochila}", font=fonte_padrao, fg=cor_texto, bg="#0d1b1e")
label_mochila.pack()  # Exibe o rótulo da mochila abaixo dos status

# Caixa de texto onde aparece a narrativa e mensagens do jogo
caixa_texto = tk.Text(janela, height=10, width=90, font=("Courier", 11), bg="#102025", fg=cor_texto)
caixa_texto.pack(pady=10)  # Exibe a caixa de texto com espaçamento vertical

# Função para atualizar os valores dos rótulos na interface
def atualizar_status():
    label_vida.config(text=f"Vida: {vida}")
    label_energia.config(text=f"Energia: {energia}")
    label_pontuacao.config(text=f"Pontuação: {pontuacao}")
    label_mochila.config(text=f"Mochila: {mochila}")

# Função para adicionar texto na caixa de narrativa
def mostrar_mensagem(msg):
    caixa_texto.insert(tk.END, msg + "\n")  # Insere a mensagem no final da caixa
    caixa_texto.see(tk.END)  # Faz a rolagem automática para a última linha

# Funções do jogo (lógica misturada com interface abaixo)
def buscar_comida():
    global energia, vida
    mostrar_mensagem("Você decidiu buscar comida...")
    energia -= 10
    atualizar_status()

    achou = random.choice(["banana", "biscoito", "nada"])
    if achou != "nada":
        if len(mochila) < TAMANHO_MOCHILA:
            mochila.append(achou)
            mostrar_mensagem(f"Você encontrou um(a) {achou}!")
        else:
            mostrar_mensagem("Sua mochila está cheia!")
    else:
        mostrar_mensagem("Você não encontrou nada.")
    atualizar_status()

def montar_abrigo():
    mostrar_mensagem("Você tenta montar um abrigo...")
    mostrar_mensagem("Abrigo improvisado construído! Pode proteger por um tempo.")

def explorar():
    global vida
    mostrar_mensagem("Você começa a explorar a floresta...")
    chance = random.randint(1, 3)
    if chance == 3:
        vida -= 15
        mostrar_mensagem("Você foi atacado por um animal selvagem!")
    else:
        mostrar_mensagem("Você encontrou pegadas misteriosas...")
    atualizar_status()

def usar_item():
    global energia, vida
    if not mochila:
        mostrar_mensagem("Você não tem nenhum item na mochila.")
    else:
        item = mochila.pop(0)
        mostrar_mensagem(f"Você usou {item}.")
        if item == "banana":
            energia_boost = 20
            energia = min(ENERGIA_MAXIMA, energia + energia_boost)
            mostrar_mensagem(f"Sua energia aumentou em {energia_boost}!")
        elif item == "biscoito":
            vida_boost = 20
            vida = min(VIDA_MAXIMA, vida + vida_boost)
            mostrar_mensagem(f"Sua vida aumentou em {vida_boost}!")
    atualizar_status()

# Criação do frame onde ficarão os botões de ação
frame_botoes = tk.Frame(janela, bg="#0d1b1e")  # Cria um container para os botões
frame_botoes.pack(pady=10)  # Exibe o frame com espaçamento vertical

# Botão: Buscar comida
tk.Button(frame_botoes, text="Buscar comida", command=buscar_comida, width=20, font=fonte_padrao).pack(side=tk.LEFT, padx=5)

# Botão: Montar abrigo
tk.Button(frame_botoes, text="Montar abrigo", command=montar_abrigo, width=20, font=fonte_padrao).pack(side=tk.LEFT, padx=5)

# Botão: Explorar
tk.Button(frame_botoes, text="Explorar", command=explorar, width=20, font=fonte_padrao).pack(side=tk.LEFT, padx=5)

# Botão: Usar item
tk.Button(frame_botoes, text="Usar item", command=usar_item, width=20, font=fonte_padrao).pack(side=tk.LEFT, padx=5)

# Primeira mensagem ao iniciar o jogo
mostrar_mensagem("Você acorda em uma floresta escura e úmida...\nComece sua jornada de sobrevivência.")

# Inicia o loop principal da interface (janela)
janela.mainloop()
