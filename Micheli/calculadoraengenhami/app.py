import tkinter as tk
from tkinter import Tk
import os
import operacoes_basicas
# Interface gráfica principal
app = Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_operacoes = tk.Frame(app)
aba_operacoes.pack(side="top", fill="both", expand=True)

# Funções para abrir os arquivos correspondentes
def abrir_arquivo_1():
    os.system("start operacoes_basicas.py")

def abrir_arquivo_2():
    os.system("start potenciacao_radificiacao.py")

def abrir_arquivo_3():
    os.system("start funcao_matematica.py")

def abrir_arquivo_4():
    os.system("start operacoes_memoria.py")

def abrir_arquivo_5():
    os.system("start integracao_numerica.py")

def abrir_arquivo_6():
    os.system("start operacoes_fourier.py")

def abrir_arquivo_7():
    os.system("start operacoes_estrututais.py")

def abrir_arquivo_8():
    os.system("start operacoes_mecanicasolos.py")

def abrir_arquivo_9():
    os.system("start operacoes_topografica.py")

def abrir_arquivo_10():
    os.system("start operacoes_interfacegrafica.py")

def abrir_arquivo_11():
    os.system("start operacoes_funcionalidadebasicas.py")

def abrir_arquivo_12():
    os.system("start operacoes_funcionalidadesmemoria.py")

def abrir_arquivo_13():
    os.system("start operacoes_funoesdeengenharia.py")

def abrir_arquivo_14():
    os.system("start operacoes_divisaointerface.py")

def abrir_arquivo_15():
    os.system("start operacoes_compotenciaeraiz.py")

def abrir_arquivo_16():
    os.system("start operacoes_momentofletor.py")

def abrir_arquivo_17():
    os.system("start operacoes_graficacalculomomentofletor.py")

def abrir_arquivo_18():
    os.system("start operacoes.py")

# Você precisa definir as funções para os outros arquivos de maneira semelhante

# Criando botões para cada arquivo de operações
botao_1 = tk.Button(aba_operacoes, text="operacoes_basica.py", command=abrir_arquivo_1)
botao_1.pack()

botao_2 = tk.Button(aba_operacoes, text="potenciacao_radificiacao.py", command=abrir_arquivo_2)
botao_2.pack()

botao_3 = tk.Button(aba_operacoes, text="funcao_matematica.py", command=abrir_arquivo_3)
botao_3.pack()

botao_4 = tk.Button(aba_operacoes, text="operacoes_memoria.py", command=abrir_arquivo_4)
botao_4.pack()

botao_5 = tk.Button(aba_operacoes, text="integracao_numerica.py", command=abrir_arquivo_5)
botao_5.pack()

botao_6 = tk.Button(aba_operacoes, text="operacoes_fourier.py", command=abrir_arquivo_6)
botao_6.pack()

botao_7 = tk.Button(aba_operacoes, text="operacoes_estruturais.py", command=abrir_arquivo_7)
botao_7.pack()

botao_8 = tk.Button(aba_operacoes, text="operacoes_mecanicasolos.py", command=abrir_arquivo_8)
botao_8.pack()

botao_9 = tk.Button(aba_operacoes, text="operacoes_topografica.py", command=abrir_arquivo_9)
botao_9.pack()

botao_10 = tk.Button(aba_operacoes, text="operacoes_interfacegrafica.py", command=abrir_arquivo_10)
botao_10.pack()

botao_11 = tk.Button(aba_operacoes, text="operacoes_funcionalidadebasicas.py", command=abrir_arquivo_11)
botao_11.pack()

botao_12 = tk.Button(aba_operacoes, text="operacoes_funcionalidadesmemoria.py", command=abrir_arquivo_12)
botao_12.pack()

botao_13 = tk.Button(aba_operacoes, text="operacoes_funoesdeengenharia.py", command=abrir_arquivo_13)
botao_13.pack()

botao_14 = tk.Button(aba_operacoes, text="start operacoes_divisaointerface.py", command=abrir_arquivo_14)
botao_14.pack()

botao_15 = tk.Button(aba_operacoes, text="operacoes_compotenciaeraiz.py", command=abrir_arquivo_15)
botao_15.pack()

botao_16 = tk.Button(aba_operacoes, text="operacoes_momentofletor.py", command=abrir_arquivo_16)
botao_16.pack()

botao_17 = tk.Button(aba_operacoes, text="operacoes_graficacalculomomentofletor.py", command=abrir_arquivo_17)
botao_17.pack()

botao_18 = tk.Button(aba_operacoes, text="start operacoes.py", command=abrir_arquivo_18)
botao_18.pack()

# Você precisa criar botões para os outros arquivos de maneira semelhante

# Iniciando a interface gráfica
app.mainloop()
