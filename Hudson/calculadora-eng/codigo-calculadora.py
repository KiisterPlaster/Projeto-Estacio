import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para Cálculo Estrutural
def calcular_momento_fletor():
    try:
        f = float(entry_f.get())
        l = float(entry_l.get())
        resultado = f * l
        label_resultado.config(text=f"Resultado: {resultado} N.m")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_forca_cortante():
    try:
        f = float(entry_f.get())
        l = float(entry_l.get())
        resultado = f / l
        label_resultado.config(text=f"Resultado: {resultado} N")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_forca_normal():
    try:
        n = float(entry_n.get())
        a = float(entry_a.get())
        resultado = n / a
        label_resultado.config(text=f"Resultado: {resultado} N/m²")
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
        label_resultado.config(text=f"Resultado: {resultado} N/m²")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_dim_coluna():
    try:
        fcd = float(entry_fcd.get())
        fck = float(entry_fck.get())
        resultado = fcd / fck
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_dim_laje():
    try:
        f = float(entry_f.get())
        a = float(entry_a.get())
        resultado = f / a
        label_resultado.config(text=f"Resultado: {resultado} N/m²")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para Mecânica dos Solos
def calcular_capacidade_estacas():
    try:
        qu = float(entry_qu.get())
        ap = float(entry_ap.get())
        resultado = qu * ap
        label_resultado.config(text=f"Resultado: {resultado} kN")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_estabilidade_talude():
    try:
        c = float(entry_c.get())
        phi = float(entry_phi.get())
        gamma = float(entry_gamma.get())
        h = float(entry_h.get())
        resultado = (c + (gamma * h * math.tan(math.radians(phi)))) / (gamma * h)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_permeabilidade_solo():
    try:
        k = float(entry_k.get())
        i = float(entry_i_permeabilidade.get())
        resultado = k * i
        label_resultado.config(text=f"Resultado: {resultado} m/s")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_recalque_solo():
    try:
        q = float(entry_q.get())
        b = float(entry_b.get())
        e = float(entry_e.get())
        resultado = q * b / e
        label_resultado.config(text=f"Resultado: {resultado} m")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para Hidráulica e Saneamento
def calcular_vazao_canal():
    try:
        q = float(entry_q_hidraulica.get())
        b = float(entry_b_hidraulica.get())
        y = float(entry_y_hidraulica.get())
        resultado = q * b * y
        label_resultado.config(text=f"Resultado: {resultado} m³/s")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def dimensionar_rede_hidraulica():
    try:
        consumo = float(entry_consumo_hidraulica.get())
        eficiencia = float(entry_eficiencia_hidraulica.get())
        resultado = consumo / eficiencia
        label_resultado.config(text=f"Resultado: {resultado} m³/h")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def tratar_agua():
    try:
        volume = float(entry_volume_agua.get())
        eficiencia = float(entry_eficiencia_agua.get())
        resultado = volume * eficiencia
        label_resultado.config(text=f"Resultado: {resultado} m³")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def tratar_esgoto():
    try:
        volume = float(entry_volume_esgoto.get())
        eficiencia = float(entry_eficiencia_esgoto.get())
        resultado = volume * eficiencia
        label_resultado.config(text=f"Resultado: {resultado} m³")
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
    btn_ln.pack()
    btn_log10.pack()
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

# Funções para exibir a interface de cálculo estrutural
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
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_dim_coluna():
    esconder_todos()
    label_fcd.pack()
    entry_fcd.pack()
    label_fck.pack()
    entry_fck.pack()
    btn_calcular_dim_coluna.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_dim_laje():
    esconder_todos()
    label_f.pack()
    entry_f.pack()
    label_a.pack()
    entry_a.pack()
    btn_calcular_dim_laje.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Funções para exibir a interface de mecânica dos solos
def mostrar_mecanica_solo():
    esconder_todos()
    label_qu.pack()
    entry_qu.pack()
    label_ap.pack()
    entry_ap.pack()
    btn_calcular_capacidade_estacas.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_estabilidade_talude():
    esconder_todos()
    label_c.pack()
    entry_c.pack()
    label_phi.pack()
    entry_phi.pack()
    label_gamma.pack()
    entry_gamma.pack()
    label_h.pack()
    entry_h.pack()
    btn_calcular_estabilidade_talude.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_permeabilidade_solo():
    esconder_todos()
    label_k.pack()
    entry_k.pack()
    label_i_permeabilidade.pack()
    entry_i_permeabilidade.pack()
    btn_calcular_permeabilidade_solo.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_recalque_solo():
    esconder_todos()
    label_q.pack()
    entry_q.pack()
    label_b.pack()
    entry_b.pack()
    label_e.pack()
    entry_e.pack()
    btn_calcular_recalque_solo.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Funções para exibir a interface de hidráulica e saneamento
def mostrar_hidraulica_saneamento():
    esconder_todos()
    label_q_hidraulica.pack()
    entry_q_hidraulica.pack()
    label_b_hidraulica.pack()
    entry_b_hidraulica.pack()
    label_y_hidraulica.pack()
    entry_y_hidraulica.pack()
    btn_calcular_vazao_canal.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_dimensionar_rede_hidraulica():
    esconder_todos()
    label_consumo_hidraulica.pack()
    entry_consumo_hidraulica.pack()
    label_eficiencia_hidraulica.pack()
    entry_eficiencia_hidraulica.pack()
    btn_dimensionar_rede_hidraulica.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_tratar_agua():
    esconder_todos()
    label_volume_agua.pack()
    entry_volume_agua.pack()
    label_eficiencia_agua.pack()
    entry_eficiencia_agua.pack()
    btn_tratar_agua.pack()
    label_resultado.pack()
    btn_voltar.pack()

def mostrar_tratar_esgoto():
    esconder_todos()
    label_volume_esgoto.pack()
    entry_volume_esgoto.pack()
    label_eficiencia_esgoto.pack()
    entry_eficiencia_esgoto.pack()
    btn_tratar_esgoto.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para esconder todos os widgets da interface
def esconder_todos():
    for widget in root.winfo_children():
        widget.pack_forget()

# Configuração da interface gráfica principal
root = tk.Tk()
root.title("Calculadora Multidisciplinar")
root.geometry("800x600")

# Widgets para operações básicas
label_num1 = tk.Label(root, text="Número 1:")
entry_num1 = tk.Entry(root)
label_num2 = tk.Label(root, text="Número 2:")
entry_num2 = tk.Entry(root)
btn_somar = tk.Button(root, text="Somar", command=somar)
btn_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_dividir = tk.Button(root, text="Dividir", command=dividir)
label_resultado = tk.Label(root, text="Resultado:")
btn_voltar = tk.Button(root, text="Voltar", command=esconder_todos)

# Widgets para radiciação e potenciação
label_base = tk.Label(root, text="Base:")
entry_base = tk.Entry(root)
label_expoente = tk.Label(root, text="Expoente:")
entry_expoente = tk.Entry(root)
btn_potencia = tk.Button(root, text="Potência", command=potencia)
btn_radiciacao = tk.Button(root, text="Radiciação", command=radiciacao)

# Widgets para funções trigonométricas
label_angulo = tk.Label(root, text="Ângulo (em graus):")
entry_angulo = tk.Entry(root)
btn_seno = tk.Button(root, text="Seno", command=seno)
btn_cosseno = tk.Button(root, text="Cosseno", command=cosseno)
btn_tangente = tk.Button(root, text="Tangente", command=tangente)

# Widgets para logaritmos
label_valor_log = tk.Label(root, text="Valor:")
entry_valor_log = tk.Entry(root)
btn_ln = tk.Button(root, text="Ln", command=logaritmo_natural)
btn_log10 = tk.Button(root, text="Log10", command=logaritmo_decimal)

# Widgets para transformada de Fourier
label_valores_fourier = tk.Label(root, text="Valores (separados por vírgula):")
entry_valores_fourier = tk.Entry(root)
btn_calcular_fourier = tk.Button(root, text="Calcular Transformada de Fourier", command=calcular_transformada_fourier)

# Widgets para cálculo estrutural
label_f = tk.Label(root, text="Força (F):")
entry_f = tk.Entry(root)
label_l = tk.Label(root, text="Largura (L):")
entry_l = tk.Entry(root)
btn_momento_fletor = tk.Button(root, text="Calcular Momento Fletor", command=calcular_momento_fletor)
btn_forca_cortante = tk.Button(root, text="Calcular Força Cortante", command=calcular_forca_cortante)
btn_forca_normal = tk.Button(root, text="Calcular Força Normal", command=calcular_forca_normal)
btn_esforcos_compostos = tk.Button(root, text="Calcular Esforços Compostos", command=calcular_esforcos_compostos)

label_fcd = tk.Label(root, text="FCD:")
entry_fcd = tk.Entry(root)
label_fck = tk.Label(root, text="FCK:")
entry_fck = tk.Entry(root)
btn_calcular_dim_coluna = tk.Button(root, text="Calcular Dimensões da Coluna", command=calcular_dim_coluna)

label_a = tk.Label(root, text="Área (A):")
entry_a = tk.Entry(root)
btn_calcular_dim_laje = tk.Button(root, text="Calcular Dimensões da Laje", command=calcular_dim_laje)

# Widgets para mecânica dos solos
label_qu = tk.Label(root, text="Qu:")
entry_qu = tk.Entry(root)
label_ap = tk.Label(root, text="Ap:")
entry_ap = tk.Entry(root)
btn_calcular_capacidade_estacas = tk.Button(root, text="Calcular Capacidade de Estacas", command=calcular_capacidade_estacas)

label_c = tk.Label(root, text="C:")
entry_c = tk.Entry(root)
label_phi = tk.Label(root, text="φ (em graus):")
entry_phi = tk.Entry(root)
label_gamma = tk.Label(root, text="γ:")
entry_gamma = tk.Entry(root)
label_h = tk.Label(root, text="H:")
entry_h = tk.Entry(root)
btn_calcular_estabilidade_talude = tk.Button(root, text="Calcular Estabilidade do Talude", command=calcular_estabilidade_talude)

label_k = tk.Label(root, text="K:")
entry_k = tk.Entry(root)
label_i_permeabilidade = tk.Label(root, text="i:")
entry_i_permeabilidade = tk.Entry(root)
btn_calcular_permeabilidade_solo = tk.Button(root, text="Calcular Permeabilidade do Solo", command=calcular_permeabilidade_solo)

label_q = tk.Label(root, text="Q:")
entry_q = tk.Entry(root)
label_b = tk.Label(root, text="B:")
entry_b = tk.Entry(root)
label_e = tk.Label(root, text="E:")
entry_e = tk.Entry(root)
btn_calcular_recalque_solo = tk.Button(root, text="Calcular Recalque do Solo", command=calcular_recalque_solo)

# Widgets para hidráulica e saneamento
label_q_hidraulica = tk.Label(root, text="Vazão (Q):")
entry_q_hidraulica = tk.Entry(root)
label_b_hidraulica = tk.Label(root, text="Largura (B):")
entry_b_hidraulica = tk.Entry(root)
label_y_hidraulica = tk.Label(root, text="Profundidade (Y):")
entry_y_hidraulica = tk.Entry(root)
btn_calcular_vazao_canal = tk.Button(root, text="Calcular Vazão do Canal", command=calcular_vazao_canal)

label_consumo_hidraulica = tk.Label(root, text="Consumo:")
entry_consumo_hidraulica = tk.Entry(root)
label_eficiencia_hidraulica = tk.Label(root, text="Eficiência:")
entry_eficiencia_hidraulica = tk.Entry(root)
btn_dimensionar_rede_hidraulica = tk.Button(root, text="Dimensionar Rede Hidráulica", command=dimensionar_rede_hidraulica)

label_volume_agua = tk.Label(root, text="Volume:")
entry_volume_agua = tk.Entry(root)
label_eficiencia_agua = tk.Label(root, text="Eficiência:")
entry_eficiencia_agua = tk.Entry(root)
btn_tratar_agua = tk.Button(root, text="Tratar Água", command=tratar_agua)

label_volume_esgoto = tk.Label(root, text="Volume:")
entry_volume_esgoto = tk.Entry(root)
label_eficiencia_esgoto = tk.Label(root, text="Eficiência:")
entry_eficiencia_esgoto = tk.Entry(root)
btn_tratar_esgoto = tk.Button(root, text="Tratar Esgoto", command=tratar_esgoto)

# Menu principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Menu Operações Básicas
menu_operacoes_basicas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Operações Básicas", menu=menu_operacoes_basicas)
menu_operacoes_basicas.add_command(label="Somar", command=mostrar_operacoes_basicas)
menu_operacoes_basicas.add_command(label="Subtrair", command=mostrar_operacoes_basicas)
menu_operacoes_basicas.add_command(label="Multiplicar", command=mostrar_operacoes_basicas)
menu_operacoes_basicas.add_command(label="Dividir", command=mostrar_operacoes_basicas)

# Menu Potenciação e Radiciação
menu_radiciacao_potenciacao = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Potenciação e Radiciação", menu=menu_radiciacao_potenciacao)
menu_radiciacao_potenciacao.add_command(label="Potência", command=mostrar_radiciacao_potenciacao)
menu_radiciacao_potenciacao.add_command(label="Radiciação", command=mostrar_radiciacao_potenciacao)

# Menu Funções Trigonométricas
menu_funcoes_trigonometricas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Funções Trigonométricas", menu=menu_funcoes_trigonometricas)
menu_funcoes_trigonometricas.add_command(label="Seno", command=mostrar_funcoes_trigonometricas)
menu_funcoes_trigonometricas.add_command(label="Cosseno", command=mostrar_funcoes_trigonometricas)
menu_funcoes_trigonometricas.add_command(label="Tangente", command=mostrar_funcoes_trigonometricas)

# Menu Logaritmos
menu_logaritmos = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Logaritmos", menu=menu_logaritmos)
menu_logaritmos.add_command(label="Ln", command=mostrar_logaritmos)
menu_logaritmos.add_command(label="Log10", command=mostrar_logaritmos)

# Menu Transformada de Fourier
menu_transformada_fourier = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Transformada de Fourier", menu=menu_transformada_fourier)
menu_transformada_fourier.add_command(label="Calcular Transformada de Fourier", command=mostrar_transformada_fourier)

# Menu Cálculo Estrutural
menu_calculo_estrutural = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Cálculo Estrutural", menu=menu_calculo_estrutural)
menu_calculo_estrutural.add_command(label="Calcular Momento Fletor", command=mostrar_calculo_estrutural)
menu_calculo_estrutural.add_command(label="Calcular Força Cortante", command=mostrar_calculo_estrutural)
menu_calculo_estrutural.add_command(label="Calcular Força Normal", command=mostrar_calculo_estrutural)
menu_calculo_estrutural.add_command(label="Calcular Esforços Compostos", command=mostrar_calculo_estrutural)
menu_calculo_estrutural.add_command(label="Calcular Dimensões da Coluna", command=mostrar_dim_coluna)
menu_calculo_estrutural.add_command(label="Calcular Dimensões da Laje", command=mostrar_dim_laje)

# Menu Mecânica dos Solos
menu_mecanica_solo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Mecânica dos Solos", menu=menu_mecanica_solo)
menu_mecanica_solo.add_command(label="Calcular Capacidade de Estacas", command=mostrar_mecanica_solo)
menu_mecanica_solo.add_command(label="Calcular Estabilidade do Talude", command=mostrar_estabilidade_talude)
menu_mecanica_solo.add_command(label="Calcular Permeabilidade do Solo", command=mostrar_permeabilidade_solo)
menu_mecanica_solo.add_command(label="Calcular Recalque do Solo", command=mostrar_recalque_solo)

# Menu Hidráulica e Saneamento
menu_hidraulica_saneamento = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Hidráulica e Saneamento", menu=menu_hidraulica_saneamento)
menu_hidraulica_saneamento.add_command(label="Calcular Vazão do Canal", command=mostrar_hidraulica_saneamento)
menu_hidraulica_saneamento.add_command(label="Dimensionar Rede Hidráulica", command=mostrar_dimensionar_rede_hidraulica)
menu_hidraulica_saneamento.add_command(label="Tratar Água", command=mostrar_tratar_agua)
menu_hidraulica_saneamento.add_command(label="Tratar Esgoto", command=mostrar_tratar_esgoto)

# Exibir a interface principal
esconder_todos()
mostrar_operacoes_basicas()

root.mainloop()
