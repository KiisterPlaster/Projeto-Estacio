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
def calcular_momento_inercia():
    try:
        largura = float(entry_largura.get())
        altura = float(entry_altura.get())
        resultado = (largura * altura ** 3) / 12
        label_resultado.config(text=f"Momento de inércia calculado: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_esforco_normal():
    try:
        forca = float(entry_forca.get())
        area = float(entry_area.get())
        resultado = forca / area
        label_resultado.config(text=f"Esforço normal calculado: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def mostrar_operacoes_estruturais():
    esconder_todos()
    label_largura.pack()
    entry_largura.pack()
    label_altura.pack()
    entry_altura.pack()
    btn_calcular_momento_inercia.pack()
    label_forca.pack()
    entry_forca.pack()
    label_area.pack()
    entry_area.pack()
    btn_calcular_esforco_normal.pack()
    label_resultado.pack()
    btn_voltar.pack()

btn_operacoes_estruturais = ttk.Button(frame_principal, text="Operações Estruturais", command=mostrar_operacoes_estruturais)
btn_operacoes_estruturais.pack(pady=5, fill=tk.X)

label_largura = ttk.Label(frame_principal, text="Largura (m):")
entry_largura = ttk.Entry(frame_principal)
label_altura = ttk.Label(frame_principal, text="Altura (m):")
entry_altura = ttk.Entry(frame_principal)
btn_calcular_momento_inercia = ttk.Button(frame_principal, text="Calcular Momento de Inércia", command=calcular_momento_inercia)
label_forca = ttk.Label(frame_principal, text="Força (N):")
entry_forca = ttk.Entry(frame_principal)
label_area = ttk.Label(frame_principal, text="Área (m²):")
entry_area = ttk.Entry(frame_principal)
btn_calcular_esforco_normal = ttk.Button(frame_principal, text="Calcular Esforço Normal", command=calcular_esforco_normal)
def calcular_distancia_horizontal():
    try:
        distancia = float(entry_distancia_horizontal.get())
        angulo = float(entry_angulo_inclinacao.get())
        resultado = distancia * math.cos(math.radians(angulo))
        label_resultado.config(text=f"Distância horizontal calculada: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_distancia_vertical():
    try:
        distancia = float(entry_distancia_vertical.get())
        angulo = float(entry_angulo_inclinacao.get())
        resultado = distancia * math.sin(math.radians(angulo))
        label_resultado.config(text=f"Distância vertical calculada: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def mostrar_operacoes_topografia():
    esconder_todos()
    label_distancia_horizontal.pack()
    entry_distancia_horizontal.pack()
    label_distancia_vertical.pack()
    entry_distancia_vertical.pack()
    label_angulo_inclinacao.pack()
    entry_angulo_inclinacao.pack()
    btn_calcular_distancia_horizontal.pack()
    btn_calcular_distancia_vertical.pack()
    label_resultado.pack()
    btn_voltar.pack()

btn_operacoes_topografia = ttk.Button(frame_principal, text="Operações de Topografia", command=mostrar_operacoes_topografia)
btn_operacoes_topografia.pack(pady=5, fill=tk.X)

label_distancia_horizontal = ttk.Label(frame_principal, text="Distância horizontal (m):")
entry_distancia_horizontal = ttk.Entry(frame_principal)
label_distancia_vertical = ttk.Label(frame_principal, text="Distância vertical (m):")
entry_distancia_vertical = ttk.Entry(frame_principal)
label_angulo_inclinacao = ttk.Label(frame_principal, text="Ângulo de inclinação (graus):")
entry_angulo_inclinacao = ttk.Entry(frame_principal)
btn_calcular_distancia_horizontal = ttk.Button(frame_principal, text="Calcular Distância Horizontal", command=calcular_distancia_horizontal)
btn_calcular_distancia_vertical = ttk.Button(frame_principal, text="Calcular Distância Vertical", command=calcular_distancia_vertical)
def calcular_volume_solo():
    try:
        area = float(entry_area_terreno.get())
        profundidade = float(entry_profundidade.get())
        resultado = area * profundidade
        label_resultado.config(text=f"Volume de solo calculado: {resultado} unidades cúbicas")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_peso_solo():
    try:
        volume = float(entry_volume_solo.get())
        densidade = float(entry_densidade_solo.get())
        resultado = volume * densidade
        label_resultado.config(text=f"Peso do solo calculado: {resultado} unidades")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def mostrar_operacoes_mecanica_solo():
    esconder_todos()
    label_area_terreno.pack()
    entry_area_terreno.pack()
    label_profundidade.pack()
    entry_profundidade.pack()
    btn_calcular_volume_solo.pack()
    label_volume_solo.pack()
    entry_volume_solo.pack()
    label_densidade_solo.pack()
    entry_densidade_solo.pack()
    btn_calcular_peso_solo.pack()
    label_resultado.pack()
    btn_voltar.pack()

btn_operacoes_mecanica_solo = ttk.Button(frame_principal, text="Operações de Mecânica dos Solos", command=mostrar_operacoes_mecanica_solo)
btn_operacoes_mecanica_solo.pack(pady=5, fill=tk.X)

label_area_terreno = ttk.Label(frame_principal, text="Área do terreno (m²):")
entry_area_terreno = ttk.Entry(frame_principal)
label_profundidade = ttk.Label(frame_principal, text="Profundidade do solo (m):")
entry_profundidade = ttk.Entry(frame_principal)
btn_calcular_volume_solo = ttk.Button(frame_principal, text="Calcular Volume de Solo", command=calcular_volume_solo)
label_volume_solo = ttk.Label(frame_principal, text="Volume de solo (m³):")
entry_volume_solo = ttk.Entry(frame_principal)
label_densidade_solo = ttk.Label(frame_principal, text="Densidade do solo (kg/m³):")
entry_densidade_solo = ttk.Entry(frame_principal)
btn_calcular_peso_solo = ttk.Button(frame_principal, text="Calcular Peso do Solo", command=calcular_peso_solo)
