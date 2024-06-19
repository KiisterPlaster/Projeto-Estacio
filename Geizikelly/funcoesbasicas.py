import tkinter as tk
from tkinter import ttk

def soma_interface(entrada_a, entrada_b):
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        resultado = a + b
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado_soma.config(text="Entrada inválida. Digite números válidos.")

def criar_interface():
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Calculadora")

    # Criando abas para organizar as funcionalidades
    notebook = ttk.Notebook(janela)
    notebook.pack(padx=10, pady=10)

    # Aba para funções básicas
    aba_basica = tk.Frame(notebook)
    notebook.add(aba_basica, text="Funções Básicas")

    label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
    label_titulo_basica.pack()

    label_a_soma = tk.Label(aba_basica, text="Valor de a:")
    label_a_soma.pack()
    entrada_a_soma = tk.Entry(aba_basica)
    entrada_a_soma.pack()

    label_b_soma = tk.Label(aba_basica, text="Valor de b:")
    label_b_soma.pack()
    entrada_b_soma = tk.Entry(aba_basica)
    entrada_b_soma.pack()

    botao_somar = tk.Button(aba_basica, text="Somar", command=lambda: soma_interface(entrada_a_soma, entrada_b_soma))
    botao_somar.pack()

    global label_resultado_soma
    label_resultado_soma = tk.Label(aba_basica, text="Resultado:")
    label_resultado_soma.pack()

    # Aba para funções avançadas (exemplo de label)
    aba_avancada = tk.Frame(notebook)
    notebook.add(aba_avancada, text="Funções Avançadas")

    label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
    label_titulo_avancada.pack()

    # Aba para funções de memória (exemplo de label)
    aba_memoria = tk.Frame(notebook)
    notebook.add(aba_memoria, text="Memória")

    label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
    label_titulo_memoria.pack()

    # Aba para funções de Engenharia Civil (exemplo de label)
    aba_engenharia_civil = tk.Frame(notebook)
    notebook.add(aba_engenharia_civil, text="Engenharia Civil")

    label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")
    label_titulo_engenharia_civil.pack()

    # Executando a aplicação
    janela.mainloop()

# Chamando a função para criar a interface
criar_interface()
