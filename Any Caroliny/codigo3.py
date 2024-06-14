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

# Funções de Engenharia Civil (implementar de acordo com suas necessidades)
def momento_fletor(forca, distancia, tipo_apoio):
    # Implementar a lógica para calcular o momento fletor
    pass

def cortante(forca, distancia, tipo_apoio):
    # Implementar a lógica para calcular o cortante
    pass

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

def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

botao_somar = tk.Button(aba_basica, text="Somar", command=soma_interface)
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
label_titulo_engenharia_civil.pack()

# ... (implementar interfaces para as funções de engenharia civil)

app.mainloop()

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
def momento_fletor(forca, distancia, tipo_apoio):
    # Lógica para calcular o momento fletor
    if tipo_apoio == "engasta":
        return forca * distancia
    elif tipo_apoio == "bi-apoiada":
        return forca * distancia / 2
    elif tipo_apoio == "encastre-livre":
        return 0  # Momento é zero em um encontro livre
    else:
        raise ValueError("Tipo de apoio inválido.")

def cortante(forca, distancia, tipo_apoio):
    # Lógica para calcular o cortante
    if tipo_apoio == "engasta":
        return forca
    elif tipo_apoio == "bi-apoiada":
        return forca / 2
    elif tipo_apoio == "encastre-livre":
        return forca  # Cortante é igual à força em um encontro livre
    else:
        raise ValueError("Tipo de apoio inválido.")

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

# Interfaces para as funções básicas (soma, subtração, multiplicação, divisão)

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# Interfaces para as funções avançadas (integração, derivada, transformada de Fourier)

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
label_titulo_memoria.pack()

# Interfaces para as funções de memória (adicionar, remover, consultar, limpar)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")
label_titulo_engenharia_civil.pack()

# Interface para calcular o momento fletor
label_forca_mf = tk.Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = tk.Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = tk.Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = tk.Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = tk.Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = tk.Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack()

def calcular_momento_fletor():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

botao_calcular_mf = tk.Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=calcular_momento_fletor)
botao_calcular_mf.pack()

label_resultado_mf = tk.Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

# Interface para calcular o cortante
label_forca_cortante = tk.Label(aba_engenharia_civil, text="Força (N):")
label_forca_cortante.pack()
entrada_forca_cortante = tk.Entry(aba_engenharia_civil)
entrada_forca_cortante.pack()

label_distancia_cortante = tk.Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_cortante.pack()
entrada_distancia_cortante = tk.Entry(aba_engenharia_civil)
entrada_distancia_cortante.pack()

label_tipo_apoio_cortante = tk.Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_cortante.pack()
entrada_tipo_apoio_cortante = tk.Entry(aba_engenharia_civil)
entrada_tipo_apoio_cortante.pack()

def calcular_cortante():
    try:
        forca = float(entrada_forca_cortante.get())
        distancia = float(entrada_distancia_cortante.get())
        tipo_apoio = entrada_tipo_apoio_cortante.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = cortante(forca, distancia, tipo_apoio)
        label_resultado_cortante.config(text=f"Cortante: {resultado:.4f} N")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

botao_calcular_cortante = tk.Button(aba_engenharia_civil, text="Calcular Cortante", command=calcular_cortante)
botao_calcular_cortante.pack()

label_resultado_cortante = tk.Label(aba_engenharia_civil, text="Resultado:")
label_resultado_cortante.pack()

app.mainloop()

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# Interfaces para as funções avançadas (integração, derivada, transformada de Fourier)

# Interface para calcular a integral
label_funcao_integral = tk.Label(aba_avancada, text="Função a integrar:")
label_funcao_integral.pack()
entrada_funcao_integral = tk.Entry(aba_avancada)
entrada_funcao_integral.pack()

label_limite_inferior_integral = tk.Label(aba_avancada, text="Limite inferior:")
label_limite_inferior_integral.pack()
entrada_limite_inferior_integral = tk.Entry(aba_avancada)
entrada_limite_inferior_integral.pack()

label_limite_superior_integral = tk.Label(aba_avancada, text="Limite superior:")
label_limite_superior_integral.pack()
entrada_limite_superior_integral = tk.Entry(aba_avancada)
entrada_limite_superior_integral.pack()

def calcular_integral():
    try:
        funcao = entrada_funcao_integral.get()
        limite_inferior = float(entrada_limite_inferior_integral.get())
        limite_superior = float(entrada_limite_superior_integral.get())

        # Aqui você pode usar uma biblioteca como sympy ou scipy para calcular a integral
        resultado = calcular_integral_com_sympy(funcao, limite_inferior, limite_superior)
        label_resultado_integral.config(text=f"Integral: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a integral: {e}")

botao_calcular_integral = tk.Button(aba_avancada, text="Calcular Integral", command=calcular_integral)
botao_calcular_integral.pack()

label_resultado_integral = tk.Label(aba_avancada, text="Resultado:")
label_resultado_integral.pack()

# Interface para calcular a derivada
label_funcao_derivada = tk.Label(aba_avancada, text="Função a derivar:")
label_funcao_derivada.pack()
entrada_funcao_derivada = tk.Entry(aba_avancada)
entrada_funcao_derivada.pack()

label_ponto_derivada = tk.Label(aba_avancada, text="Ponto de derivada:")
label_ponto_derivada.pack()
entrada_ponto_derivada = tk.Entry(aba_avancada)
entrada_ponto_derivada.pack()

def calcular_derivada():
    try:
        funcao = entrada_funcao_derivada.get()
        ponto = float(entrada_ponto_derivada.get())

        # Aqui você pode usar uma biblioteca como sympy ou scipy para calcular a derivada
        resultado = calcular_derivada_com_sympy(funcao, ponto)
        label_resultado_derivada.config(text=f"Derivada: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a derivada: {e}")

botao_calcular_derivada = tk.Button(aba_avancada, text="Calcular Derivada", command=calcular_derivada)
botao_calcular_derivada.pack()

label_resultado_derivada = tk.Label(aba_avancada, text="Resultado:")
label_resultado_derivada.pack()

# Outras funcionalidades avançadas podem ser adicionadas aqui, como a transformada de Fourier

# Funções trigonométricas e hiperbólicas
label_titulo_trig_hiper = tk.Label(aba_avancada, text="Funções Trigonométricas e Hiperbólicas")
label_titulo_trig_hiper.pack()

# Interface para calcular seno
label_seno = tk.Label(aba_avancada, text="Seno (em radianos):")
label_seno.pack()
entrada_seno = tk.Entry(aba_avancada)
entrada_seno.pack()

def calcular_seno():
    try:
        valor = float(entrada_seno.get())
        resultado = math.sin(valor)
        label_resultado_seno.config(text=f"Seno: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o seno: {e}")

botao_calcular_seno = tk.Button(aba_avancada, text="Calcular Seno", command=calcular_seno)
botao_calcular_seno.pack()

label_resultado_seno = tk.Label(aba_avancada, text="Resultado:")
label_resultado_seno.pack()

# Interface para calcular cosseno
label_cosseno = tk.Label(aba_avancada, text="Cosseno (em radianos):")
label_cosseno.pack()
entrada_cosseno = tk.Entry(aba_avancada)
entrada_cosseno.pack()

def calcular_cosseno():
    try:
        valor = float(entrada_cosseno.get())
        resultado = math.cos(valor)
        label_resultado_cosseno.config(text=f"Cosseno: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o cosseno: {e}")

botao_calcular_cosseno = tk.Button(aba_avancada, text="Calcular Cosseno", command=calcular_cosseno)
botao_calcular_cosseno.pack()

label_resultado_cosseno = tk.Label(aba_avancada, text="Resultado:")
label_resultado_cosseno.pack()

# Outras operações trigonométricas (tangente, cotangente, secante, cossecante) e hiperbólicas (seno hiperbólico, cosseno hiperbólico, etc.) podem ser adicionadas de maneira semelhante.

# Funções de potência e raiz
label_titulo_potencia_raiz = tk.Label(aba_avancada, text="Funções de Potência e Raiz")
label_titulo_potencia_raiz.pack()

# Interface para calcular potência
label_base_potencia = tk.Label(aba_avancada, text="Base:")
label_base_potencia.pack()
entrada_base_potencia = tk.Entry(aba_avancada)
entrada_base_potencia.pack()

label_expoente_potencia = tk.Label(aba_avancada, text="Expoente:")
label_expoente_potencia.pack()
entrada_expoente_potencia = tk.Entry(aba_avancada)
entrada_expoente_potencia.pack()

def calcular_potencia():
    try:
        base = float(entrada_base_potencia.get())
        expoente = float(entrada_expoente_potencia.get())
        resultado = base ** expoente
        label_resultado_potencia.config(text=f"Potência: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a potência: {e}")

botao_calcular_potencia = tk.Button(aba_avancada, text="Calcular Potência", command=calcular_potencia)
botao_calcular_potencia.pack()

label_resultado_potencia = tk.Label(aba_avancada, text="Resultado:")
label_resultado_potencia.pack()

# Interface para calcular raiz quadrada
label_numero_raiz = tk.Label(aba_avancada, text="Número:")
label_numero_raiz.pack()
entrada_numero_raiz = tk.Entry(aba_avancada)
entrada_numero_raiz.pack()

def calcular_raiz_quadrada():
    try:
        numero = float(entrada_numero_raiz.get())
        resultado = math.sqrt(numero)
        label_resultado_raiz.config(text=f"Raiz Quadrada: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a raiz quadrada: {e}")

botao_calcular_raiz = tk.Button(aba_avancada, text="Calcular Raiz Quadrada", command=calcular_raiz_quadrada)
botao_calcular_raiz.pack()

label_resultado_raiz = tk.Label(aba_avancada, text="Resultado:")
label_resultado_raiz.pack()

# Funções de logaritmo
label_titulo_logaritmos = tk.Label(aba_avancada, text="Funções de Logaritmo")
label_titulo_logaritmos.pack()

# Interface para calcular logaritmo natural
label_numero_log = tk.Label(aba_avancada, text="Número (base e):")
label_numero_log.pack()
entrada_numero_log = tk.Entry(aba_avancada)
entrada_numero_log.pack()

def calcular_log():
    try:
        numero = float(entrada_numero_log.get())
        resultado = math.log(numero)
        label_resultado_log.config(text=f"Logaritmo Natural: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o logaritmo natural: {e}")

botao_calcular_log = tk.Button(aba_avancada, text="Calcular Logaritmo Natural", command=calcular_log)
botao_calcular_log.pack()

label_resultado_log = tk.Label(aba_avancada, text="Resultado:")
label_resultado_log.pack()

# Interface para calcular logaritmo em base 10
label_numero_log10 = tk.Label(aba_avancada, text="Número (base 10):")
label_numero_log10.pack()
entrada_numero_log10 = tk.Entry(aba_avancada)
entrada_numero_log10.pack()

def calcular_log10():
    try:
        numero = float(entrada_numero_log10.get())
        resultado = math.log10(numero)
        label_resultado_log10.config(text=f"Logaritmo Base 10: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o logaritmo em base 10: {e}")

botao_calcular_log10 = tk.Button(aba_avancada, text="Calcular Logaritmo Base 10", command=calcular_log10)
botao_calcular_log10.pack()

label_resultado_log10 = tk.Label(aba_avancada, text="Resultado:")
label_resultado_log10.pack()

# Outras bases de logaritmos podem ser adicionadas de forma semelhante.

# Função de valor absoluto
label_titulo_valor_absoluto = tk.Label(aba_avancada, text="Função de Valor Absoluto")
label_titulo_valor_absoluto.pack()

# Interface para calcular valor absoluto
label_numero_absoluto = tk.Label(aba_avancada, text="Número:")
label_numero_absoluto.pack()
entrada_numero_absoluto = tk.Entry(aba_avancada)
entrada_numero_absoluto.pack()

def calcular_absoluto():
    try:
        numero = float(entrada_numero_absoluto.get())
        resultado = abs(numero)
        label_resultado_absoluto.config(text=f"Valor Absoluto: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o valor absoluto: {e}")

botao_calcular_absoluto = tk.Button(aba_avancada, text="Calcular Valor Absoluto", command=calcular_absoluto)
botao_calcular_absoluto.pack()

label_resultado_absoluto = tk.Label(aba_avancada, text="Resultado:")
label_resultado_absoluto.pack()

# Função de arredondamento
label_titulo_arredondamento = tk.Label(aba_avancada, text="Função de Arredondamento")
label_titulo_arredondamento.pack()

# Interface para arredondar número
label_numero_arredondar = tk.Label(aba_avancada, text="Número:")
label_numero_arredondar.pack()
entrada_numero_arredondar = tk.Entry(aba_avancada)
entrada_numero_arredondar.pack()

def arredondar_numero():
    try:
        numero = float(entrada_numero_arredondar.get())
        resultado = round(numero)
        label_resultado_arredondamento.config(text=f"Número Arredondado: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao arredondar o número: {e}")

botao_arredondar_numero = tk.Button(aba_avancada, text="Arredondar Número", command=arredondar_numero)
botao_arredondar_numero.pack()

label_resultado_arredondamento = tk.Label(aba_avancada, text="Resultado:")
label_resultado_arredondamento.pack()

# Funções trigonométricas
label_titulo_trigonometrico = tk.Label(aba_avancada, text="Funções Trigonométricas")
label_titulo_trigonometrico.pack()

# Interface para calcular seno
label_angulo_seno = tk.Label(aba_avancada, text="Ângulo (em graus):")
label_angulo_seno.pack()
entrada_angulo_seno = tk.Entry(aba_avancada)
entrada_angulo_seno.pack()

def calcular_seno():
    try:
        angulo = float(entrada_angulo_seno.get())
        angulo_radianos = math.radians(angulo)
        resultado = math.sin(angulo_radianos)
        label_resultado_seno.config(text=f"Seno: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o seno: {e}")

botao_calcular_seno = tk.Button(aba_avancada, text="Calcular Seno", command=calcular_seno)
botao_calcular_seno.pack()

label_resultado_seno = tk.Label(aba_avancada, text="Resultado:")
label_resultado_seno.pack()

# Interface para calcular cosseno
label_angulo_cosseno = tk.Label(aba_avancada, text="Ângulo (em graus):")
label_angulo_cosseno.pack()
entrada_angulo_cosseno = tk.Entry(aba_avancada)
entrada_angulo_cosseno.pack()

def calcular_cosseno():
    try:
        angulo = float(entrada_angulo_cosseno.get())
        angulo_radianos = math.radians(angulo)
        resultado = math.cos(angulo_radianos)
        label_resultado_cosseno.config(text=f"Cosseno: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o cosseno: {e}")

botao_calcular_cosseno = tk.Button(aba_avancada, text="Calcular Cosseno", command=calcular_cosseno)
botao_calcular_cosseno.pack()

label_resultado_cosseno = tk.Label(aba_avancada, text="Resultado:")
label_resultado_cosseno.pack()

# Interface para calcular tangente
label_angulo_tangente = tk.Label(aba_avancada, text="Ângulo (em graus):")
label_angulo_tangente.pack()
entrada_angulo_tangente = tk.Entry(aba_avancada)
entrada_angulo_tangente.pack()

def calcular_tangente():
    try:
        angulo = float(entrada_angulo_tangente.get())
        angulo_radianos = math.radians(angulo)
        resultado = math.tan(angulo_radianos)
        label_resultado_tangente.config(text=f"Tangente: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a tangente: {e}")

botao_calcular_tangente = tk.Button(aba_avancada, text="Calcular Tangente", command=calcular_tangente)
botao_calcular_tangente.pack()

label_resultado_tangente = tk.Label(aba_avancada, text="Resultado:")
label_resultado_tangente.pack()
