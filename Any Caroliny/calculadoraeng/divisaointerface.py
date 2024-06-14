# Função divisão_interface com tratamento de erros e mensagem para o usuário
from tkinter import messagebox


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

# ... (código restante para outras funções básicas)