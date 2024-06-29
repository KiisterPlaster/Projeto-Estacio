import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import operacoes_basicas
import potenciacao_radiciacao
import funcoes_matematicas
import memoria
import integracao_derivacao

# Função para exibir a tela de operações básicas
def show_operacoes_basicas():
    operacoes_basicas.OperacoesBasicasGUI(root)

# Função para exibir a tela de potenciação e radiciação
def show_potenciacao_radiciacao():
    potenciacao_radiciacao.PotenciacaoRadiciacaoGUI(root)

# Função para exibir a tela de funções matemáticas
def show_funcoes_matematicas():
    funcoes_matematicas.FuncoesMatematicasGUI(root)

# Função para exibir a tela de operações com memória
def show_memoria():
    memoria.MemoriaGUI(root)

# Função para exibir a tela de integração e derivação
def show_integracao_derivacao():
    integracao_derivacao.IntegracaoDerivacaoGUI(root)

# Função para exibir a tela de splash
def show_splash():
    splash_root = tk.Toplevel(root)
    splash_root.overrideredirect(True)  # Remove a barra de título da janela

    # Carrega o ícone a partir do arquivo de imagem
    icon = ImageTk.PhotoImage(Image.open("images/icon.png"))
    icon_label = tk.Label(splash_root, image=icon)
    icon_label.pack(pady=20)

    # Define um atraso antes de fechar a tela de splash
    splash_root.after(2000, splash_root.destroy)

root = tk.Tk()
root.title("Calculadora de Engenharia")

# Carrega o ícone a partir do arquivo de imagem
icon = ImageTk.PhotoImage(Image.open("images/icon.png"))
root.iconphoto(False, icon)

# Configura o estilo dos botões
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Cria a tela inicial com botões para selecionar a função
inicio_frame = ttk.Frame(notebook)
notebook.add(inicio_frame, text='Início')

btn_operacoes_basicas = ttk.Button(inicio_frame, text="Operações Básicas", command=show_operacoes_basicas, style="TButton")
btn_operacoes_basicas.pack(pady=10)

btn_potenciacao_radiciacao = ttk.Button(inicio_frame, text="Potenciação e Radiciação", command=show_potenciacao_radiciacao, style="TButton")
btn_potenciacao_radiciacao.pack(pady=10)

btn_funcoes_matematicas = ttk.Button(inicio_frame, text="Funções Matemáticas", command=show_funcoes_matematicas, style="TButton")
btn_funcoes_matematicas.pack(pady=10)

btn_memoria = ttk.Button(inicio_frame, text="Operações com Memória", command=show_memoria, style="TButton")
btn_memoria.pack(pady=10)

btn_integracao_derivacao = ttk.Button(inicio_frame, text="Integração e Derivação", command=show_integracao_derivacao, style="TButton")
btn_integracao_derivacao.pack(pady=10)

# Exibe a tela de splash antes da janela principal
show_splash()

root.mainloop()