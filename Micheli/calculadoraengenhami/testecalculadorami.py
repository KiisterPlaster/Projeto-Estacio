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
def mostrar_operacoes_combinacao_permutacao():
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
    btn_converter_celsius_fahrenheit.pack()
    label_fahrenheit.pack()
    entry_fahrenheit.pack()
    btn_converter_fahrenheit_celsius.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para esconder todos os widgets
def esconder_todos():
    for widget in frame_principal.pack_slaves():
        widget.pack_forget()

# Função para mostrar a interface principal
def mostrar_interface_principal():
    esconder_todos()
    label_titulo.pack(pady=20)
    btn_operacoes_basicas.pack(pady=5, fill=tk.X)
    btn_radiciacao_potenciacao.pack(pady=5, fill=tk.X)
    btn_funcoes_matematicas.pack(pady=5, fill=tk.X)
    btn_operacoes_engenharia.pack(pady=5, fill=tk.X)
    btn_integracao_numerica.pack(pady=5, fill=tk.X)
    btn_combinacao_permutacao.pack(pady=5, fill=tk.X)
    btn_conversao_unidades.pack(pady=5, fill=tk.X)

# Criação da interface principal
root = tk.Tk()
root.title("Calculadora Avançada")

style = ttk.Style()
style.theme_use('clam')

# Configuração de cores e estilos
style.configure("TButton",
                font=("Arial", 10, "bold"),
                foreground="#333333",
                background="#ffffff",
                borderwidth=2,
                relief="raised",
                padding=5)

# Estilo personalizado para o frame principal
frame_principal = ttk.Frame(root, padding="20")
frame_principal.pack(expand=True, fill=tk.BOTH)

label_titulo = ttk.Label(frame_principal, text="Calculadora Avançada", font=("Arial", 20, "bold"))
label_titulo.pack(pady=20)

btn_operacoes_basicas = ttk.Button(frame_principal, text="Operações Básicas", command=mostrar_operacoes_basicas)
btn_radiciacao_potenciacao = ttk.Button(frame_principal, text="Radiciação e Potenciação", command=mostrar_radiciacao_potenciacao)
btn_funcoes_matematicas = ttk.Button(frame_principal, text="Funções Matemáticas", command=mostrar_funcoes_matematicas)
btn_operacoes_engenharia = ttk.Button(frame_principal, text="Operações de Engenharia", command=mostrar_operacoes_engenharia)
btn_integracao_numerica = ttk.Button(frame_principal, text="Integração Numérica", command=mostrar_integracao_numerica)
btn_combinacao_permutacao = ttk.Button(frame_principal, text="Combinação e Permutação", command=mostrar_operacoes_combinacao_permutacao)
btn_conversao_unidades = ttk.Button(frame_principal, text="Conversão de Unidades", command=mostrar_conversao_unidades)

btn_operacoes_basicas.pack(pady=5, fill=tk.X)
btn_radiciacao_potenciacao.pack(pady=5, fill=tk.X)
btn_funcoes_matematicas.pack(pady=5, fill=tk.X)
btn_operacoes_engenharia.pack(pady=5, fill=tk.X)
btn_integracao_numerica.pack(pady=5, fill=tk.X)
btn_combinacao_permutacao.pack(pady=5, fill=tk.X)
btn_conversao_unidades.pack(pady=5, fill=tk.X)

# Inicialização de widgets comuns para diversas interfaces
label_num1 = ttk.Label(frame_principal, text="Número 1:")
entry_num1 = ttk.Entry(frame_principal)
label_num2 = ttk.Label(frame_principal, text="Número 2:")
entry_num2 = ttk.Entry(frame_principal)
btn_somar = ttk.Button(frame_principal, text="Somar", command=somar)
btn_subtrair = ttk.Button(frame_principal, text="Subtrair", command=subtrair)
btn_multiplicar = ttk.Button(frame_principal, text="Multiplicar", command=multiplicar)
btn_dividir = ttk.Button(frame_principal, text="Dividir", command=dividir)

label_base = ttk.Label(frame_principal, text="Base:")
entry_base = ttk.Entry(frame_principal)
label_expoente = ttk.Label(frame_principal, text="Expoente:")
entry_expoente = ttk.Entry(frame_principal)
btn_potencia = ttk.Button(frame_principal, text="Calcular Potência", command=potencia)
label_valor = ttk.Label(frame_principal, text="Valor para Radiciação:")
entry_valor = ttk.Entry(frame_principal)
btn_radiciacao = ttk.Button(frame_principal, text="Calcular Raiz Quadrada", command=radiciacao)

label_angulo = ttk.Label(frame_principal, text="Ângulo (graus):")
entry_angulo = ttk.Entry(frame_principal)
btn_seno = ttk.Button(frame_principal, text="Calcular Seno", command=seno)
btn_cosseno = ttk.Button(frame_principal, text="Calcular Cosseno", command=cosseno)
btn_tangente = ttk.Button(frame_principal, text="Calcular Tangente", command=tangente)
label_valor_log = ttk.Label(frame_principal, text="Valor para Logaritmo:")
entry_valor_log = ttk.Entry(frame_principal)
btn_logaritmo_natural = ttk.Button(frame_principal, text="Logaritmo Natural", command=logaritmo_natural)
btn_logaritmo_decimal = ttk.Button(frame_principal, text="Logaritmo Decimal", command=logaritmo_decimal)

label_carga = ttk.Label(frame_principal, text="Carga:")
entry_carga = ttk.Entry(frame_principal)
label_distancia = ttk.Label(frame_principal, text="Distância:")
entry_distancia = ttk.Entry(frame_principal)
btn_calcular_momento_fletor = ttk.Button(frame_principal, text="Calcular Momento Fletor", command=calcular_momento_fletor)

label_limite_inf = ttk.Label(frame_principal, text="Limite Inferior:")
entry_limite_inf = ttk.Entry(frame_principal)
label_limite_sup = ttk.Label(frame_principal, text="Limite Superior:")
entry_limite_sup = ttk.Entry(frame_principal)
label_num_segmentos = ttk.Label(frame_principal, text="Número de Segmentos:")
entry_num_segmentos = ttk.Entry(frame_principal)
btn_calcular_integral = ttk.Button(frame_principal, text="Calcular Integral", command=calcular_integral)

label_numero_fatorial = ttk.Label(frame_principal, text="Número para Fatorial:")
entry_numero_fatorial = ttk.Entry(frame_principal)
btn_calcular_fatorial = ttk.Button(frame_principal, text="Calcular Fatorial", command=calcular_fatorial)
label_n_combinacao = ttk.Label(frame_principal, text="n (Combinação):")
entry_n_combinacao = ttk.Entry(frame_principal)
label_k_combinacao = ttk.Label(frame_principal, text="k (Combinação):")
entry_k_combinacao = ttk.Entry(frame_principal)
btn_calcular_combinacao = ttk.Button(frame_principal, text="Calcular Combinação", command=calcular_combinacao)
label_n_permutacao = ttk.Label(frame_principal, text="n (Permutação):")
entry_n_permutacao = ttk.Entry(frame_principal)
entry_k_permutacao = ttk.Entry(frame_principal)
btn_calcular_permutacao = ttk.Button(frame_principal, text="Calcular Permutação", command=calcular_permutacao)

btn_voltar = ttk.Button(frame_principal, text="Voltar", command=lambda: esconder_todos() or mostrar_interface_principal())

label_celsius = ttk.Label(frame_principal, text="Celsius:")
entry_celsius = ttk.Entry(frame_principal)
btn_converter_celsius_fahrenheit = ttk.Button(frame_principal, text="Converter para Fahrenheit", command=converter_celsius_para_fahrenheit)
label_fahrenheit = ttk.Label(frame_principal, text="Fahrenheit:")
entry_fahrenheit = ttk.Entry(frame_principal)
btn_converter_fahrenheit_celsius = ttk.Button(frame_principal, text="Converter para Celsius", command=converter_fahrenheit_para_celsius)

label_resultado = ttk.Label(frame_principal, text="Resultado:")
btn_voltar = ttk.Button(frame_principal, text="Voltar", command=lambda: esconder_todos() or mostrar_interface_principal())

mostrar_interface_principal()
root.mainloop()
