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