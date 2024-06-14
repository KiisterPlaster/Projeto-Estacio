# Funções para operações com potências e raízes
def potenciacao_interface():
    try:
        base = float(entrada_base_potenciacao.get()) 
        expoente = float(entrada_expoente_potenciacao.get()) 
        resultado = potenciacao(base, expoente)
        label_resultado_potenciacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

def raiz_quadrada_interface():
    try:
        numero = float(entrada_raiz_quadrada.get())
        resultado = raiz_quadrada(numero)
        if resultado is not None:
            label_resultado_raiz_quadrada.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar um número.")

def raiz_n_esima_interface():
    try:
        numero = float(entrada_raiz_n_esima_numero.get())
        indice = float(entrada_raiz_n_esima_indice.get())
        resultado = raiz_n_esima(numero, indice)
        if resultado is not None:
            label_resultado_raiz_n_esima.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz n-ésima de um número negativo com índice par.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

# ... (código para implementar as interfaces gráficas dessas funções)

# ... (código restante da interface gráfica)

# ... (código anterior para funções básicas e de memória)
