import tkinter as tk
from tkinter import ttk
import os

# Função para abrir os arquivos correspondentes
def abrir_arquivo(nome_arquivo):
    os.system(f"start {nome_arquivo}")

# Função para mostrar a tela inicial
def mostrar_tela_inicial():
    aba_operacoes.pack_forget()
    tela_inicial.pack(side="top", fill="both", expand=True)

# Função para mostrar a aba de operações
def mostrar_aba_operacoes():
    tela_inicial.pack_forget()
    aba_operacoes.pack(side="top", fill="both", expand=True)

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")

# Definindo o tamanho fixo da janela principal
app.geometry("400x600")  # Tamanho ajustado para caber na tela

# Definindo as cores
cor_fundo = "#E6E6FA"  # Lilás claro
cor_botao = "#D8BFD8"  # Lilás mais escuro
cor_texto_botao = "#000000"  # Cor do texto dos botões (preto)

# Configurando a cor de fundo das janelas principais
app.configure(bg=cor_fundo)

# Tela inicial
tela_inicial = tk.Frame(app, bg=cor_fundo)
tela_inicial.pack(side="top", fill="both", expand=True)

titulo = tk.Label(tela_inicial, text="Calculadora Avançada", font=("Helvetica", 16), bg=cor_fundo, fg=cor_texto_botao)
titulo.pack(pady=20)

botao_entrar = ttk.Button(tela_inicial, text="Entrar", command=mostrar_aba_operacoes)
botao_entrar.pack(pady=10)

# Aba de operações com rolagem
aba_operacoes = tk.Frame(app, bg=cor_fundo)
canvas = tk.Canvas(aba_operacoes, bg=cor_fundo)
scrollbar = tk.Scrollbar(aba_operacoes, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=cor_fundo)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Botão de voltar
botao_voltar = ttk.Button(scrollable_frame, text="Voltar", command=mostrar_tela_inicial)
botao_voltar.pack(pady=5)

# Lista de arquivos
arquivos = [
    "derivadanumerica.py",
    "divisao_interface.py",
    "engenhariacivil.py",
    "funcionalidadesbasicas.py",
    "funcionalidadesdememoria.py",
    "funcoesbasicas.py",
    "funcoesdeeng_civil.py",
    "funcoesdememoria.py",
    "funcoesmatematicas.py",
    "igc_momentofletor.py",
    "integracaonumerica.py",
    "interfaceprincipal.py",
    "matematicasbasicas.py",
    "operacoesbasicas.py",
    "operacoescommemoria.py",
    "operacoescompotencias.py",
    "potenciacaoeradiciacao.py"
]

# Organizando a lista em ordem alfabética
arquivos.sort()

# Configurando o estilo do ttk
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat",
                background=cor_botao, foreground=cor_texto_botao)
style.map("TButton",
          background=[('active', cor_botao)],
          relief=[('pressed', 'flat')],
          focuscolor=[('focus', cor_fundo)],
          bordercolor=[('focus', cor_botao)],
          highlightcolor=[('focus', cor_botao)])

# Criando botões para cada arquivo de operações e organizando verticalmente
for arquivo in arquivos:
    botao = ttk.Button(scrollable_frame, text=arquivo, command=lambda arq=arquivo: abrir_arquivo(arq), style="TButton")
    botao.pack(pady=5)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Configurando layout da aba de operações
aba_operacoes.pack(side="top", fill="both", expand=True)

# Iniciando a interface gráfica
app.mainloop()
