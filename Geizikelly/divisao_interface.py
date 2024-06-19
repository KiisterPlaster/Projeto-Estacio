import tkinter as tk
from tkinter import ttk  # Importe ttk para usar Notebook

def divisao(a, b):
    if b == 0:
        return None
    return a / b

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

# Criar a janela principal
janela = tk.Tk()
janela.title("Divisão de Dois Números")

# Widgets para entrada e botão
tk.Label(janela, text="Número A:").pack()
entrada_a_divisao = tk.Entry(janela)
entrada_a_divisao.pack()

tk.Label(janela, text="Número B:").pack()
entrada_b_divisao = tk.Entry(janela)
entrada_b_divisao.pack()

botao_dividir = tk.Button(janela, text="Dividir", command=divisao_interface)
botao_dividir.pack()

label_resultado_divisao = tk.Label(janela, text="Resultado:")
label_resultado_divisao.pack()

# Iniciar o loop principal da interface gráfica
janela.mainloop()
