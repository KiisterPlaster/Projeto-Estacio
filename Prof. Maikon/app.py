import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from op import operacoes_basicas, potenciacao_radiciacao, funcoes_matematicas, memoria, integracao_derivacao

def show_splash():
    splash_root = tk.Toplevel()
    splash_root.overrideredirect(True)  # Remove a barra de título da janela
    splash_root.geometry("800x600+{}+{}".format((splash_root.winfo_screenwidth() // 2) - 400, (splash_root.winfo_screenheight() // 2) - 300))

    # Obtém o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Carrega o ícone a partir do arquivo de imagem
    icon_path = os.path.join(current_dir, "images/icon.png")
    icon_image = Image.open(icon_path).convert("RGBA")  # Garantir que a imagem tem canal alfa para transparência
    icon = ImageTk.PhotoImage(icon_image)
    icon_label = tk.Label(splash_root, image=icon, bg='white')  # Define o fundo como branco para transparência
    icon_label.image = icon  # Mantém a referência para evitar coleta de lixo
    icon_label.pack(pady=100)

    # Define um atraso antes de fechar a tela de splash e iniciar a janela principal
    def close_splash():
        splash_root.destroy()
        start_main_window()

    splash_root.after(5000, close_splash)

# Função para inicializar a janela principal
def start_main_window():
    root = tk.Tk()
    root.title("Calculadora de Engenharia")
    root.geometry("800x600")

    # Obtém o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Carrega o ícone a partir do arquivo de imagem
    icon_path = os.path.join(current_dir, "images/icon.png")
    icon_image = Image.open(icon_path).convert("RGBA")  # Garantir que a imagem tem canal alfa para transparência
    icon = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon)

    # Configura o estilo dos botões
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10)

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Cria a tela inicial com botões para selecionar a função
    inicio_frame = ttk.Frame(notebook)
    notebook.add(inicio_frame, text='Início')

    btn_operacoes_basicas = ttk.Button(inicio_frame, text="Operações Básicas", command=lambda: operacoes_basicas.OperacoesBasicasGUI(root))
    btn_operacoes_basicas.pack(pady=10)

    btn_potenciacao_radiciacao = ttk.Button(inicio_frame, text="Potenciação e Radiciação", command=lambda: potenciacao_radiciacao.PotenciacaoRadiciacaoGUI(root))
    btn_potenciacao_radiciacao.pack(pady=10)

    btn_funcoes_matematicas = ttk.Button(inicio_frame, text="Funções Matemáticas", command=lambda: funcoes_matematicas.FuncoesMatematicasGUI(root))
    btn_funcoes_matematicas.pack(pady=10)

    btn_memoria = ttk.Button(inicio_frame, text="Operações com Memória", command=lambda: memoria.MemoriaGUI(root))
    btn_memoria.pack(pady=10)

    btn_integracao_derivacao = ttk.Button(inicio_frame, text="Integração e Derivação", command=lambda: integracao_derivacao.IntegracaoDerivacaoGUI(root))
    btn_integracao_derivacao.pack(pady=10)

    root.mainloop()

# Inicializa a janela principal antes da tela de splash
root = tk.Tk()
root.withdraw()  # Oculta a janela principal durante a exibição da tela de splash

# Exibe a tela de splash
show_splash()

# Mantém a referência da janela principal para evitar coleta de lixo prematura
root.mainloop()
