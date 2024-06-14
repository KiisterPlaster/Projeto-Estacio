import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Funções para operações básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        messagebox.showerror("Erro", "Divisão por zero!")
        return None
    else:
        return a / b

# Funções para potenciação e radiciação
def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return a ** 0.5

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return a ** (1 / n)

# Funções para funções matemáticas
def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    if math.cos(x) == 0:
        messagebox.showerror("Erro", "Tangente indefinida!")
        return None
    else:
        return math.tan(x)

def logaritmo_natural(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo natural de número não positivo!")
        return None
    else:
        return math.log(x)

def logaritmo_decimal(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo decimal de número não positivo!")
        return None
    else:
        return math.log10(x)

# Funções para operações com memória
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

# Funções para integração numérica
def integral_numerica(funcao_str, a, b, n):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

# Funções para derivada numérica
def derivada_numerica(funcao_str, x, h):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

# Funções para transformada de Fourier
def transformada_fourier(sinal):
    fourier = np.fft.fft(sinal)
    return fourier

# Funções para cálculos estruturais (implementar de acordo com suas necessidades)
def momento_fletor(forca, distancia, tipo_apoio):
    # Implementar a lógica para cálculo de momento fletor considerando o tipo de apoio (engasta, bi-apoiada, etc.)
    pass

def cortante(forca, distancia, tipo_apoio):
    # Implementar a lógica para cálculo de cortante considerando o tipo de apoio
    pass

def normal(area, tensao):
    # Implementar a Lei de Hooke para calcular a força normal
    return area * tensao

def analise_esforcos_composta(materiais, geometrias):
    # Implementar a lógica para análise de esforços em vigas compostas
    pass

def dimensionamento_coluna(carga, material, comprimento):
    # Implementar a lógica para dimensionamento de colunas utilizando normas como a NBR 6118
    pass

def calculo_laje(carga, vão, material, espessura):
    # Implementar a lógica para cálculo de lajes utilizando métodos como o método de vigas biapoiadas
    pass

# Funções para mecânica dos solos (implementar de acordo com suas necessidades)
def capacidade_carga_estacas(metodo, parametros):
    # Implementar a lógica para cálculo da capacidade de carga de estacas utilizando métodos como Meyerhof ou Terzaghi
    pass

def estabilidade_talude(metodo, parametros):
    # Implementar a lógica para análise da estabilidade de taludes utilizando métodos como Mohr-Coulomb ou Bishop
    pass

def permeabilidade_solo(metodo, parametros):
    # Implementar a lógica para cálculo da permeabilidade do solo utilizando métodos como teste de permeabilidade
    pass

def recalque_solo(metodo, parametros):
    # Implementar a lógica para cálculo de recalque do solo utilizando métodos como elasticidade ou Winkler
    pass

# Funções para hidráulica e saneamento (implementar de acordo com suas necessidades)
def fluxo_tubulacao(vazão, diametro, rugosidade):
    # Implementar a lógica para cálculo do fluxo em tubulações utilizando equações como Darcy-Weisbach
    pass

def fluxo_canal(area_molhada, declividade, rugosidade):
    # Implementar a lógica para cálculo do fluxo em canais abertos utilizando equações como Manning
    pass

def dimensionamento_rede_hidraulica(metodo, parametros):
    # Implementar a lógica para dimensionamento de redes hidráulicas utilizando normas como NBR 10838
    pass

def tratamento_agua(metodo, parametros):
    # Implementar a lógica para cálculo de estações de tratamento de água utilizando métodos como coagulação
    pass

def tratamento_esgoto(metodo, parametros):
    # Implementar a lógica para cálculo de estações de tratamento de esgoto utilizando métodos como ativação por lodo

# Funções para topografia (implementar de acordo com suas necessidades)
 def area_terreno(vertices):
    # Implementar a lógica para cálculo da área de um terreno utilizando métodos como planímetro
    pass

def volume_terreno(area, profundidade):
    # Implementar a lógica para cálculo do volume de um terreno
    pass

def nivelamento(pontos):
    # Implementar a lógica para nivelamento utilizando instrumentos como o nível
    pass

def locacao_obra(coordenadas):
    # Implementar a lógica para locação de obras utilizando instrumentos como o teodolito
    pass

def curva_nivel(pontos):
    # Implementar a lógica para traçado de curvas de nível utilizando métodos de interpolação

# Interface gráfica (utilizando tkinter como exemplo)
 def interface():
    # Criar a janela principal
    janela = Tk()
    janela.title("Calculadora Científica Avançada - Engenharia Civil e Básica")

    # Abas para separação das funcionalidades
    abas = ttk.Notebook(janela)
    aba_basica = ttk.Frame(abas)
    aba_avancada = ttk.Frame(abas)
    aba_engenharia_civil = ttk.Frame(abas)
    abas.add(aba_basica, text="Básica")
    abas.add(aba_avancada, text="Avançada")
    abas.add(aba_engenharia_civil, text="Eng. Civil")
    abas.pack(expand=True, fill="both")

    # Funcionalidades básicas (utilizar widgets do tkinter)
    # ... (implementar campos de entrada, botões, labels para as operações básicas)

    # Funcionalidades avançadas (integração, derivada, transformada de Fourier)
    def integracao_numerica():
        funcao_str = entrada_funcao.get()
        a = float(entrada_limite_a.get())
        b = float(entrada_limite_b.get())
        n = int(entrada_pontos.get())
        resultado = integral_numerica(funcao_str, a, b, n)
        if resultado is not None:
            label_resultado_integracao.config(text=f"Resultado: {resultado:.4f}")

    label_funcao_integracao = Label(aba_avancada, text="Função:")
    label_funcao_integracao.pack()
    entrada_funcao = Entry(aba_avancada)
    entrada_funcao.pack()

    label_limite_a = Label(aba_avancada, text="Limite inferior (a):")
    label_limite_a.pack()
    entrada_limite_a = Entry(aba_avancada)
    entrada_limite_a.pack()

    label_limite_b = Label(aba_avancada, text="Limite superior (b):")
    label_limite_b.pack()
    entrada_limite_b = Entry(aba_avancada)
    entrada_limite_b.pack()

    label_pontos = Label(aba_avancada, text="Número de pontos (n):")
    label_pontos.pack()
    entrada_pontos = Entry(aba_avancada)
    entrada_pontos.pack()

    botao_integrar = Button(aba_avancada, text="Integrar", command=integracao_numerica)
    botao_integrar.pack()

    label_resultado_integracao = Label(aba_avancada, text="Resultado:")
    label_resultado_integracao.pack()

    def derivada_numerica():
        funcao_str = entrada_funcao_derivada.get()
        x = float(entrada_valor_x.get())
        h = float(entrada_passo.get())
        resultado = derivada_numerica(funcao_str, x, h)
        if resultado is not None:
            label_resultado_derivada.config(text=f"Derivada: {resultado:.4f}")

    label_funcao_derivada = Label(aba_avancada, text="Função:")
    label_funcao_derivada.pack()
    entrada_funcao_derivada = Entry(aba_avancada)
    entrada_funcao_derivada.pack()

    label_valor_x = Label(aba_avancada, text="Valor de x:")
    label_valor_x.pack()
    entrada_valor_x = Entry(aba_avancada)
    entrada_valor_x.pack()

    label_passo = Label(aba_avancada, text="Passo (h):")
    label_passo.pack()
    entrada_passo = Entry(aba_avancada)
    entrada_passo.pack()

    botao_derivar = Button(aba_avancada, text="Derivar", command=derivada_numerica)
    botao_derivar.pack()

    label_resultado_derivada = Label(aba_avancada, text="Resultado:")
    label_resultado_derivada.pack()

    def transformada_fourier_plot():
        sinal_str = entrada_sinal.get()
        try:
            sinal = eval(sinal_str)
            fourier = transformada_fourier(sinal)
            plt.plot(np.abs(fourier))
            plt.title("Transformada de Fourier")
            plt.xlabel("Frequência")
            plt.ylabel("Magnitude")
            plt.show()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o sinal: {e}")

    label_sinal = Label(aba_avancada, text="Sinal:")
    label_sinal.pack()
    entrada_sinal = Entry(aba_avancada)
    entrada_sinal.pack()

    botao_fourier = Button(aba_avancada, text="Calcular Fourier", command=transformada_fourier_plot)
    botao_fourier.pack()

    # Funções de Engenharia Civil (implementar botões para acionar funções específicas)
    # ... (implementar botões para momento fletor, cortante
	# ... (código anterior para integração, derivada e transformada de Fourier)

# Funcionalidades básicas (utilizar widgets do tkinter)
def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_soma = Label(aba_basica, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = Entry(aba_basica)
entrada_a_soma.pack()

label_b_soma = Label(aba_basica, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = Entry(aba_basica)
entrada_b_soma.pack()

botao_somar = Button(aba_basica, text="Somar", command=soma_interface)
botao_somar.pack()

label_resultado_soma = Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

def subtracao_interface():
    try:
        a = float(entrada_a_subtracao.get())
        b = float(entrada_b_subtracao.get())
        resultado = subtracao(a, b)
        label_resultado_subtracao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_subtracao = Label(aba_basica, text="Valor de a:")
label_a_subtracao.pack()
entrada_a_subtracao = Entry(aba_basica)
entrada_a_subtracao.pack()

label_b_subtracao = Label(aba_basica, text="Valor de b:")
label_b_subtracao.pack()
entrada_b_subtracao = Entry(aba_basica)
entrada_b_subtracao.pack()

botao_subtrair = Button(aba_basica, text="Subtrair", command=subtracao_interface)
botao_subtrair.pack()

label_resultado_subtracao = Label(aba_basica, text="Resultado:")
label_resultado_subtracao.pack()

def multiplicacao_interface():
    try:
        a = float(entrada_a_multiplicacao.get())
        b = float(entrada_b_multiplicacao.get())
        resultado = multiplicacao(a, b)
        label_resultado_multiplicacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_multiplicacao = Label(aba_basica, text="Valor de a:")
label_a_multiplicacao.pack()
entrada_a_multiplicacao = Entry(aba_basica)
entrada_a_multiplicacao.pack()

label_b_multiplicacao = Label(aba_basica, text="Valor de b:")
label_b_multiplicacao.pack()
entrada_b_multiplicacao = Entry(aba_basica)
entrada_b_multiplicacao.pack()

botao_multiplicar = Button(aba_basica, text="Multiplicar", command=multiplicacao_interface)
botao_multiplicar.pack()

label_resultado_multiplicacao = Label(aba_basica, text="Resultado:")
label_resultado_multiplicacao.pack()

def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        label_resultado_divisao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")

label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_

# ... (código anterior para soma, subtração, multiplicação e divisão)

# Funcionalidades de memória (utilizar widgets do tkinter)
def adicionar_memoria_interface():
    nome = entrada_nome_memoria.get()
    valor_str = entrada_valor_memoria.get()
    try:
        valor = float(valor_str)
        adicionar_memoria(nome, valor)
        messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

label_nome_memoria = Label(aba_basica, text="Nome:")
label_nome_memoria.pack()
entrada_nome_memoria = Entry(aba_basica)
entrada_nome_memoria.pack()

label_valor_memoria = Label(aba_basica, text="Valor:")
label_valor_memoria.pack()
entrada_valor_memoria = Entry(aba_basica)
entrada_valor_memoria.pack()

botao_adicionar_memoria = Button(aba_basica, text="Adicionar", command=adicionar_memoria_interface)
botao_adicionar_memoria.pack()

def remover_memoria_interface():
    nome = entrada_nome_memoria_remover.get()
    remover_memoria(nome)
    messagebox.showinfo("Informação", f"Valor com nome '{nome}' removido da memória.")

label_nome_memoria_remover = Label(aba_basica, text="Nome:")
label_nome_memoria_remover.pack()
entrada_nome_memoria_remover = Entry(aba_basica)
entrada_nome_memoria_remover.pack()

botao_remover_memoria = Button(aba_basica, text="Remover", command=remover_memoria_interface)
botao_remover_memoria.pack()

def consultar_memoria_interface():
    nome = entrada_nome_memoria_consultar.get()
    valor = consultar_memoria(nome)
    if valor is not None:
        messagebox.showinfo("Informação", f"Valor do nome '{nome}': {valor}")
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

label_nome_memoria_consultar = Label(aba_basica, text="Nome:")
label_nome_memoria_consultar.pack()
entrada_nome_memoria_consultar = Entry(aba_basica)
entrada_nome_memoria_consultar.pack()

botao_consultar_memoria = Button(aba_basica, text="Consultar", command=consultar_memoria_interface)
botao_consultar_memoria.pack()

def limpar_memoria_interface():
    limpar_memoria()
    messagebox.showinfo("Informação", "Memória limpa.")

botao_limpar_memoria = Button(aba_basica, text="Limpar Memória", command=limpar_memoria_interface)
botao_limpar_memoria.pack()

# Funções de Engenharia Civil (implementar botões para acionar funções específicas)
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get()
        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Resultado: {resultado:.4f} N.m")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_forca_mf = Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack

# ... (código anterior para funções de soma, subtração, multiplicação)

# Função divisão_interface com tratamento de erros e mensagem para o usuário
def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        if resultado is not None:
            label_resultado_divisao.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Divisão por zero!")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

# ... (código restante para outras funções básicas)

# Funções para operações com potências e raízes
def potenciacao_interface():
    try:
        base = float(entrada_base_potenciacao.get())
        expoente = float(entrada_expoente_potenciacao.get())
        resultado = potenciacao(base, expoente)
        label_resultado_potenciacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

def raiz_quadrada_interface():
    try:
        numero = float(entrada_raiz_quadrada.get())
        resultado = raiz_quadrada(numero)
        if resultado is not None:
            label_resultado_raiz_quadrada.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar um número.")

def raiz_n_esima_interface():
    try:
        numero = float(entrada_raiz_n_esima_numero.get())
        indice = float(entrada_raiz_n_esima_indice.get())
        resultado = raiz_n_esima(numero, indice)
        if resultado is not None:
            label_resultado_raiz_n_esima.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz n-ésima de um número negativo com índice par.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

# ... (código para implementar as interfaces gráficas dessas funções)

# ... (código restante da interface gráfica)

# ... (código anterior para funções básicas e de memória)

# Funções de Engenharia Civil (implementar botões para acionar funções específicas)
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o momento fletor.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# ... (código para implementar interfaces gráficas de outras funções de engenharia civil)

# ... (código restante da interface gráfica)

# ... (código anterior para funções básicas, memória e outras funções de engenharia civil)

# Funções de Engenharia Civil
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o momento fletor.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Interface Gráfica para Cálculo de Momento Fletor (aba_engenharia_civil)
label_forca_mf = Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack()

botao_calcular_mf = Button(aba_engenharia_civil, text="Calcular", command=momento_fletor_interface)
botao_calcular_mf.pack()

label_resultado_mf = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

# ... (código restante da interface gráfica)

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
def adicionar_memoria(nome, valor):
    # ... (implementar a lógica para adicionar o valor à memória)

 def remover_memoria(nome):
    # ... (implementar a lógica para remover o valor da memória)

  def consultar_memoria(nome):
    # ... (implementar a lógica para consultar o valor na memória)

   def limpar_memoria():
    # ... (implementar a lógica para limpar a memória)

# Funções de Engenharia Civil (implementar de acordo com suas necessidades)
    def momento_fletor(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o momento fletor)

       def cortante(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o cortante)

# ... (implementar outras funções de engenharia civil que você desejar)

# Interface gráfica principal
        app = tk.Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app)
aba_avancada = tk.Frame(app)
aba_memoria = tk.Frame(app)
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_memoria.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Funções básicas (soma, subtração, multiplicação, divisão)
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

label_resultado_soma = tk.Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

# ... (interfaces para as outras funções básicas: subtração, multiplicação, divisão)

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# ... (implementar interfaces para integração, derivada e transformada de Fourier)

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
label_titulo_memoria.pack()

# ... (implementar interfaces para as funções de memória)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")

