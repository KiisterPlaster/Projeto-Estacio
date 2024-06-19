import tkinter as tk
from tkinter import messagebox
import math
import numpy as np

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

# Funções para operações matemáticas
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

def calcular_transformada_fourier():
    try:
        valores = list(map(float, entry_valores_fourier.get().split(',')))
        resultado = np.fft.fft(valores)
        label_resultado.config(text=f"Resultado da Transformada de Fourier: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para Cálculo Estrutural
def calcular_momento_fletor():
    try:
        f = float(entry_f.get())
        l = float(entry_l.get())
        resultado = f * l
        label_resultado.config(text=f"Resultado do Momento Fletor: {resultado} N.m")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_forca_cortante():
    try:
        f = float(entry_f.get())
        l = float(entry_l.get())
        resultado = f / l
        label_resultado.config(text=f"Resultado da Força Cortante: {resultado} N")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_forca_normal():
    try:
        n = float(entry_n.get())
        a = float(entry_a.get())
        resultado = n / a
        label_resultado.config(text=f"Resultado da Força Normal: {resultado} N/m²")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_esforcos_compostos():
    try:
        n = float(entry_n.get())
        a = float(entry_a.get())
        m = float(entry_m.get())
        y = float(entry_y.get())
        i = float(entry_i.get())
        resultado = (n / a) + (m * y / i)
        label_resultado.config(text=f"Resultado dos Esforços Compostos: {resultado} N/m²")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_dim_coluna():
    try:
        fcd = float(entry_fcd.get())
        fck = float(entry_fck.get())
        resultado = fcd / fck
        label_resultado.config(text=f"Resultado do Dimensionamento de Coluna: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_dim_laje():
    try:
        f = float(entry_f.get())
        a = float(entry_a.get())
        resultado = f / a
        label_resultado.config(text=f"Resultado do Dimensionamento de Lajes: {resultado} N/m²")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para Mecânica dos Solos
def calcular_capacidade_estacas():
    try:
        qu = float(entry_qu.get())
        ap = float(entry_ap.get())
        resultado = qu * ap
        label_resultado.config(text=f"Resultado da Capacidade de Carga de Estacas: {resultado} kN")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_estabilidade_talude():
    try:
        c = float(entry_c.get())
        phi = float(entry_phi.get())
        gamma = float(entry_gamma.get())
        h = float(entry_h.get())
        
        resultado = (c + (gamma * h * math.tan(math.radians(phi)))) / (gamma * h)
        
        label_resultado.config(text=f"Resultado da Estabilidade de Talude: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de que todos os valores são números válidos.")


def calcular_permeabilidade_solo():
    try:
        k = float(entry_k.get())
        i = float(entry_i_permeabilidade.get())
        resultado = k * i
        label_resultado.config(text=f"Resultado da Permeabilidade do Solo: {resultado} m/s")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_recalque_solo():
    try:
        q = float(entry_q.get())
        b = float(entry_b.get())
        e = float(entry_e.get())
        resultado = q * b / e
        label_resultado.config(text=f"Resultado do Recalque do Solo: {resultado} m")
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
    btn_radiciacao.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de funções trigonométricas
def mostrar_funcoes_trigonometricas():
    esconder_todos()
    label_angulo.pack()
    entry_angulo.pack()
    btn_seno.pack()
    btn_cosseno.pack()
    btn_tangente.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de logaritmos
def mostrar_logaritmos():
    esconder_todos()
    label_valor_log.pack()
    entry_valor_log.pack()
    btn_log_natural.pack()
    btn_log_decimal.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de transformada de Fourier
def mostrar_transformada_fourier():
    esconder_todos()
    label_valores_fourier.pack()
    entry_valores_fourier.pack()
    btn_calcular_fourier.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de cálculo estrutural
def mostrar_calculo_estrutural():
    esconder_todos()
    label_f.pack()
    entry_f.pack()
    label_l.pack()
    entry_l.pack()
    btn_momento_fletor.pack()
    btn_forca_cortante.pack()
    btn_forca_normal.pack()
    btn_esforcos_compostos.pack()
    btn_dim_coluna.pack()
    btn_dim_laje.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de mecânica dos solos
def mostrar_mecanica_solo():
    esconder_todos()
    label_qu.pack()
    entry_qu.pack()
    label_ap.pack()
    entry_ap.pack()
    btn_capacidade_estacas.pack()
    btn_estabilidade_talude.pack()
    btn_permeabilidade_solo.pack()
    btn_recalque_solo.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para esconder todos os widgets
def esconder_todos():
    for widget in root.winfo_children():
        widget.pack_forget()

# Função para voltar ao menu principal
def voltar_menu_principal():
    esconder_todos()
    mostrar_menu_principal()

# Função para exibir o menu principal
def mostrar_menu_principal():
    esconder_todos()
    btn_operacoes_basicas.pack()
    btn_radiciacao_potenciacao.pack()
    btn_funcoes_trigonometricas.pack()
    btn_logaritmos.pack()
    btn_transformada_fourier.pack()
    btn_calculo_estrutural.pack()
    btn_mecanica_solo.pack()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Engenharia")

# Botões do menu principal
btn_operacoes_basicas = tk.Button(root, text="Operações Básicas", command=mostrar_operacoes_basicas)
btn_radiciacao_potenciacao = tk.Button(root, text="Radiciação e Potenciação", command=mostrar_radiciacao_potenciacao)
btn_funcoes_trigonometricas = tk.Button(root, text="Funções Trigonométricas", command=mostrar_funcoes_trigonometricas)
btn_logaritmos = tk.Button(root, text="Logaritmos", command=mostrar_logaritmos)
btn_transformada_fourier = tk.Button(root, text="Transformada de Fourier", command=mostrar_transformada_fourier)
btn_calculo_estrutural = tk.Button(root, text="Cálculo Estrutural", command=mostrar_calculo_estrutural)
btn_mecanica_solo = tk.Button(root, text="Mecânica dos Solos", command=mostrar_mecanica_solo)

# Botões para operações básicas
btn_somar = tk.Button(root, text="Somar", command=somar)
btn_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_dividir = tk.Button(root, text="Dividir", command=dividir)
btn_voltar = tk.Button(root, text="Voltar", command=voltar_menu_principal)

# Botões para radiciação e potenciação
btn_potencia = tk.Button(root, text="Potência", command=potencia)
btn_radiciacao = tk.Button(root, text="Radiciação", command=radiciacao)

# Botões para funções trigonométricas
btn_seno = tk.Button(root, text="Seno", command=seno)
btn_cosseno = tk.Button(root, text="Cosseno", command=cosseno)
btn_tangente = tk.Button(root, text="Tangente", command=tangente)

# Botões para logaritmos
btn_log_natural = tk.Button(root, text="Logaritmo Natural", command=logaritmo_natural)
btn_log_decimal = tk.Button(root, text="Logaritmo Decimal", command=logaritmo_decimal)

# Botões para transformada de Fourier
btn_calcular_fourier = tk.Button(root, text="Calcular Fourier", command=calcular_transformada_fourier)

# Botões para cálculo estrutural
btn_momento_fletor = tk.Button(root, text="Momento Fletor", command=calcular_momento_fletor)
btn_forca_cortante = tk.Button(root, text="Força Cortante", command=calcular_forca_cortante)
btn_forca_normal = tk.Button(root, text="Força Normal", command=calcular_forca_normal)
btn_esforcos_compostos = tk.Button(root, text="Esforços Compostos", command=calcular_esforcos_compostos)
btn_dim_coluna = tk.Button(root, text="Dimensionamento de Coluna", command=calcular_dim_coluna)
btn_dim_laje = tk.Button(root, text="Dimensionamento de Laje", command=calcular_dim_laje)

# Botões para mecânica dos solos
btn_capacidade_estacas = tk.Button(root, text="Capacidade de Estacas", command=calcular_capacidade_estacas)
btn_estabilidade_talude = tk.Button(root, text="Estabilidade de Talude", command=calcular_estabilidade_talude)
btn_permeabilidade_solo = tk.Button(root, text="Permeabilidade do Solo", command=calcular_permeabilidade_solo)
btn_recalque_solo = tk.Button(root, text="Recalque do Solo", command=calcular_recalque_solo)

# Labels e Entries para operações básicas
label_num1 = tk.Label(root, text="Número 1:")
entry_num1 = tk.Entry(root)
label_num2 = tk.Label(root, text="Número 2:")
entry_num2 = tk.Entry(root)
label_resultado = tk.Label(root, text="Resultado:")

# Labels e Entries para radiciação e potenciação
label_base = tk.Label(root, text="Base:")
entry_base = tk.Entry(root)
label_expoente = tk.Label(root, text="Expoente:")
entry_expoente = tk.Entry(root)

# Labels e Entries para funções trigonométricas
label_angulo = tk.Label(root, text="Ângulo (graus):")
entry_angulo = tk.Entry(root)

# Labels e Entries para logaritmos
label_valor_log = tk.Label(root, text="Valor:")
entry_valor_log = tk.Entry(root)

# Labels e Entries para transformada de Fourier
label_valores_fourier = tk.Label(root, text="Valores (separados por vírgula):")
entry_valores_fourier = tk.Entry(root)

# Labels e Entries para cálculo estrutural
label_f = tk.Label(root, text="Força (N):")
entry_f = tk.Entry(root)
label_l = tk.Label(root, text="Braço de Alavanca (m):")
entry_l = tk.Entry(root)
label_n = tk.Label(root, text="Força (N):")
entry_n = tk.Entry(root)
label_a = tk.Label(root, text="Área (m²):")
entry_a = tk.Entry(root)
label_m = tk.Label(root, text="Momento (N.m):")
entry_m = tk.Entry(root)
label_y = tk.Label(root, text="Distância (m):")
entry_y = tk.Entry(root)
label_i = tk.Label(root, text="Inércia (m⁴):")
entry_i = tk.Entry(root)
label_fcd = tk.Label(root, text="Fcd (kN/m²):")
entry_fcd = tk.Entry(root)
label_fck = tk.Label(root, text="Fck (kN/m²):")
entry_fck = tk.Entry(root)

# Labels e Entries para mecânica dos solos
label_qu = tk.Label(root, text="Qu (kN/m²):")
entry_qu = tk.Entry(root)
label_ap = tk.Label(root, text="Área Projetada (m²):")
entry_ap = tk.Entry(root)
label_c = tk.Label(root, text="C (kN/m²):")
entry_c = tk.Entry(root)
label_phi = tk.Label(root, text="Ângulo (graus):")
entry_phi = tk.Entry(root)

# Exibir menu principal
mostrar_menu_principal()

# Iniciar a interface gráfica
root.mainloop()
