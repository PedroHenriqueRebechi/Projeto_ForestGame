import tkinter as tk
from tkinter import messagebox
import random

# --- Dados do jogo ---
VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
TAMANHO_MOCHILA = 6

vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = []

itens = {
    'biscoito': {'tipo': 'comida', 'regeneração': 25, 'energia': 30},
    'energético': {'tipo': 'bebida', 'regeneração': 15, 'energia': 50},
    'facão': {'tipo': 'arma', 'dano': 35},
    'banana': {'tipo': 'comida', 'regeneração': 20, 'energia': 30}
}

# --- Funções do jogo ---

def atualizar_status():
    status_var.set(f"Vida: {vida} | Energia: {energia} | Pontuação: {pontuacao}")
    mochila_var.set("Mochila: " + ", ".join(mochila) if mochila else "Mochila vazia")

def buscar_comida():
    global vida, energia
    resultado = random.choice(["nada", "banana", "biscoito", "animal"])
    if resultado == "nada":
        energia -= 10
        messagebox.showinfo("Exploração", "Você não encontrou nada e perdeu 10 de energia.")
    elif resultado in itens:
        if len(mochila) < TAMANHO_MOCHILA:
            mochila.append(resultado)
            messagebox.showinfo("Comida Encontrada", f"Você encontrou um(a) {resultado}!")
        else:
            messagebox.showinfo("Mochila Cheia", "Você encontrou comida, mas a mochila está cheia!")
    elif resultado == "animal":
        vida -= 15
        messagebox.showinfo("Animal!", "Você foi atacado por um animal e perdeu 15 de vida!")
    atualizar_status()

def montar_abrigo():
    global pontuacao
    pontuacao += 5
    messagebox.showinfo("Abrigo", "Você montou um abrigo simples e ganhou 5 pontos.")
    atualizar_status()

def explorar():
    global pontuacao
    chance = random.randint(1, 4)
    if chance == 1:
        messagebox.showinfo("Exploração", "Você encontrou uma trilha! +10 pontos.")
        pontuacao += 10
    else:
        messagebox.showinfo("Exploração", "Você não encontrou nada relevante.")
    atualizar_status()

def usar_item():
    global vida, energia
    if not mochila:
        messagebox.showinfo("Mochila", "Sua mochila está vazia!")
        return

    item = mochila.pop(0)  # Usa o primeiro item da mochila
    dados = itens[item]

    if dados['tipo'] in ['comida', 'bebida']:
        vida = min(VIDA_MAXIMA, vida + dados['regeneração'])
        energia = min(ENERGIA_MAXIMA, energia + dados['energia'])
        messagebox.showinfo("Usar Item", f"Você usou {item}. Vida e energia recuperadas!")
    else:
        messagebox.showinfo("Usar Item", f"O item {item} não pode ser usado diretamente.")
        mochila.append(item)  # devolve o item
    atualizar_status()

def verificar_morte():
    if vida <= 0:
        messagebox.showerror("Game Over", "Você morreu na floresta... ☠️")
        janela.quit()

# --- Interface Gráfica ---

janela = tk.Tk()
janela.title("Forest Game - Sobrevivendo na Floresta")
janela.geometry("500x400")
janela.resizable(False, False)

# Variáveis de texto
status_var = tk.StringVar()
mochila_var = tk.StringVar()

# Labels
tk.Label(janela, text="🌲 Forest Game 🌲", font=("Arial", 18)).pack(pady=10)
tk.Label(janela, textvariable=status_var, font=("Arial", 12)).pack(pady=5)
tk.Label(janela, textvariable=mochila_var, font=("Arial", 10)).pack(pady=5)

# Botões
tk.Button(janela, text="Buscar Comida", width=20, command=lambda: [buscar_comida(), verificar_morte()]).pack(pady=5)
tk.Button(janela, text="Montar Abrigo", width=20, command=montar_abrigo).pack(pady=5)
tk.Button(janela, text="Explorar Floresta", width=20, command=explorar).pack(pady=5)
tk.Button(janela, text="Usar Item", width=20, command=usar_item).pack(pady=5)
tk.Button(janela, text="Sair", width=20, command=janela.quit).pack(pady=15)

# Iniciar status
atualizar_status()

# Iniciar interface
janela.mainloop()
