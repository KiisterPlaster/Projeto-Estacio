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

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")