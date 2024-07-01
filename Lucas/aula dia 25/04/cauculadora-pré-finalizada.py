import tkinter as tk
from tkinter import messagebox
from math import sqrt

# Funções matemáticas básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return None
    return a / b

def potenciacao(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        return None
    return sqrt(numero)

def raiz_n_esima(numero, indice):
    if numero < 0 and indice % 2 == 0:
        return None
    return numero ** (1 / indice)

# Funções de memória
memoria = {}

def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")

# Funções de Engenharia Civil (implementar de acordo com suas necessidades)
def momento_fletor(forca, distancia, tipo_apoio):
    # Implementar a lógica para calcular o momento fletor
    pass

def cortante(forca, distancia, tipo_apoio):
    # Implementar a lógica para calcular o cortante
    pass

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app)
aba_avancada = tk.Frame(app)
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack()

# ... (interfaces para as funções básicas: soma, subtração, multiplicação, divisão)

# Funções avançadas (potenciação, raiz quadrada, raiz n-ésima)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# ... (interfaces para as funções avançadas: potenciação, raiz quadrada, raiz n-ésima)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")
label_titulo_engenharia_civil.pack()

# ... (interfaces para as funções de engenharia civil)

app.mainloop()
