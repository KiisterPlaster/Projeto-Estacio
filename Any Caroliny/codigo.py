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

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora")

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = tk.Label(app, text="Operações Básicas")
label_titulo_basica.pack()

def calcular_operacao(operacao):
    def executar():
        try:
            resultado = operacao(float(entry_num1.get()), float(entry_num2.get()))
            if resultado is not None:
                messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
            else:
                messagebox.showerror("Erro", "Não é possível dividir por zero.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    frame_operacao = tk.Frame(app)
    frame_operacao.pack()

    label_num1 = tk.Label(frame_operacao, text="Número 1:")
    label_num1.grid(row=0, column=0)
    entry_num1 = tk.Entry(frame_operacao)
    entry_num1.grid(row=0, column=1)

    label_num2 = tk.Label(frame_operacao, text="Número 2:")
    label_num2.grid(row=1, column=0)
    entry_num2 = tk.Entry(frame_operacao)
    entry_num2.grid(row=1, column=1)

    button_calcular = tk.Button(frame_operacao, text="Calcular", command=executar)
    button_calcular.grid(row=2, columnspan=2)

operacoes = [
    ("Soma", soma),
    ("Subtração", subtracao),
    ("Multiplicação", multiplicacao),
    ("Divisão", divisao)
]

for nome, operacao in operacoes:
    button_operacao = tk.Button(app, text=nome, command=lambda operacao=operacao: calcular_operacao(operacao))
    button_operacao.pack()

# Funções avançadas (potenciação, raiz quadrada, raiz n-ésima)
label_titulo_avancada = tk.Label(app, text="Operações Avançadas")
label_titulo_avancada.pack()

def calcular_potencia():
    def executar():
        try:
            resultado = potenciacao(float(entry_base.get()), float(entry_expoente.get()))
            messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    frame_potencia = tk.Frame(app)
    frame_potencia.pack()

    label_base = tk.Label(frame_potencia, text="Base:")
    label_base.grid(row=0, column=0)
    entry_base = tk.Entry(frame_potencia)
    entry_base.grid(row=0, column=1)

    label_expoente = tk.Label(frame_potencia, text="Expoente:")
    label_expoente.grid(row=1, column=0)
    entry_expoente = tk.Entry(frame_potencia)
    entry_expoente.grid(row=1, column=1)

    button_calcular = tk.Button(frame_potencia, text="Calcular", command=executar)
    button_calcular.grid(row=2, columnspan=2)

button_potencia = tk.Button(app, text="Potenciação", command=calcular_potencia)
button_potencia.pack()

def calcular_raiz_quadrada():
    def executar():
        try:
            resultado = raiz_quadrada(float(entry_numero.get()))
            if resultado is not None:
                messagebox.showinfo("Resultado", f"A raiz quadrada é: {resultado}")
            else:
                messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    frame_raiz_quadrada = tk.Frame(app)
    frame_raiz_quadrada.pack()

    label_numero = tk.Label(frame_raiz_quadrada, text="Número:")
    label_numero.grid(row=0, column=0)
    entry_numero = tk.Entry(frame_raiz_quadrada)
    entry_numero.grid(row=0, column=1)

    button_calcular = tk.Button(frame_raiz_quadrada, text="Calcular", command=executar)
    button_calcular.grid(row=1, columnspan=2)

button_raiz_quadrada = tk.Button(app, text="Raiz Quadrada", command=calcular_raiz_quadrada)
button_raiz_quadrada.pack()

def calcular_raiz_n_esima():
    def executar():
        try:
            resultado = raiz_n_esima(float(entry_numero.get()), float(entry_indice.get()))
            if resultado is not None:
                messagebox.showinfo("Resultado", f"A raiz {indice} é: {resultado}")
            else:
                messagebox.showerror("Erro", "Não é possível calcular a raiz de um número negativo para um índice par.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    frame_raiz_n_esima = tk.Frame(app)
    frame_raiz_n_esima.pack()

    label_numero = tk.Label(frame_raiz_n_esima, text="Número:")
    label_numero.grid(row=0, column=0)
    entry_numero = tk.Entry(frame_raiz_n_esima)
    entry_numero.grid(row=0, column=1)

    label_indice = tk.Label(frame_raiz_n_esima, text="Índice:")
    label_indice.grid(row=1, column=0)
    entry_indice = tk.Entry(frame_raiz_n_esima)
    entry_indice.grid(row=1, column=1)

    button_calcular = tk.Button(frame_raiz_n_esima, text="Calcular", command=executar)
    button_calcular.grid(row=2, columnspan=2)

button_raiz_n_esima = tk.Button(app, text="Raiz N-ésima", command=calcular_raiz_n_esima)
button_raiz_n_esima.pack()

app.mainloop()
