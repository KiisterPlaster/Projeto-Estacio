
import tkinter as tk
from tkinter import messagebox
import math

def append_to_expression(symbol):
    expression_field.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(expression_field.get())
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")

def clear():
    expression_field.delete(0, tk.END)

def sqrt():
    try:
        result = math.sqrt(float(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def log():
    try:
        result = math.log10(float(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def sin():
    try:
        result = math.sin(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def cos():
    try:
        result = math.cos(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def tan():
    try:
        result = math.tan(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de expressão
expression_field = tk.Entry(root, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
expression_field.grid(row=0, column=0, columnspan=4)

# Criação dos botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: append_to_expression(t))
    button.grid(row=row, column=col, sticky="nsew")

# Criação dos botões de funções avançadas
advanced_buttons = [
    ('√', sqrt), ('log', log), ('sin', sin), ('cos', cos), ('tan', tan), ('C', clear)
]

for i, (text, func) in enumerate(advanced_buttons):
    button = tk.Button(root, text=text, padx=20, pady=20, command=func)
    button.grid(row=i//2+1, column=4+i%2, sticky="nsew")

# Tornar os botões responsivos
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

# Execução do loop principal da interface
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_fft():
    try:
        # Pegando a expressão de entrada
        data = entry_data.get()
        # Convertendo a string em uma lista de números
        data_list = list(map(float, data.split(',')))
        # Calculando a Transformada de Fourier
        fft_result = np.fft.fft(data_list)
        freqs = np.fft.fftfreq(len(fft_result))
        
        # Plotando o resultado
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(data_list, label='Data')
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.plot(freqs, np.abs(fft_result), label='FFT')
        plt.legend()
        
        plt.show()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular FFT: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Transformada de Fourier")

# Criação dos campos de entrada e botões
label_data = tk.Label(root, text="Insira os dados (separados por vírgula):")
label_data.pack(pady=5)

entry_data = tk.Entry(root, width=50)
entry_data.pack(pady=5)

button_calculate = tk.Button(root, text="Calcular FFT", command=calculate_fft)
button_calculate.pack(pady=20)

# Execução do loop principal da interface
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_beam():
    try:
        L = float(entry_length.get())  # Comprimento da viga
        P = float(entry_load.get())    # Valor da carga
        a = float(entry_position.get()) # Posição da carga

        if a > L:
            messagebox.showerror("Erro", "A posição da carga não pode ser maior que o comprimento da viga.")
            return

        # Reações nos apoios (simplificação para viga simplesmente apoiada)
        R1 = P * (L - a) / L
        R2 = P * a / L

        # Cálculo dos momentos fletores e forças cortantes ao longo da viga
        x = np.linspace(0, L, 500)
        V = np.where(x <= a, R1, -R2)
        M = np.where(x <= a, R1 * x, R1 * a - R2 * (x - a))

        # Plotando os resultados
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(x, V, label='Força Cortante (V)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Força Cortante (N)')
        plt.legend()
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(x, M, label='Momento Fletor (M)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Momento Fletor (Nm)')
        plt.legend()
        plt.grid()

        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora Estrutural")

# Labels e entradas para os dados da viga
label_length = tk.Label(root, text="Comprimento da Viga (m):")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

label_load = tk.Label(root, text="Valor da Carga (N):")
label_load.pack(pady=5)

entry_load = tk.Entry(root)
entry_load.pack(pady=5)

label_position = tk.Label(root, text="Posição da Carga (m):")
label_position.pack(pady=5)

entry_position = tk.Entry(root)
entry_position.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_beam)
button_calculate.pack(pady=20)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import math

def calculate_capacity():
    try:
        c = float(entry_cohesion.get())
        sigma = float(entry_sigma.get())
        gamma = float(entry_gamma.get())
        B = float(entry_width.get())
        phi = float(entry_phi.get())

        phi_rad = math.radians(phi)

        Nq = math.exp(math.pi * math.tan(phi_rad)) * (math.tan(math.radians(45) + phi_rad / 2))**2
        Nc = (Nq - 1) / math.tan(phi_rad)
        N_gamma = 2 * (Nq + 1) * math.tan(phi_rad)

        q_ult = c * Nc + sigma * Nq + 0.5 * gamma * B * N_gamma

        label_result.config(text=f"Capacidade de Carga Última (q_ult): {q_ult:.2f} kN/m²")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Capacidade de Carga de Fundação Rasa")

# Labels e entradas para os dados do solo e da fundação
label_cohesion = tk.Label(root, text="Coesão (c) em kN/m²:")
label_cohesion.pack(pady=5)
entry_cohesion = tk.Entry(root)
entry_cohesion.pack(pady=5)

label_sigma = tk.Label(root, text="Tensão Efetiva (σ') em kN/m²:")
label_sigma.pack(pady=5)
entry_sigma = tk.Entry(root)
entry_sigma.pack(pady=5)

label_gamma = tk.Label(root, text="Peso Específico (γ) em kN/m³:")
label_gamma.pack(pady=5)
entry_gamma = tk.Entry(root)
entry_gamma.pack(pady=5)

label_width = tk.Label(root, text="Largura da Fundação (B) em m:")
label_width.pack(pady=5)
entry_width = tk.Entry(root)
entry_width.pack(pady=5)

label_phi = tk.Label(root, text="Ângulo de Atrito Interno (φ) em graus:")
label_phi.pack(pady=5)
entry_phi = tk.Entry(root)
entry_phi.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_capacity)
button_calculate.pack(pady=20)

# Label para mostrar o resultado
label_result = tk.Label(root, text="Capacidade de Carga Última (q_ult):")
label_result.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_moment():
    try:
        L = float(entry_length.get())  # Comprimento da viga
        P = float(entry_load.get())    # Valor da carga
        a = float(entry_position.get()) # Posição da carga
        support_type = combo_support_type.get()

        if a > L:
            messagebox.showerror("Erro", "A posição da carga não pode ser maior que o comprimento da viga.")
            return

        x = np.linspace(0, L, 500)
        M = np.zeros_like(x)

        if support_type == "Simplesmente apoiada":
            R1 = P * (L - a) / L
            R2 = P * a / L
            M = np.where(x <= a, R1 * x, R1 * a - R2 * (x - a))

        elif support_type == "Engastada":
            M = P * (L - a) * x / L

        elif support_type == "Bi-apoiada":
            R = P / 2
            M = R * x - np.where(x >= L/2, P * (x - L/2), 0)

        else:
            messagebox.showerror("Erro", "Tipo de apoio não reconhecido.")
            return

        # Plotando os resultados
        plt.figure()
        plt.plot(x, M, label='Momento Fletor (M)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Momento Fletor (Nm)')
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Momento Fletor")

# Labels e entradas para os dados da viga
label_length = tk.Label(root, text="Comprimento da Viga (m):")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

label_load = tk.Label(root, text="Valor da Carga (N):")
label_load.pack(pady=5)
entry_load = tk.Entry(root)
entry_load.pack(pady=5)

label_position = tk.Label(root, text="Posição da Carga (m):")
label_position.pack(pady=5)
entry_position = tk.Entry(root)
entry_position.pack(pady=5)

label_support_type = tk.Label(root, text="Tipo de Apoio:")
label_support_type.pack(pady=5)
combo_support_type = ttk.Combobox(root, values=["Simplesmente apoiada", "Engastada", "Bi-apoiada"])
combo_support_type.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_moment)
button_calculate.pack(pady=20)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_shear():
    try:
        L = float(entry_length.get())  # Comprimento da viga
        P = float(entry_load.get())    # Valor da carga
        a = float(entry_position.get()) # Posição da carga
        support_type = combo_support_type.get()

        if a > L:
            messagebox.showerror("Erro", "A posição da carga não pode ser maior que o comprimento da viga.")
            return

        x = np.linspace(0, L, 500)
        V = np.zeros_like(x)

        if support_type == "Simplesmente apoiada":
            R1 = P * (L - a) / L
            R2 = P * a / L
            V = np.where(x <= a, R1, -R2)

        elif support_type == "Engastada":
            V = np.where(x <= a, P, 0)

        elif support_type == "Bi-apoiada":
            R = P / 2
            V = np.where(x <= L/2, R, -R)

        else:
            messagebox.showerror("Erro", "Tipo de apoio não reconhecido.")
            return

        # Plotando os resultados
        plt.figure()
        plt.plot(x, V, label='Força Cortante (V)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Força Cortante (N)')
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Força Cortante")

# Labels e entradas para os dados da viga
label_length = tk.Label(root, text="Comprimento da Viga (m):")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

label_load = tk.Label(root, text="Valor da Carga (N):")
label_load.pack(pady=5)
entry_load = tk.Entry(root)
entry_load.pack(pady=5)

label_position = tk.Label(root, text="Posição da Carga (m):")
label_position.pack(pady=5)
entry_position = tk.Entry(root)
entry_position.pack(pady=5)

label_support_type = tk.Label(root, text="Tipo de Apoio:")
label_support_type.pack(pady=5)
combo_support_type = ttk.Combobox(root, values=["Simplesmente apoiada", "Engastada", "Bi-apoiada"])
combo_support_type.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_shear)
button_calculate.pack(pady=20)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def calculate_force():
    try:
        k = float(entry_constant.get())  # Constante de mola (k)
        x = float(entry_deformation.get())  # Deformação (x)

        F = k * x  # Lei de Hooke

        label_result.config(text=f"Força Normal (F): {F:.2f} N")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Força Normal - Lei de Hooke")

# Labels e entradas para os dados
label_constant = tk.Label(root, text="Constante de Mola (k) em N/m:")
label_constant.pack(pady=5)
entry_constant = tk.Entry(root)
entry_constant.pack(pady=5)

label_deformation = tk.Label(root, text="Deformação (x) em m:")
label_deformation.pack(pady=5)
entry_deformation = tk.Entry(root)
entry_deformation.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_force)
button_calculate.pack(pady=20)

# Label para mostrar o resultado
label_result = tk.Label(root, text="Força Normal (F):")
label_result.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def calculate_composite_beam():
    try:
        L1 = float(entry_length1.get())
        L2 = float(entry_length2.get())
        P = float(entry_load.get())
        a = float(entry_position.get())
        E1 = float(entry_E1.get())
        E2 = float(entry_E2.get())
        I1 = float(entry_I1.get())
        I2 = float(entry_I2.get())
        
        if a > L1 + L2:
            messagebox.showerror("Erro", "A posição da carga não pode ser maior que o comprimento total da viga.")
            return
        
        L_total = L1 + L2
        x = np.linspace(0, L_total, 500)
        V = np.zeros_like(x)
        M = np.zeros_like(x)

        if a <= L1:
            R1 = P * (L_total - a) / L_total
            R2 = P * a / L_total
            V = np.where(x <= a, R1, np.where(x <= L1, R1, -R2))
            M = np.where(x <= a, R1 * x, np.where(x <= L1, R1 * a - R2 * (x - a), R1 * a - R2 * (x - a)))
        else:
            R1 = P * (L_total - a) / L_total
            R2 = P * a / L_total
            V = np.where(x <= L1, R1, np.where(x <= a, R1 - P, -R2))
            M = np.where(x <= L1, R1 * x, np.where(x <= a, R1 * x - P * (x - L1), R1 * x - P * (x - L1)))

        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(x, V, label='Força Cortante (V)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Força Cortante (N)')
        plt.legend()
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(x, M, label='Momento Fletor (M)')
        plt.xlabel('Posição ao longo da viga (m)')
        plt.ylabel('Momento Fletor (Nm)')
        plt.legend()
        plt.grid()

        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Análise de Esforços em Vigas Compostas")

# Labels e entradas para os dados das seções
label_length1 = tk.Label(root, text="Comprimento da Seção 1 (m):")
label_length1.pack(pady=5)
entry_length1 = tk.Entry(root)
entry_length1.pack(pady=5)

label_length2 = tk.Label(root, text="Comprimento da Seção 2 (m):")
label_length2.pack(pady=5)
entry_length2 = tk.Entry(root)
entry_length2.pack(pady=5)

label_load = tk.Label(root, text="Valor da Carga (N):")
label_load.pack(pady=5)
entry_load = tk.Entry(root)
entry_load.pack(pady=5)

label_position = tk.Label(root, text="Posição da Carga (m):")
label_position.pack(pady=5)
entry_position = tk.Entry(root)
entry_position.pack(pady=5)

label_E1 = tk.Label(root, text="Módulo de Elasticidade da Seção 1 (E1) em Pa:")
label_E1.pack(pady=5)
entry_E1 = tk.Entry(root)
entry_E1.pack(pady=5)

label_E2 = tk.Label(root, text="Módulo de Elasticidade da Seção 2 (E2) em Pa:")
label_E2.pack(pady=5)
entry_E2 = tk.Entry(root)
entry_E2.pack(pady=5)

label_I1 = tk.Label(root, text="Momento de Inércia da Seção 1 (I1) em m^4:")
label_I1.pack(pady=5)
entry_I1 = tk.Entry(root)
entry_I1.pack(pady=5)

label_I2 = tk.Label(root, text="Momento de Inércia da Seção 2 (I2) em m^4:")
label_I2.pack(pady=5)
entry_I2 = tk.Entry(root)
entry_I2.pack(pady=5)

# Botão para calcular
button_calculate = tk.Button(root, text="Calcular", command=calculate_composite_beam)
button_calculate.pack(pady=20)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_dimensao_coluna():
    try:
        # Obtendo os dados de entrada
        N = float(entry_carga_axial.get())
        M = float(entry_momento_fletor.get())
        b = float(entry_dimensao_b.get())
        h = float(entry_dimensao_h.get())
        f_ck = float(entry_fck.get())
        f_yk = float(entry_fyk.get())
        rho = float(entry_taxa_armadura.get())

        # Parâmetros e coeficientes da norma
        gamma_c = 1.4  # Coeficiente de segurança do concreto
        gamma_s = 1.15  # Coeficiente de segurança do aço
        alpha_c = 0.85  # Redutor da resistência à compressão do concreto
        f_cd = f_ck / gamma_c  # Resistência de cálculo do concreto
        f_yd = f_yk / gamma_s  # Resistência de cálculo do aço

        # Área da seção transversal da coluna
        A_c = b * h

        # Área de aço
        A_s = rho * A_c

        # Cálculo da força resistente da coluna (considerando o momento fletor)
        M_rd = (alpha_c * f_cd * b * h**2 / 6) + (A_s * f_yd * (h / 2))

        # Verificação se a coluna está dimensionada adequadamente
        if N <= alpha_c * f_cd * A_c + A_s * f_yd and M <= M_rd:
            resultado = "A coluna está adequadamente dimensionada."
        else:
            resultado = "A coluna não está adequadamente dimensionada."

        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Dimensionamento de Colunas - NBR 6118")

# Labels e entradas para os dados da coluna
label_carga_axial = tk.Label(root, text="Carga Axial (N) em kN:")
label_carga_axial.pack(pady=5)
entry_carga_axial = tk.Entry(root)
entry_carga_axial.pack(pady=5)

label_momento_fletor = tk.Label(root, text="Momento Fletor (M) em kNm:")
label_momento_fletor.pack(pady=5)
entry_momento_fletor = tk.Entry(root)
entry_momento_fletor.pack(pady=5)

label_dimensao_b = tk.Label(root, text="Dimensão b da seção (cm):")
label_dimensao_b.pack(pady=5)
entry_dimensao_b = tk.Entry(root)
entry_dimensao_b.pack(pady=5)

label_dimensao_h = tk.Label(root, text="Dimensão h da seção (cm):")
label_dimensao_h.pack(pady=5)
entry_dimensao_h = tk.Entry(root)
entry_dimensao_h.pack(pady=5)

label_fck = tk.Label(root, text="Resistência Característica do Concreto (f_ck) em MPa:")
label_fck.pack(pady=5)
entry_fck = tk.Entry(root)
entry_fck.pack(pady=5)

label_fyk = tk.Label(root, text="Resistência Característica do Aço (f_yk) em MPa:")
label_fyk.pack(pady=5)
entry_fyk = tk.Entry(root)
entry_fyk.pack(pady=5)

label_taxa_armadura = tk.Label(root, text="Taxa de Armadura Longitudinal (ρ):")
label_taxa_armadura.pack(pady=5)
entry_taxa_armadura = tk.Entry(root)
entry_taxa_armadura.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_dimensao_coluna)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_dimensao_coluna():
    try:
        # Obtendo os dados de entrada
        N = float(entry_carga_axial.get())
        M = float(entry_momento_fletor.get())
        b = float(entry_dimensao_b.get())
        h = float(entry_dimensao_h.get())
        f_ck = float(entry_fck.get())
        f_yk = float(entry_fyk.get())
        rho = float(entry_taxa_armadura.get())

        # Parâmetros e coeficientes da norma
        gamma_c = 1.4  # Coeficiente de segurança do concreto
        gamma_s = 1.15  # Coeficiente de segurança do aço
        alpha_c = 0.85  # Redutor da resistência à compressão do concreto
        f_cd = f_ck / gamma_c  # Resistência de cálculo do concreto
        f_yd = f_yk / gamma_s  # Resistência de cálculo do aço

        # Área da seção transversal da coluna
        A_c = b * h

        # Área de aço
        A_s = rho * A_c

        # Cálculo da força resistente da coluna (considerando o momento fletor)
        M_rd = (alpha_c * f_cd * b * h**2 / 6) + (A_s * f_yd * (h / 2))

        # Verificação se a coluna está dimensionada adequadamente
        if N <= alpha_c * f_cd * A_c + A_s * f_yd and M <= M_rd:
            resultado = "A coluna está adequadamente dimensionada."
        else:
            resultado = "A coluna não está adequadamente dimensionada."

        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Dimensionamento de Colunas - NBR 6118")

# Labels e entradas para os dados da coluna
label_carga_axial = tk.Label(root, text="Carga Axial (N) em kN:")
label_carga_axial.pack(pady=5)
entry_carga_axial = tk.Entry(root)
entry_carga_axial.pack(pady=5)

label_momento_fletor = tk.Label(root, text="Momento Fletor (M) em kNm:")
label_momento_fletor.pack(pady=5)
entry_momento_fletor = tk.Entry(root)
entry_momento_fletor.pack(pady=5)

label_dimensao_b = tk.Label(root, text="Dimensão b da seção (cm):")
label_dimensao_b.pack(pady=5)
entry_dimensao_b = tk.Entry(root)
entry_dimensao_b.pack(pady=5)

label_dimensao_h = tk.Label(root, text="Dimensão h da seção (cm):")
label_dimensao_h.pack(pady=5)
entry_dimensao_h = tk.Entry(root)
entry_dimensao_h.pack(pady=5)

label_fck = tk.Label(root, text="Resistência Característica do Concreto (f_ck) em MPa:")
label_fck.pack(pady=5)
entry_fck = tk.Entry(root)
entry_fck.pack(pady=5)

label_fyk = tk.Label(root, text="Resistência Característica do Aço (f_yk) em MPa:")
label_fyk.pack(pady=5)
entry_fyk = tk.Entry(root)
entry_fyk.pack(pady=5)

label_taxa_armadura = tk.Label(root, text="Taxa de Armadura Longitudinal (ρ):")
label_taxa_armadura.pack(pady=5)
entry_taxa_armadura = tk.Entry(root)
entry_taxa_armadura.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_dimensao_coluna)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

def calcular_laje():
    try:
        Lx = float(entry_Lx.get())  # Comprimento da laje no eixo x
        Ly = float(entry_Ly.get())  # Comprimento da laje no eixo y
        q = float(entry_q.get())    # Carga distribuída (kN/m²)
        h = float(entry_h.get())    # Espessura da laje (cm)
        fck = float(entry_fck.get()) # Resistência característica do concreto (MPa)
        
        # Convertendo unidades
        q = q * 1000  # Convertendo para N/m²
        h = h / 100  # Convertendo para metros
        
        # Cálculo dos momentos fletores
        Mx = q * Ly**2 / 8  # Momento fletor no eixo x
        My = q * Lx**2 / 8  # Momento fletor no eixo y
        
        # Cálculo das reações de apoio
        Vx = q * Ly / 2
        Vy = q * Lx / 2
        
        # Criando um grid para plotar os resultados
        x = np.linspace(0, Lx, 100)
        y = np.linspace(0, Ly, 100)
        X, Y = np.meshgrid(x, y)
        Zx = (q * (Ly - Y) * Y) / (2 * Lx)
        Zy = (q * (Lx - X) * X) / (2 * Ly)
        
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(x, Zx[int(len(y) / 2)], label='Momento Fletor ao longo de X')
        plt.xlabel('Posição ao longo do eixo X (m)')
        plt.ylabel('Momento Fletor (Nm)')
        plt.legend()
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(y, Zy[int(len(x) / 2)], label='Momento Fletor ao longo de Y')
        plt.xlabel('Posição ao longo do eixo Y (m)')
        plt.ylabel('Momento Fletor (Nm)')
        plt.legend()
        plt.grid()

        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Cálculo de Lajes - Método das Vigas Biapoiadas")

# Labels e entradas para os dados da laje
label_Lx = tk.Label(root, text="Comprimento da Laje no Eixo X (m):")
label_Lx.pack(pady=5)
entry_Lx = tk.Entry(root)
entry_Lx.pack(pady=5)

label_Ly = tk.Label(root, text="Comprimento da Laje no Eixo Y (m):")
label_Ly.pack(pady=5)
entry_Ly = tk.Entry(root)
entry_Ly.pack(pady=5)

label_q = tk.Label(root, text="Carga Distribuída (kN/m²):")
label_q.pack(pady=5)
entry_q = tk.Entry(root)
entry_q.pack(pady=5)

label_h = tk.Label(root, text="Espessura da Laje (cm):")
label_h.pack(pady=5)
entry_h = tk.Entry(root)
entry_h.pack(pady=5)

label_fck = tk.Label(root, text="Resistência Característica do Concreto (f_ck) em MPa:")
label_fck.pack(pady=5)
entry_fck = tk.Entry(root)
entry_fck.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_laje)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_capacidade_estaca():
    try:
        # Obtendo os dados de entrada
        D = float(entry_diametro.get())  # Diâmetro da estaca (m)
        L = float(entry_profundidade.get())  # Comprimento da estaca (m)
        gamma_solo = float(entry_gamma_solo.get())  # Peso específico do solo (kN/m³)
        c_solo = float(entry_coesao_solo.get())  # Coesão do solo (kPa)
        phi_solo = float(entry_phi_solo.get())  # Ângulo de atrito do solo (graus)
        metodo = combo_metodo.get()  # Método de cálculo (Meyerhof ou Terzaghi)

        # Conversão do ângulo de atrito para radianos
        phi_solo_rad = phi_solo * (3.14159265 / 180)

        # Constantes
        N_q = 1 + (1 * (2.71828 ** (3.14159265 * 1 * (0.75 + phi_solo_rad / 2))))
        N_gamma = 2 * (N_q - 1) * (1 / (2 * (1 + (phi_solo_rad / 2))))
        N_c = 0.2 * N_q

        if metodo == 'Meyerhof':
            # Capacidade de carga utilizando o método de Meyerhof
            Q_s = 0.5 * gamma_solo * (N_gamma * D * D)
            Q_b = c_solo * N_c * (D * D)
            Q_total = Q_s + Q_b
        elif metodo == 'Terzaghi':
            # Capacidade de carga utilizando o método de Terzaghi
            Q_s = 0.5 * gamma_solo * L * N_q
            Q_b = c_solo * (N_c * (D * D))
            Q_total = Q_s + Q_b
        else:
            messagebox.showerror("Erro", "Método de cálculo não reconhecido.")
            return

        label_resultado.config(text=f"Capacidade de Carga (Q): {Q_total:.2f} kN")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Capacidade de Carga de Estacas")

# Labels e entradas para os dados das estacas e do solo
label_diametro = tk.Label(root, text="Diâmetro da Estaca (m):")
label_diametro.pack(pady=5)
entry_diametro = tk.Entry(root)
entry_diametro.pack(pady=5)

label_profundidade = tk.Label(root, text="Profundidade da Estaca (m):")
label_profundidade.pack(pady=5)
entry_profundidade = tk.Entry(root)
entry_profundidade.pack(pady=5)

label_gamma_solo = tk.Label(root, text="Peso Específico do Solo (kN/m³):")
label_gamma_solo.pack(pady=5)
entry_gamma_solo = tk.Entry(root)
entry_gamma_solo.pack(pady=5)

label_coesao_solo = tk.Label(root, text="Coesão do Solo (kPa):")
label_coesao_solo.pack(pady=5)
entry_coesao_solo = tk.Entry(root)
entry_coesao_solo.pack(pady=5)

label_phi_solo = tk.Label(root, text="Ângulo de Atrito do Solo (graus):")
label_phi_solo.pack(pady=5)
entry_phi_solo = tk.Entry(root)
entry_phi_solo.pack(pady=5)

label_metodo = tk.Label(root, text="Método de Cálculo:")
label_metodo.pack(pady=5)
combo_metodo = ttk.Combobox(root, values=["Meyerhof", "Terzaghi"])
combo_metodo.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_capacidade_estaca)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

def calcular_estabilidade_talude():
    try:
        # Obtendo os dados de entrada
        phi = float(entry_phi.get())  # Ângulo de atrito interno do solo (graus)
        c = float(entry_c.get())      # Coesão do solo (kPa)
        gamma = float(entry_gamma.get())  # Peso específico do solo (kN/m³)
        H = float(entry_altura.get())     # Altura do talude (m)
        beta = float(entry_inclinacao.get())  # Inclinação do talude (graus)
        metodo = combo_metodo.get()  # Método de cálculo (Mohr-Coulomb ou Bishop)

        # Convertendo ângulo para radianos
        phi_rad = np.deg2rad(phi)
        beta_rad = np.deg2rad(beta)

        # Cálculo dos fatores de segurança
        if metodo == 'Mohr-Coulomb':
            FS = (gamma * H * np.cos(phi_rad) + c * np.sin(phi_rad)) / (gamma * H * np.sin(phi_rad))
        elif metodo == 'Bishop':
            FS = (gamma * H * np.cos(phi_rad) + c * np.sin(phi_rad)) / (gamma * H * np.sin(phi_rad) * np.cos(phi_rad - beta_rad))
        else:
            messagebox.showerror("Erro", "Método de cálculo não reconhecido.")
            return

        label_resultado.config(text=f"Fator de Segurança: {FS:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Análise de Estabilidade de Taludes")

# Labels e entradas para os dados do solo e do talude
label_phi = tk.Label(root, text="Ângulo de Atrito Interno (φ) do Solo (graus):")
label_phi.pack(pady=5)
entry_phi = tk.Entry(root)
entry_phi.pack(pady=5)

label_c = tk.Label(root, text="Coesão do Solo (c) (kPa):")
label_c.pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack(pady=5)

label_gamma = tk.Label(root, text="Peso Específico do Solo (γ) (kN/m³):")
label_gamma.pack(pady=5)
entry_gamma = tk.Entry(root)
entry_gamma.pack(pady=5)

label_altura = tk.Label(root, text="Altura do Talude (H) (m):")
label_altura.pack(pady=5)
entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

label_inclinacao = tk.Label(root, text="Inclinação do Talude (β) (graus):")
label_inclinacao.pack(pady=5)
entry_inclinacao = tk.Entry(root)
entry_inclinacao.pack(pady=5)

label_metodo = tk.Label(root, text="Método de Cálculo:")
label_metodo.pack(pady=5)
combo_metodo = ttk.Combobox(root, values=["Mohr-Coulomb", "Bishop"])
combo_metodo.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_estabilidade_talude)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_permeabilidade():
    try:
        # Obtendo os dados de entrada
        d_tubo = float(entry_d_tubo.get())  # Diâmetro do tubo de permeabilidade (cm)
        area_transversal = float(entry_area_transversal.get())  # Área transversal do solo (cm²)
        h_agua = float(entry_h_agua.get())  # Altura da coluna d'água (cm)
        tempo = float(entry_tempo.get())  # Tempo de coleta (s)

        # Convertendo unidades
        d_tubo /= 100  # Convertendo para metros
        area_transversal /= 10000  # Convertendo para metros quadrados
        h_agua /= 100  # Convertendo para metros

        # Cálculo da permeabilidade
        k = (area_transversal * h_agua) / (d_tubo * tempo)

        label_resultado.config(text=f"Permeabilidade do solo: {k:.6f} m/s")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Cálculo de Permeabilidade do Solo")

# Labels e entradas para os parâmetros do teste de permeabilidade
label_d_tubo = tk.Label(root, text="Diâmetro do Tubo de Permeabilidade (cm):")
label_d_tubo.pack(pady=5)
entry_d_tubo = tk.Entry(root)
entry_d_tubo.pack(pady=5)

label_area_transversal = tk.Label(root, text="Área Transversal do Solo (cm²):")
label_area_transversal.pack(pady=5)
entry_area_transversal = tk.Entry(root)
entry_area_transversal.pack(pady=5)

label_h_agua = tk.Label(root, text="Altura da Coluna d'Água (cm):")
label_h_agua.pack(pady=5)
entry_h_agua = tk.Entry(root)
entry_h_agua.pack(pady=5)

label_tempo = tk.Label(root, text="Tempo de Coleta (s):")
label_tempo.pack(pady=5)
entry_tempo = tk.Entry(root)
entry_tempo.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_permeabilidade)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_recalque():
    try:
        # Obtendo os dados de entrada
        E = float(entry_E.get())  # Módulo de elasticidade do solo (kN/m²)
        Iz = float(entry_Iz.get())  # Momento de inércia do solo (m⁴)
        q = float(entry_q.get())  # Carga aplicada (kN/m²)
        A_fundacao = float(entry_A_fundacao.get())  # Área da fundação (m²)

        # Cálculo do recalque do solo
        recalque = (q * A_fundacao * Iz) / E

        label_resultado.config(text=f"Recalque do solo: {recalque:.6f} m")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
root = tk.Tk()
root.title("Cálculo de Recalque do Solo")

# Labels e entradas para os parâmetros do cálculo de recalque
label_E = tk.Label(root, text="Módulo de Elasticidade do Solo (kN/m²):")
label_E.pack(pady=5)
entry_E = tk.Entry(root)
entry_E.pack(pady=5)

label_Iz = tk.Label(root, text="Momento de Inércia do Solo (m⁴):")
label_Iz.pack(pady=5)
entry_Iz = tk.Entry(root)
entry_Iz.pack(pady=5)

label_q = tk.Label(root, text="Carga Aplicada (kN/m²):")
label_q.pack(pady=5)
entry_q = tk.Entry(root)
entry_q.pack(pady=5)

label_A_fundacao = tk.Label(root, text="Área da Fundação (m²):")
label_A_fundacao.pack(pady=5)
entry_A_fundacao = tk.Entry(root)
entry_A_fundacao.pack(pady=5)

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_recalque)
button_calcular.pack(pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=5)

# Execução do loop principal da interface
root.mainloop()

import math

def calcular_vazao(diametro_tubo, diferenca_altura, viscosidade, densidade):
    """
    Calcula a vazão de um fluido em um tubo.

    Parâmetros:
    - diametro_tubo: Diâmetro do tubo (m)
    - diferenca_altura: Diferença de altura entre as extremidades do tubo (m)
    - viscosidade: Viscosidade dinâmica do fluido (Pa.s)
    - densidade: Densidade do fluido (kg/m³)

    Retorna:
    - vazao: Vazão do fluido no tubo (m³/s)
    """
    area_secao = math.pi * (diametro_tubo/2)**2
    velocidade = math.sqrt(2 * 9.81 * diferenca_altura)
    numero_reynolds = (densidade * velocidade * diametro_tubo) / viscosidade
    if numero_reynolds < 2000:  # Regime laminar
        vazao = (math.pi * (diametro_tubo ** 2) * diferenca_altura) / (8 * viscosidade)
    else:  # Regime turbulento
        vazao = area_secao * velocidade
    return vazao

# Exemplo de uso da função
diametro = 0.1  # m
diferenca_altura = 10  # m
viscosidade_fluido = 1.002e-3  # Pa.s (viscosidade da água a 20°C)
densidade_fluido = 1000  # kg/m³ (densidade da água a 20°C)

vazao_resultante = calcular_vazao(diametro, diferenca_altura, viscosidade_fluido, densidade_fluido)
print("A vazão resultante é:", vazao_resultante, "m³/s")

import math

def calcular_fluxo_darcy_weisbach(diametro, rugosidade, vazao, comprimento):
    """
    Calcula a perda de carga e a velocidade do fluido em uma tubulação utilizando a equação de Darcy-Weisbach.

    Parâmetros:
    - diametro: Diâmetro do tubo (m)
    - rugosidade: Rugosidade do tubo (m)
    - vazao: Vazão do fluido na tubulação (m³/s)
    - comprimento: Comprimento da tubulação (m)

    Retorna:
    - perda_carga: Perda de carga na tubulação (m)
    - velocidade: Velocidade do fluido na tubulação (m/s)
    """
    # Área da seção transversal
    area = math.pi * (diametro / 2) ** 2

    # Cálculo da velocidade do fluido
    velocidade = vazao / area

    # Número de Reynolds
    Reynolds = velocidade * diametro / 1e-6  # Viscosidade cinemática da água a 20°C: 1e-6 m²/s

    # Fator de atrito
    f = 0.079 / (Reynolds ** 0.25)

    # Cálculo da perda de carga
    perda_carga = f * (comprimento / diametro) * (velocidade ** 2) / 2

    return perda_carga, velocidade

# Exemplo de uso da função
diametro_tubo = 0.1  # m
rugosidade_tubo = 0.0002  # m (para tubo de PVC)
vazao_fluido = 0.05  # m³/s
comprimento_tubulacao = 100  # m

perda_carga_resultante, velocidade_resultante = calcular_fluxo_darcy_weisbach(diametro_tubo, rugosidade_tubo, vazao_fluido, comprimento_tubulacao)
print("A perda de carga resultante é:", perda_carga_resultante, "m")
print("A velocidade resultante é:", velocidade_resultante, "m/s")

def calcular_fluxo_manning(largura, profundidade, rugosidade):
    """
    Calcula a vazão e a velocidade média da água em um canal aberto utilizando a equação de Manning.

    Parâmetros:
    - largura: Largura do canal (m)
    - profundidade: Profundidade da água no canal (m)
    - rugosidade: Coeficiente de rugosidade de Manning (adimensional)

    Retorna:
    - vazao: Vazão da água no canal (m³/s)
    - velocidade_media: Velocidade média da água no canal (m/s)
    """
    # Área molhada do canal
    area_molhada = largura * profundidade

    # Raio hidráulico
    raio_hidraulico = area_molhada / (largura + 2 * profundidade)

    # Vazão pela equação de Manning
    vazao = 1.0 / rugosidade * area_molhada * raio_hidraulico ** (2/3) * (0.674 / raio_hidraulico) ** 0.5

    # Velocidade média
    velocidade_media = vazao / area_molhada

    return vazao, velocidade_media

# Exemplo de uso da função
largura_canal = 5  # m
profundidade_agua = 1  # m
rugosidade_manning = 0.03  # coeficiente de rugosidade típico para um canal de concreto

vazao_resultante, velocidade_media_resultante = calcular_fluxo_manning(largura_canal, profundidade_agua, rugosidade_manning)
print("A vazão resultante é:", vazao_resultante, "m³/s")
print("A velocidade média resultante é:", velocidade_media_resultante, "m/s")

def dimensionar_rede_hidraulica(vazao, perda_carga_maxima):
    """
    Dimensiona a rede hidráulica de acordo com a norma NBR 10838.

    Parâmetros:
    - vazao: Vazão total demandada pela rede (m³/s)
    - perda_carga_maxima: Perda de carga máxima permitida na rede (m)

    Retorna:
    - diametro: Diâmetro do tubo a ser utilizado na rede (m)
    """
    # Aqui você implementaria a lógica de dimensionamento conforme a NBR 10838
    # Esta função é apenas um exemplo simplificado e não implementa a lógica completa

    # Por exemplo, você pode calcular o diâmetro do tubo com base na vazão e na perda de carga máxima permitida
    # Aqui, vamos apenas retornar um valor de diâmetro fixo para simplificar o exemplo
    diametro = 0.1  # m (diâmetro fixo)

    return diametro

# Exemplo de uso da função
vazao_total = 0.05  # m³/s
perda_carga_maxima = 5  # m

diametro_tubo = dimensionar_rede_hidraulica(vazao_total, perda_carga_maxima)
print("O diâmetro do tubo recomendado é:", diametro_tubo, "m")

def calcular_dosagem_coagulante(turbidez_agua_bruta, eficiencia_coagulante):
    """
    Calcula a dosagem de coagulante necessária em uma estação de tratamento de água.

    Parâmetros:
    - turbidez_agua_bruta: Turbidez da água bruta (NTU)
    - eficiencia_coagulante: Eficiência do coagulante (adimensional)

    Retorna:
    - dosagem_coagulante: Dosagem de coagulante necessária (mg/L)
    """
    # Aqui você implementaria a lógica para calcular a dosagem de coagulante
    # Esta função é apenas um exemplo simplificado e não implementa a lógica completa

    # Por exemplo, você pode calcular a dosagem com base na turbidez da água bruta e na eficiência do coagulante
    # Aqui, vamos apenas retornar um valor de dosagem fixo para simplificar o exemplo
    dosagem_coagulante = turbidez_agua_bruta * eficiencia_coagulante  # mg/L

    return dosagem_coagulante

# Exemplo de uso da função
turbidez_bruta = 10  # NTU (Nephelometric Turbidity Units)
eficiencia = 0.5  # adimensional (eficiência do coagulante)

dosagem_resultante = calcular_dosagem_coagulante(turbidez_bruta, eficiencia)
print("A dosagem de coagulante necessária é:", dosagem_resultante, "mg/L")

def calcular_dimensionamento_reator(vazao_esgoto, carga_organica):
    """
    Calcula o dimensionamento do reator de ativação por lodo em uma estação de tratamento de esgoto.

    Parâmetros:
    - vazao_esgoto: Vazão do esgoto a ser tratado (m³/s)
    - carga_organica: Carga orgânica do esgoto (kg/dia)

    Retorna:
    - volume_reator: Volume do reator de ativação por lodo (m³)
    """
    # Aqui você implementaria a lógica para calcular o dimensionamento do reator
    # Esta função é apenas um exemplo simplificado e não implementa a lógica completa

    # Por exemplo, você pode calcular o volume do reator com base na carga orgânica e na vazão do esgoto
    # Aqui, vamos apenas retornar um valor de volume fixo para simplificar o exemplo
    volume_reator = vazao_esgoto * 24  # m³ (volume diário necessário)

    return volume_reator

# Exemplo de uso da função
vazao_esgoto = 0.1  # m³/s
carga_organica = 100  # kg/dia

volume_resultante = calcular_dimensionamento_reator(vazao_esgoto, carga_organica)
print("O volume do reator de ativação por lodo é:", volume_resultante, "m³")

import math

def calcular_distancia_entre_pontos(x1, y1, x2, y2):
    """
    Calcula a distância entre dois pontos no plano cartesiano.

    Parâmetros:
    - x1, y1: Coordenadas do primeiro ponto
    - x2, y2: Coordenadas do segundo ponto

    Retorna:
    - distancia: Distância entre os dois pontos
    """
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcular_coordenadas_polares(x1, y1, x2, y2):
    """
    Calcula as coordenadas polares do segundo ponto em relação ao primeiro ponto.

    Parâmetros:
    - x1, y1: Coordenadas do ponto de referência (origem)
    - x2, y2: Coordenadas do ponto de interesse

    Retorna:
    - distancia: Distância entre os dois pontos
    - angulo: Ângulo em relação ao eixo x (em radianos)
    """
    distancia = calcular_distancia_entre_pontos(x1, y1, x2, y2)
    angulo = math.atan2(y2 - y1, x2 - x1)  # Calcula o ângulo em relação ao eixo x
    return distancia, angulo

# Exemplo de uso das funções
x1, y1 = 0, 0
x2, y2 = 3, 4

distancia_resultante = calcular_distancia_entre_pontos(x1, y1, x2, y2)
print("A distância entre os pontos é:", distancia_resultante)

distancia_polar, angulo_polar = calcular_coordenadas_polares(x1, y1, x2, y2)
print("Distância polar:", distancia_polar)
print("Ângulo polar (radianos):", angulo_polar)

def calcular_area_terreno(coordenadas):
    """
    Calcula a área de um terreno fechado com base em suas coordenadas.

    Parâmetros:
    - coordenadas: Lista de tuplas contendo as coordenadas dos vértices do terreno [(x1, y1), (x2, y2), ...]

    Retorna:
    - area: Área do terreno (unidades de área quadradas, como m²)
    """
    area = 0
    n = len(coordenadas)

    # Utiliza a fórmula do método de Gauss para calcular a área
    for i in range(n):
        x1, y1 = coordenadas[i]
        x2, y2 = coordenadas[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2
    return area

# Exemplo de uso da função
coordenadas_terreno = [(0, 0), (0, 5), (3, 5), (3, 0)]  # Exemplo de coordenadas de um terreno retangular
area_terreno = calcular_area_terreno(coordenadas_terreno)
print("A área do terreno é:", area_terreno, "m²")

def calcular_volume_terreno(elevacoes, area_celula):
    """
    Calcula o volume de um terreno representado por uma matriz de elevações.

    Parâmetros:
    - elevacoes: Matriz 2D de elevações do terreno (lista de listas)
    - area_celula: Área de cada célula da grade de elevação (m²)

    Retorna:
    - volume: Volume do terreno (unidades cúbicas, como m³)
    """
    volume = 0

    # Calcula o volume somando as elevações de cada célula multiplicadas pela área da célula
    for linha in elevacoes:
        for elevacao in linha:
            volume += elevacao * area_celula

    return volume

# Exemplo de uso da função
elevacoes_terreno = [
    [10, 20, 30],
    [15, 25, 35],
    [12, 22, 32]
]
area_celula = 10  # m² (área de cada célula da grade de elevação)

volume_terreno = calcular_volume_terreno(elevacoes_terreno, area_celula)
print("O volume do terreno é:", volume_terreno, "m³")

def nivelamento_terreno(pontos, altura_referencia):
    """
    Realiza o nivelamento de um terreno com base em uma série de pontos.

    Parâmetros:
    - pontos: Lista de tuplas contendo as coordenadas (x, y) e as elevações dos pontos
    - altura_referencia: Altura de referência para o nivelamento

    Retorna:
    - pontos_nivelados: Lista de tuplas contendo as coordenadas (x, y) e as elevações dos pontos nivelados
    """
    pontos_nivelados = []

    # Calcula a diferença de altura entre cada ponto e a altura de referência
    for ponto in pontos:
        x, y, altura = ponto
        diferenca_altura = altura_referencia - altura
        pontos_nivelados.append((x, y, altura + diferenca_altura))

    return pontos_nivelados

# Exemplo de uso da função
pontos_terreno = [
    (1, 2, 10),  # (x, y, altura)
    (3, 4, 12),
    (5, 6, 9),
    (7, 8, 11)
]
altura_referencia = 8  # Altura de referência para o nivelamento

pontos_nivelados = nivelamento_terreno(pontos_terreno, altura_referencia)
print("Pontos nivelados:")
for ponto in pontos_nivelados:
    print(ponto)

import math

def calcular_coordenadas_ponto_referencia(x_ref, y_ref, distancia, angulo_horizontal, angulo_vertical):
    """
    Calcula as coordenadas de um ponto de locação com base em um ponto de referência e medições de um teodolito.

    Parâmetros:
    - x_ref, y_ref: Coordenadas do ponto de referência
    - distancia: Distância medida pelo teodolito até o ponto de locação (m)
    - angulo_horizontal: Ângulo horizontal medido pelo teodolito (graus)
    - angulo_vertical: Ângulo vertical medido pelo teodolito (graus)

    Retorna:
    - coordenadas_locacao: Coordenadas do ponto de locação (x, y)
    """
    # Converter ângulos para radianos
    angulo_horizontal_rad = math.radians(angulo_horizontal)
    angulo_vertical_rad = math.radians(angulo_vertical)

    # Calcular deslocamento horizontal e vertical
    deslocamento_horizontal = distancia * math.sin(angulo_horizontal_rad)
    deslocamento_vertical = distancia * math.sin(angulo_vertical_rad)

    # Calcular coordenadas do ponto de locação
    x_loc = x_ref + deslocamento_horizontal
    y_loc = y_ref + deslocamento_vertical

    return x_loc, y_loc

# Exemplo de uso da função
x_referencia = 100  # Coordenada x do ponto de referência
y_referencia = 200  # Coordenada y do ponto de referência
distancia_medida = 50  # Distância medida pelo teodolito até o ponto de locação
angulo_horizontal_medido = 30  # Ângulo horizontal medido pelo teodolito (graus)
angulo_vertical_medido = 45  # Ângulo vertical medido pelo teodolito (graus)

coordenadas_locacao = calcular_coordenadas_ponto_referencia(x_referencia, y_referencia, distancia_medida, angulo_horizontal_medido, angulo_vertical_medido)
print("Coordenadas do ponto de locação:", coordenadas_locacao)

def interpolar_altitude(x1, y1, z1, x2, y2, z2, x_interpolado, y_interpolado):
    """
    Interpola a altitude em um ponto intermediário entre dois pontos de medição conhecidos.

    Parâmetros:
    - x1, y1, z1: Coordenadas e altitude do primeiro ponto de medição
    - x2, y2, z2: Coordenadas e altitude do segundo ponto de medição
    - x_interpolado, y_interpolado: Coordenadas do ponto intermediário para interpolação

    Retorna:
    - z_interpolado: Altitude estimada no ponto intermediário
    """
    # Verifica se os pontos de medição têm a mesma coordenada x ou y
    if x1 == x2:
        z_interpolado = z1 + (z2 - z1) * (y_interpolado - y1) / (y2 - y1)
    elif y1 == y2:
        z_interpolado = z1 + (z2 - z1) * (x_interpolado - x1) / (x2 - x1)
    else:
        # Interpolação linear ponderada
        z_interpolado = z1 + ((z2 - z1) / (x2 - x1)) * (x_interpolado - x1) + ((z2 - z1) / (y2 - y1)) * (y_interpolado - y1)

    return z_interpolado

# Exemplo de uso da função
x1, y1, z1 = 0, 0, 10  # Coordenadas e altitude do primeiro ponto de medição
x2, y2, z2 = 10, 0, 20  # Coordenadas e altitude do segundo ponto de medição
x_interpolado, y_interpolado = 5, 0  # Coordenadas do ponto intermediário para interpolação

z_interpolado = interpolar_altitude(x1, y1, z1, x2, y2, z2, x_interpolado, y_interpolado)
print("Altitude interpolada:", z_interpolado)

