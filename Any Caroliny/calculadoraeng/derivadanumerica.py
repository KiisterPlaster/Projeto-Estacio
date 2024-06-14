# Funções para derivada numérica
from tkinter import messagebox


def derivada_numerica(funcao_str, x, h):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None