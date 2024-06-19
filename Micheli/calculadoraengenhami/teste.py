import tkinter as tk
from tkinter import Tk
import subprocess

# Interface gráfica principal
app = Tk()
app.title("Calculadora Avançada")

# Criando aba para diferentes funcionalidades
aba_operacoes = tk.Frame(app)
aba_operacoes.pack(side="top", fill="both", expand=True)

# Funções para executar os arquivos correspondentes
def executar_arquivo(arquivo):
    try:
        subprocess.Popen(['python', arquivo])
        print(f"Arquivo {arquivo} executado com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o arquivo {arquivo}: {e}")

# Lista dos arquivos a serem executados
arquivos = [
    "operacoes_basicas.py",
    "potenciacao_radificiacao.py",
    "funcao_matematica.py",
    "operacoes_memoria.py",
    "integracao_numerica.py",
    "operacoes_fourier.py",
    "operacoes_estruturais.py",
    "operacoes_mecanicasolos.py",
    "operacoes_topografica.py",
    "operacoes_interfacegrafica.py",
    "operacoes_funcionalidadebasicas.py",
    "operacoes_funcionalidadesmemoria.py",
    "operacoes_funcoesdeengenharia.py",
    "operacoes_divisaointerface.py",
    "operacoes_compotenciaeraiz.py",
    "operacoes_momentofletor.py",
    "operacoes_graficacalculomomentofletor.py",
    "operacoes.py"
]

# Criando botões para cada arquivo de operações
for arquivo in arquivos:
    botao = tk.Button(aba_operacoes, text=arquivo, command=lambda a=arquivo: executar_arquivo(a))
    botao.pack()

# Iniciando a interface gráfica
app.mainloop()
