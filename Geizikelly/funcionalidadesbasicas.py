from tkinter import *
from tkinter import messagebox

# Functions for mathematical operations
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero!")
    return a / b

# Function definitions for interface operations
def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def subtracao_interface():
    try:
        a = float(entrada_a_subtracao.get())
        b = float(entrada_b_subtracao.get())
        resultado = subtracao(a, b)
        label_resultado_subtracao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def multiplicacao_interface():
    try:
        a = float(entrada_a_multiplicacao.get())
        b = float(entrada_b_multiplicacao.get())
        resultado = multiplicacao(a, b)
        label_resultado_multiplicacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

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

# Tkinter GUI setup
root = Tk()
root.title("Calculadora Básica")

# Create a scrollable frame
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

canvas = Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(fill=BOTH, expand=True)

scrollbar.config(command=canvas.yview)

aba_basica = Frame(canvas)
canvas.create_window((0, 0), window=aba_basica, anchor='nw')

# Addition section
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

# Subtraction section
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

# Multiplication section
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

# Division section
label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_divisao.pack()
entrada_a_divisao = Entry(aba_basica)
entrada_a_divisao.pack()

label_b_divisao = Label(aba_basica, text="Valor de b:")
label_b_divisao.pack()
entrada_b_divisao = Entry(aba_basica)
entrada_b_divisao.pack()

botao_dividir = Button(aba_basica, text="Dividir", command=divisao_interface)
botao_dividir.pack()

label_resultado_divisao = Label(aba_basica, text="Resultado:")
label_resultado_divisao.pack()

# Configure scrollbar to work with canvas
aba_basica.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

# Run the main loop
root.mainloop()
