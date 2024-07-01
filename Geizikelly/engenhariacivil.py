import tkinter as tk
from tkinter import messagebox

# Função para calcular momento fletor
def momento_fletor(forca, distancia, tipo_apoio):
    # Implemente sua lógica para calcular o momento fletor aqui
    # Exemplo simplificado:
    if tipo_apoio == "engasta":
        return forca * distancia / 2
    elif tipo_apoio == "bi-apoiada":
        return forca * distancia / 4
    elif tipo_apoio == "encastre-livre":
        return forca * distancia / 3
    else:
        return None

# Função associada ao botão de calcular momento fletor
def calcular_momento_fletor():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o momento fletor.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Cálculo de Momento Fletor")

# Definição dos widgets
tk.Label(root, text="Força (N):").grid(row=0, column=0)
entrada_forca_mf = tk.Entry(root)
entrada_forca_mf.grid(row=0, column=1)

tk.Label(root, text="Distância (m):").grid(row=1, column=0)
entrada_distancia_mf = tk.Entry(root)
entrada_distancia_mf.grid(row=1, column=1)

tk.Label(root, text="Tipo de Apoio:").grid(row=2, column=0)
entrada_tipo_apoio_mf = tk.Entry(root)
entrada_tipo_apoio_mf.grid(row=2, column=1)

tk.Button(root, text="Calcular Momento Fletor", command=calcular_momento_fletor).grid(row=3, column=0, columnspan=2)

label_resultado_mf = tk.Label(root, text="")
label_resultado_mf.grid(row=4, column=0, columnspan=2)

root.mainloop()
