import tkinter as tk
from tkinter import messagebox
import math

# Funções para operações básicas
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

# Funções matemáticas
def seno(a):
    return math.sin(a)

def cosseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

def logaritmo_natural(a):
    if a <= 0:
        return "Erro: Logaritmo de valor não positivo"
    return math.log(a)

def logaritmo_decimal(a):
    if a <= 0:
        return "Erro: Logaritmo de valor não positivo"
    return math.log10(a)

# Função para criar a tela inicial
def tela_inicial():
    limpar_janela()
    titulo = tk.Label(janela, text="Calculadora", font=("Arial", 24))
    titulo.pack(pady=20)
    
    botao_operacoes_basicas = tk.Button(janela, text="Operações Básicas", font=("Arial", 18), command=tela_operacoes_basicas)
    botao_operacoes_basicas.pack(pady=10)
    
    botao_funcoes_matematicas = tk.Button(janela, text="Funções Matemáticas", font=("Arial", 18), command=tela_funcoes_matematicas)
    botao_funcoes_matematicas.pack(pady=10)
    
# Função para criar a tela de operações básicas
def tela_operacoes_basicas():
    limpar_janela()
    
    label_a = tk.Label(janela, text="Valor A", font=("Arial", 14))
    label_a.pack()
    entrada_a = tk.Entry(janela, font=("Arial", 14))
    entrada_a.pack()
    
    label_b = tk.Label(janela, text="Valor B", font=("Arial", 14))
    label_b.pack()
    entrada_b = tk.Entry(janela, font=("Arial", 14))
    entrada_b.pack()
    
    def realizar_operacao(operacao):
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            if operacao == "soma":
                resultado = adicionar(a, b)
            elif operacao == "subtracao":
                resultado = subtrair(a, b)
            elif operacao == "multiplicacao":
                resultado = multiplicar(a, b)
            elif operacao == "divisao":
                resultado = dividir(a, b)
            messagebox.showinfo("Resultado", f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    
    botao_soma = tk.Button(janela, text="Somar", font=("Arial", 14), command=lambda: realizar_operacao("soma"))
    botao_soma.pack(pady=5)
    
    botao_subtracao = tk.Button(janela, text="Subtrair", font=("Arial", 14), command=lambda: realizar_operacao("subtracao"))
    botao_subtracao.pack(pady=5)
    
    botao_multiplicacao = tk.Button(janela, text="Multiplicar", font=("Arial", 14), command=lambda: realizar_operacao("multiplicacao"))
    botao_multiplicacao.pack(pady=5)
    
    botao_divisao = tk.Button(janela, text="Dividir", font=("Arial", 14), command=lambda: realizar_operacao("divisao"))
    botao_divisao.pack(pady=5)
    
    botao_voltar = tk.Button(janela, text="Voltar", font=("Arial", 14), command=tela_inicial)
    botao_voltar.pack(pady=20)

# Função para criar a tela de funções matemáticas
def tela_funcoes_matematicas():
    limpar_janela()
    
    label_a = tk.Label(janela, text="Valor", font=("Arial", 14))
    label_a.pack()
    entrada_a = tk.Entry(janela, font=("Arial", 14))
    entrada_a.pack()
    
    def realizar_funcao(funcao):
        try:
            a = float(entrada_a.get())
            if funcao == "seno":
                resultado = seno(a)
            elif funcao == "cosseno":
                resultado = cosseno(a)
            elif funcao == "tangente":
                resultado = tangente(a)
            elif funcao == "log_natural":
                resultado = logaritmo_natural(a)
            elif funcao == "log_decimal":
                resultado = logaritmo_decimal(a)
            messagebox.showinfo("Resultado", f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
    
    botao_seno = tk.Button(janela, text="Seno", font=("Arial", 14), command=lambda: realizar_funcao("seno"))
    botao_seno.pack(pady=5)
    
    botao_cosseno = tk.Button(janela, text="Cosseno", font=("Arial", 14), command=lambda: realizar_funcao("cosseno"))
    botao_cosseno.pack(pady=5)
    
    botao_tangente = tk.Button(janela, text="Tangente", font=("Arial", 14), command=lambda: realizar_funcao("tangente"))
    botao_tangente.pack(pady=5)
    
    botao_log_natural = tk.Button(janela, text="Logaritmo Natural", font=("Arial", 14), command=lambda: realizar_funcao("log_natural"))
    botao_log_natural.pack(pady=5)
    
    botao_log_decimal = tk.Button(janela, text="Logaritmo Decimal", font=("Arial", 14), command=lambda: realizar_funcao("log_decimal"))
    botao_log_decimal.pack(pady=5)
    
    botao_voltar = tk.Button(janela, text="Voltar", font=("Arial", 14), command=tela_inicial)
    botao_voltar.pack(pady=20)

# Função para limpar a janela
def limpar_janela():
    for widget in janela.winfo_children():
        widget.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Básica")
janela.geometry("400x400")

# Exibir a tela inicial
tela_inicial()

# Executar o loop principal da janela
janela.mainloop()
