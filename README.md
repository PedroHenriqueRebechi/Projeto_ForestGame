
# 🌲 Forest Game - Sobrevivendo na Floresta

**Forest Game** é um jogo de texto em Python baseado em escolhas, com foco em **sobrevivência**, **exploração** e **estratégia**. O jogador precisa tomar decisões inteligentes para coletar recursos, derrotar animais selvagens e encontrar o caminho de volta para casa. Projeto desenvolvido por Eric Julio da Silva e Pedro Henrique Rebechi durante o curso de Engenharia de Software da PUCPR. Criamos um jogo utilizando a linguagem Python, com foco em aplicar conceitos aprendidos em aula, como lógica de programação, estruturas de dados e desenvolvimento colaborativo. 

---

## 🎮 Como jogar

Ao iniciar o jogo, o jogador entra no papel de uma pessoa perdida em uma floresta após uma tempestade. Seu objetivo é:

- Manter sua **vida** e **energia** acima de zero;
- Coletar **itens** e **recursos**;
- Construir um **abrigo** para descansar;
- Lutar ou fugir de **animais selvagens**;
- Explorar lugares da floresta para ganhar **pontos**;
- Descobrir o **mapa da saída** para vencer o jogo.

---

## 🧠 Mecânicas principais

- ⚔️ **Combate:** você pode lutar com facão, usar itens da mochila ou tentar fugir.
- 🎒 **Mochila:** limitada a 6 itens, é usada para guardar comida, bebida, armas e o mapa.
- 🏕️ **Abrigo:** pode ser construído com diferentes níveis de durabilidade e é necessário para descansar e recuperar energia.
- 🔍 **Exploração:** locais como lago, rio e caverna podem ser descobertos para ganhar pontos e enfrentar desafios.
- 🍌 **Busca por comida:** gera situações aleatórias com risco ou recompensa.
- 🔥 **Final alternativo:** ao atingir 100 pontos, o jogador pode encontrar um acampamento misterioso e adquirir o mapa para escapar da floresta.

---

## 🗂️ Estrutura do projeto

- `modulosTimer.py`: módulo com funções auxiliares de pausa (`criar_pausa`, `criar_pausa_maior`).
- `main.py`: código principal com toda a lógica do jogo.
- `statusFinal.txt`: arquivo gerado automaticamente com o **status final do jogador** (vida, energia, pontuação e mochila) ao **vencer** ou **perder** o jogo.

---

## 💾 Salvamento de progresso

Ao final do jogo, os dados do jogador são salvos no arquivo `statusFinal.txt`, localizado na mesma pasta do jogo. Esse registro mostra:

- Situação final (vitória ou derrota);
- Vida restante;
- Energia restante;
- Pontuação alcançada;
- Itens presentes na mochila.
