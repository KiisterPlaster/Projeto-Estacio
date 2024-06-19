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

# Função para exibir a interface de transformada de Fourier
def mostrar_transformada_fourier():
    esconder_todos()
    label_valores_fourier.pack()
    entry_valores_fourier.pack()
    btn_transformada_fourier.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de cálculo estrutural
def mostrar_calculo_estrutural():
    esconder_todos()
    label_f.pack()
    entry_f.pack()
    label_l.pack()
    entry_l.pack()
    label_n.pack()
    entry_n.pack()
    label_a.pack()
    entry_a.pack()
    label_m.pack()
    entry_m.pack()
    label_y.pack()
    entry_y.pack()
    label_i.pack()
    entry_i.pack()
    label_fcd.pack()
    entry_fcd.pack()
    label_fck.pack()
    entry_fck.pack()
    btn_momento_fletor.pack()
    btn_forca_cortante.pack()
    btn_forca_normal.pack()
    btn_esforcos_compostos.pack()
    btn_dim_coluna.pack()
    btn_dim_laje.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de mecânica dos solos
def mostrar_mecanica_solos():
    esconder_todos()
    label_qu.pack()
    entry_qu.pack()
    label_ap.pack()
    entry_ap.pack()
    btn_capacidade_estacas.pack()
    label_c.pack()
    entry_c.pack()
    label_phi.pack()
    entry_phi.pack()
    label_gamma.pack()
    entry_gamma.pack()
    label_h.pack()
    entry_h.pack()
    btn_estabilidade_talude.pack()
    label_k.pack()
    entry_k.pack()
    label_i_permeabilidade.pack()
    entry_i_permeabilidade.pack()
    btn_permeabilidade_solo.pack()
    label_q.pack()
    entry_q.pack()
    label_b.pack()
    entry_b.pack()
    label_e.pack()
    entry_e.pack()
    btn_recalque_solo.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para esconder todos os componentes
def esconder_todos():
    for widget in root.pack_slaves():
        widget.pack_forget()

# Função para voltar à interface inicial
def voltar():
    esconder_todos()
    btn_op_basicas.pack()
    btn_rad_pot.pack()
    btn_funcoes_matematicas.pack()
    btn_transformada_fourier.pack()
    btn_calculo_estrutural.pack()
    btn_mecanica_solos.pack()

# Função principal para configurar a interface gráfica
def configurar_interface_grafica():
    global root, label_num1, entry_num1, label_num2, entry_num2
    global btn_somar, btn_subtrair, btn_multiplicar, btn_dividir
    global label_base, entry_base, label_expoente, entry_expoente
    global btn_potencia, label_valor, entry_valor, btn_radiciacao
    global label_angulo, entry_angulo, btn_seno, btn_cosseno, btn_tangente
    global label_valor_log, entry_valor_log, btn_logaritmo_natural, btn_logaritmo_decimal
    global btn_op_basicas, btn_rad_pot, btn_funcoes_matematicas, btn_transformada_fourier
    global btn_calculo_estrutural, btn_mecanica_solos, btn_voltar, label_resultado
    global label_valores_fourier, entry_valores_fourier, btn_transformada_fourier
    global label_f, entry_f, label_l, entry_l, label_n, entry_n, label_a, entry_a
    global label_m, entry_m, label_y, entry_y, label_i, entry_i, label_fcd, entry_fcd
    global label_fck, entry_fck, btn_momento_fletor, btn_forca_cortante, btn_forca_normal
    global btn_esforcos_compostos, btn_dim_coluna, btn_dim_laje
    global label_qu, entry_qu, label_ap, entry_ap, btn_capacidade_estacas
    global label_c, entry_c, label_phi, entry_phi, label_gamma, entry_gamma
    global label_h, entry_h, btn_estabilidade_talude, label_k, entry_k
    global label_i_permeabilidade, entry_i_permeabilidade, btn_permeabilidade_solo
    global label_q, entry_q, label_b, entry_b, label_e, entry_e, btn_recalque_solo

    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("500x600")

    # Botões iniciais
    btn_op_basicas = tk.Button(root, text="Operações Básicas", command=mostrar_operacoes_basicas)
    btn_rad_pot = tk.Button(root, text="Radiciação e Potenciação", command=mostrar_radiciacao_potenciacao)
    btn_funcoes_matematicas = tk.Button(root, text="Funções Matemáticas", command=mostrar_funcoes_matematicas)
    btn_transformada_fourier = tk.Button(root, text="Transformada de Fourier", command=mostrar_transformada_fourier)
    btn_calculo_estrutural = tk.Button(root, text="Cálculo Estrutural", command=mostrar_calculo_estrutural)
    btn_mecanica_solos = tk.Button(root, text="Mecânica dos Solos", command=mostrar_mecanica_solos)
    btn_op_basicas.pack()
    btn_rad_pot.pack()
    btn_funcoes_matematicas.pack()
    btn_transformada_fourier.pack()
    btn_calculo_estrutural.pack()
    btn_mecanica_solos.pack()

    # Labels e entradas para operações básicas
    label_num1 = tk.Label(root, text="Número 1:")
    entry_num1 = tk.Entry(root)
    label_num2 = tk.Label(root, text="Número 2:")
    entry_num2 = tk.Entry(root)

    # Botões de operações básicas
    btn_somar = tk.Button(root, text="Somar", command=somar)
    btn_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
    btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
    btn_dividir = tk.Button(root, text="Dividir", command=dividir)

    # Labels e entradas para potenciação
    label_base = tk.Label(root, text="Base:")
    entry_base = tk.Entry(root)
    label_expoente = tk.Label(root, text="Expoente:")
    entry_expoente = tk.Entry(root)

    # Botão de potenciação
    btn_potencia = tk.Button(root, text="Potência", command=potencia)

    # Labels e entradas para radiciação
    label_valor = tk.Label(root, text="Valor para raiz quadrada:")
    entry_valor = tk.Entry(root)

    # Botão de radiciação
    btn_radiciacao = tk.Button(root, text="Raiz Quadrada", command=radiciacao)

    # Labels e entradas para funções matemáticas
    label_angulo = tk.Label(root, text="Ângulo (graus):")
    entry_angulo = tk.Entry(root)
    btn_seno = tk.Button(root, text="Seno", command=seno)
    btn_cosseno = tk.Button(root, text="Cosseno", command=cosseno)
    btn_tangente = tk.Button(root, text="Tangente", command=tangente)
    label_valor_log = tk.Label(root, text="Valor para logaritmo:")
    entry_valor_log = tk.Entry(root)
    btn_logaritmo_natural = tk.Button(root, text="Logaritmo Natural", command=logaritmo_natural)
    btn_logaritmo_decimal = tk.Button(root, text="Logaritmo Decimal", command=logaritmo_decimal)

    # Labels e entradas para transformada de Fourier
    label_valores_fourier = tk.Label(root, text="Valores (separados por vírgula):")
    entry_valores_fourier = tk.Entry(root)
    btn_transformada_fourier = tk.Button(root, text="Calcular Transformada de Fourier", command=calcular_transformada_fourier)

    # Labels e entradas para cálculo estrutural
    label_f = tk.Label(root, text="Força (N):")
    entry_f = tk.Entry(root)
    label_l = tk.Label(root, text="Comprimento (m):")
    entry_l = tk.Entry(root)
    label_n = tk.Label(root, text="Força Normal (N):")
    entry_n = tk.Entry(root)
    label_a = tk.Label(root, text="Área (m²):")
    entry_a = tk.Entry(root)
    label_m = tk.Label(root, text="Momento (N.m):")
    entry_m = tk.Entry(root)
    label_y = tk.Label(root, text="Distância (m):")
    entry_y = tk.Entry(root)
    label_i = tk.Label(root, text="Momento de Inércia (m⁴):")
    entry_i = tk.Entry(root)
    label_fcd = tk.Label(root, text="Fcd:")
    entry_fcd = tk.Entry(root)
    label_fck = tk.Label(root, text="Fck:")
    entry_fck = tk.Entry(root)
    btn_momento_fletor = tk.Button(root, text="Momento Fletor", command=calcular_momento_fletor)
    btn_forca_cortante = tk.Button(root, text="Força Cortante", command=calcular_forca_cortante)
    btn_forca_normal = tk.Button(root, text="Força Normal", command=calcular_forca_normal)
    btn_esforcos_compostos = tk.Button(root, text="Esforços Compostos", command=calcular_esforcos_compostos)
    btn_dim_coluna = tk.Button(root, text="Dimensionamento de Coluna", command=calcular_dim_coluna)
    btn_dim_laje = tk.Button(root, text="Dimensionamento de Lajes", command=calcular_dim_laje)

    # Labels e entradas para mecânica dos solos
    label_qu = tk.Label(root, text="Capacidade de Carga (kN):")
    entry_qu = tk.Entry(root)
    label_ap = tk.Label(root, text="Área da Ponta (m²):")
    entry_ap = tk.Entry(root)
    btn_capacidade_estacas = tk.Button(root, text="Capacidade de Carga de Estacas", command=calcular_capacidade_estacas)
    label_c = tk.Label(root, text="Coesão (kPa):")
    entry_c = tk.Entry(root)
    label_phi = tk.Label(root, text="Ângulo de Atrito (°):")
    entry_phi = tk.Entry(root)
    label_gamma = tk.Label(root, text="Peso Específico (kN/m³):")
    entry_gamma = tk.Entry(root)
    label_h = tk.Label(root, text="Altura do Talude (m):")
    entry_h = tk.Entry(root)
    btn_estabilidade_talude = tk.Button(root, text="Estabilidade de Talude", command=calcular_estabilidade_talude)

    label_k = tk.Label(root, text="Coeficiente de Permeabilidade (m/s):")
    entry_k = tk.Entry(root)
    label_i_permeabilidade = tk.Label(root, text="Gradiente Hidráulico:")
    entry_i_permeabilidade = tk.Entry(root)
    btn_permeabilidade_solo = tk.Button(root, text="Permeabilidade do Solo", command=calcular_permeabilidade_solo)

    label_q = tk.Label(root, text="Carga (kN):")
    entry_q = tk.Entry(root)
    label_b = tk.Label(root, text="Largura da Fundação (m):")
    entry_b = tk.Entry(root)
    label_e = tk.Label(root, text="Módulo de Elasticidade (kPa):")
    entry_e = tk.Entry(root)
    btn_recalque_solo = tk.Button(root, text="Recalque do Solo", command=calcular_recalque_solo)

    # Botão para voltar à tela inicial
    btn_voltar = tk.Button(root, text="Voltar", command=voltar)

    # Label para exibir os resultados
    label_resultado = tk.Label(root, text="Resultado:")

    voltar()  # Inicializa a tela inicial

    root.mainloop()

configurar_interface_grafica()