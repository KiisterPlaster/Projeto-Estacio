import tkinter as tk
from tkinter import messagebox, ttk
import math

# Funções para operações básicas
def somar():
    calcular_operacao(lambda num1, num2: num1 + num2)

def subtrair():
    calcular_operacao(lambda num1, num2: num1 - num2)

def multiplicar():
    calcular_operacao(lambda num1, num2: num1 * num2)

def dividir():
    calcular_operacao(lambda num1, num2: num1 / num2 if num2 != 0 else "Divisão por zero não permitida!")

def calcular_operacao(operacao):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = operacao(num1, num2)
        if resultado == "Divisão por zero não permitida!":
            messagebox.showerror("Erro", resultado)
        else:
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações de potenciação e radiciação
def potencia():
    try:
        base = float(entry_base.get())
        expoente = float(entry_expoente.get())
        resultado = base ** expoente
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def radiciacao():
    try:
        valor = float(entry_valor.get())
        if valor < 0:
            messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo!")
            return
        resultado = math.sqrt(valor)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações matemáticas avançadas
def seno():
    calcular_funcao_trigonometrica(math.sin)

def cosseno():
    calcular_funcao_trigonometrica(math.cos)

def tangente():
    calcular_funcao_trigonometrica(math.tan)

def calcular_funcao_trigonometrica(funcao):
    try:
        angulo = float(entry_angulo.get())
        resultado = funcao(math.radians(angulo))
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def logaritmo_natural():
    calcular_logaritmo(math.log)

def logaritmo_decimal():
    calcular_logaritmo(math.log10)

def calcular_logaritmo(funcao):
    try:
        valor = float(entry_valor_log.get())
        if valor <= 0:
            messagebox.showerror("Erro", "O logaritmo de um valor menor ou igual a zero não é definido!")
            return
        resultado = funcao(valor)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações de engenharia
def calcular_momento_fletor():
    try:
        carga = float(entry_carga.get())
        distancia = float(entry_distancia.get())
        resultado = carga * distancia ** 2 / 2
        label_resultado.config(text=f"Momento fletor calculado: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_momento_fletor_engastada():
    try:
        carga = float(entry_carga_engastada.get())
        comprimento = float(entry_comprimento_engastada.get())
        resultado = (carga * comprimento ** 2) / 8
        label_resultado.config(text=f"Momento fletor (engastada): {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações de integração numérica
def calcular_integral():
    try:
        limite_inf = float(entry_limite_inf.get())
        limite_sup = float(entry_limite_sup.get())
        num_segmentos = int(entry_num_segmentos.get())
        
        # Cálculo da integral numérica (método dos trapézios)
        h = (limite_sup - limite_inf) / num_segmentos
        x = limite_inf
        integral = 0
        for _ in range(num_segmentos):
            integral += (math.sin(x) + math.sin(x + h)) * h / 2
            x += h
        
        label_resultado.config(text=f"Integral calculada: {integral}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações de fatorial, combinação e permutação
def calcular_fatorial():
    try:
        numero = int(entry_numero_fatorial.get())
        resultado = math.factorial(numero)
        label_resultado.config(text=f"Fatorial de {numero}: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_combinacao():
    try:
        n = int(entry_n_combinacao.get())
        k = int(entry_k_combinacao.get())
        resultado = math.comb(n, k)
        label_resultado.config(text=f"Combinação C({n}, {k}): {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_permutacao():
    try:
        n = int(entry_n_permutacao.get())
        k = int(entry_k_permutacao.get())
        resultado = math.perm(n, k)
        label_resultado.config(text=f"Permutação P({n}, {k}): {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para conversão de unidades
def converter_celsius_para_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_resultado.config(text=f"{celsius}°C é equivalente a {fahrenheit}°F")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def converter_fahrenheit_para_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_resultado.config(text=f"{fahrenheit}°F é equivalente a {celsius}°C")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Função para exibir a interface de operações básicas
def mostrar_operacoes_basicas():
    esconder_todos()
    label_num1.pack()
    entry_num1.pack()
    label_num2.pack()
    entry_num2.pack()
    btn_somar.pack()
    btn_subtrair.pack()
    btn_multiplicar.pack()
    btn_dividir.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de radiciação e potenciação
def mostrar_radiciacao_potenciacao():
    esconder_todos()
    label_base.pack()
    entry_base.pack()
    label_expoente.pack()
    entry_expoente.pack()
    btn_potencia.pack()
    label_valor.pack()
    entry_valor.pack()
    btn_radiciacao.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de operações matemáticas
def mostrar_funcoes_matematicas():
    esconder_todos()
    label_angulo.pack()
    entry_angulo.pack()
    btn_seno.pack()
    btn_cosseno.pack()
    btn_tangente.pack()
    label_valor_log.pack()
    entry_valor_log.pack()
    btn_logaritmo_natural.pack()
    btn_logaritmo_decimal.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de operações de engenharia
def mostrar_operacoes_engenharia():
    esconder_todos()
    label_carga.pack()
    entry_carga.pack()
    label_distancia.pack()
    entry_distancia.pack()
    btn_calcular_momento_fletor.pack()
    label_carga_engastada.pack()
    entry_carga_engastada.pack()
    label_comprimento_engastada.pack()
    entry_comprimento_engastada.pack()
    btn_calcular_momento_fletor_engastada.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de integração numérica
def mostrar_integracao_numerica():
    esconder_todos()
    label_limite_inf.pack()
    entry_limite_inf.pack()
    label_limite_sup.pack()
    entry_limite_sup.pack()
    label_num_segmentos.pack()
    entry_num_segmentos.pack()
    btn_calcular_integral.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de operações de fatorial, combinação e permutação
def mostrar_fatorial_combinacao_permutacao():
    esconder_todos()
    label_numero_fatorial.pack()
    entry_numero_fatorial.pack()
    btn_calcular_fatorial.pack()
    label_n_combinacao.pack()
    entry_n_combinacao.pack()
    label_k_combinacao.pack()
    entry_k_combinacao.pack()
    btn_calcular_combinacao.pack()
    label_n_permutacao.pack()
    entry_n_permutacao.pack()
    label_k_permutacao.pack()
    entry_k_permutacao.pack()
    btn_calcular_permutacao.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de conversão de unidades
def mostrar_conversao_unidades():
    esconder_todos()
    label_celsius.pack()
    entry_celsius.pack()
    btn_converter_celsius.pack()
    label_fahrenheit.pack()
    entry_fahrenheit.pack()
    btn_converter_fahrenheit.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para esconder todos os widgets
def esconder_todos():
    for widget in janela.winfo_children():
        widget.pack_forget()

# Configuração da interface principal
janela = tk.Tk()
janela.title("Calculadora Completa")

# Widgets comuns
label_resultado = tk.Label(janela, text="Resultado:", font=("Arial", 14))
btn_voltar = tk.Button(janela, text="Voltar", command=lambda: mostrar_menu())

# Widgets para operações básicas
label_num1 = tk.Label(janela, text="Número 1:")
entry_num1 = tk.Entry(janela)
label_num2 = tk.Label(janela, text="Número 2:")
entry_num2 = tk.Entry(janela)
btn_somar = tk.Button(janela, text="Somar", command=somar)
btn_subtrair = tk.Button(janela, text="Subtrair", command=subtrair)
btn_multiplicar = tk.Button(janela, text="Multiplicar", command=multiplicar)
btn_dividir = tk.Button(janela, text="Dividir", command=dividir)

# Widgets para radiciação e potenciação
label_base = tk.Label(janela, text="Base:")
entry_base = tk.Entry(janela)
label_expoente = tk.Label(janela, text="Expoente:")
entry_expoente = tk.Entry(janela)
btn_potencia = tk.Button(janela, text="Potência", command=potencia)
label_valor = tk.Label(janela, text="Valor:")
entry_valor = tk.Entry(janela)
btn_radiciacao = tk.Button(janela, text="Radiciação", command=radiciacao)

# Widgets para operações matemáticas
label_angulo = tk.Label(janela, text="Ângulo (em graus):")
entry_angulo = tk.Entry(janela)
btn_seno = tk.Button(janela, text="Seno", command=seno)

btn_tangente = tk.Button(janela, text="Tangente", command=tangente)
label_valor_log = tk.Label(janela, text="Valor:")
entry_valor_log = tk.Entry(janela)
btn_logaritmo_natural = tk.Button(janela, text="Logaritmo Natural", command=logaritmo_natural)
btn_logaritmo_decimal = tk.Button(janela, text="Logaritmo Decimal", command=logaritmo_decimal)

# Widgets para operações de engenharia
label_carga = tk.Label(janela, text="Carga (N):")
entry_carga = tk.Entry(janela)
label_distancia = tk.Label(janela, text="Distância (m):")
entry_distancia = tk.Entry(janela)
btn_calcular_momento_fletor = tk.Button(janela, text="Calcular Momento Fletor", command=calcular_momento_fletor)
label_carga_engastada = tk.Label(janela, text="Carga (N):")
entry_carga_engastada = tk.Entry(janela)
label_comprimento_engastada = tk.Label(janela, text="Comprimento (m):")
entry_comprimento_engastada = tk.Entry(janela)
btn_calcular_momento_fletor_engastada = tk.Button(janela, text="Calcular Momento Fletor (Engastada)", command=calcular_momento_fletor_engastada)

# Widgets para integração numérica
label_limite_inf = tk.Label(janela, text="Limite Inferior:")
entry_limite_inf = tk.Entry(janela)
label_limite_sup = tk.Label(janela, text="Limite Superior:")
entry_limite_sup = tk.Entry(janela)
label_num_segmentos = tk.Label(janela, text="Número de Segmentos:")
entry_num_segmentos = tk.Entry(janela)
btn_calcular_integral = tk.Button(janela, text="Calcular Integral", command=calcular_integral)

# Widgets para operações de fatorial, combinação e permutação
label_numero_fatorial = tk.Label(janela, text="Número:")
entry_numero_fatorial = tk.Entry(janela)
btn_calcular_fatorial = tk.Button(janela, text="Calcular Fatorial", command=calcular_fatorial)
label_n_combinacao = tk.Label(janela, text="n:")
entry_n_combinacao = tk.Entry(janela)
label_k_combinacao = tk.Label(janela, text="k:")
entry_k_combinacao = tk.Entry(janela)
btn_calcular_combinacao = tk.Button(janela, text="Calcular Combinação", command=calcular_combinacao)
label_n_permutacao = tk.Label(janela, text="n:")
entry_n_permutacao = tk.Entry(janela)
label_k_permutacao = tk.Label(janela, text="k:")
entry_k_permutacao = tk.Entry(janela)
btn_calcular_permutacao = tk.Button(janela, text="Calcular Permutação", command=calcular_permutacao)

# Widgets para conversão de unidades
label_celsius = tk.Label(janela, text="Temperatura em °C:")
entry_celsius = tk.Entry(janela)
btn_converter_celsius = tk.Button(janela, text="Converter para °F", command=converter_celsius_para_fahrenheit)
label_fahrenheit = tk.Label(janela, text="Temperatura em °F:")
entry_fahrenheit = tk.Entry(janela)
btn_converter_fahrenheit = tk.Button(janela, text="Converter para °C", command=converter_fahrenheit_para_celsius)

# Função para exibir o menu principal
def mostrar_menu():
    esconder_todos()
    btn_operacoes_basicas.pack()
    btn_radiciacao_potenciacao.pack()
    btn_funcoes_matematicas.pack()
    btn_operacoes_engenharia.pack()
    btn_integracao_numerica.pack()
    btn_fatorial_combinacao_permutacao.pack()
    btn_conversao_unidades.pack()

# Botões do menu principal
btn_operacoes_basicas = tk.Button(janela, text="Operações Básicas", command=mostrar_operacoes_basicas)
btn_radiciacao_potenciacao = tk.Button(janela, text="Radiciação e Potenciação", command=mostrar_radiciacao_potenciacao)
btn_funcoes_matematicas = tk.Button(janela, text="Funções Matemáticas", command=mostrar_funcoes_matematicas)
btn_operacoes_engenharia = tk.Button(janela, text="Operações de Engenharia", command=mostrar_operacoes_engenharia)
btn_integracao_numerica = tk.Button(janela, text="Integração Numérica", command=mostrar_integracao_numerica)
btn_fatorial_combinacao_permutacao = tk.Button(janela, text="Fatorial, Combinação e Permutação", command=mostrar_fatorial_combinacao_permutacao)
btn_conversao_unidades = tk.Button(janela, text="Conversão de Unidades", command=mostrar_conversao_unidades)

# Exibir o menu principal
mostrar_menu()

# Iniciar a aplicação
janela.mainloop()
