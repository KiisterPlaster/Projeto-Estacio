import tkinter as tk
from tkinter import messagebox

# Funções para interação com a memória (adicionar, remover, consultar, limpar)
memoria = {}

def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]

def consultar_memoria(nome):
    return memoria.get(nome, None)

def limpar_memoria():
    memoria.clear()

# Funções de interface
def adicionar_memoria_interface():
    nome = entrada_nome_memoria.get()
    valor_str = entrada_valor_memoria.get()
    try:
        valor = float(valor_str)
        adicionar_memoria(nome, valor)
        messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

def remover_memoria_interface():
    nome = entrada_nome_memoria_remover.get()
    remover_memoria(nome)
    messagebox.showinfo("Informação", f"Valor com nome '{nome}' removido da memória.")

def consultar_memoria_interface():
    nome = entrada_nome_memoria_consultar.get()
    valor = consultar_memoria(nome)
    if valor is not None:
        messagebox.showinfo("Informação", f"Valor do nome '{nome}': {valor}")
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria_interface():
    limpar_memoria()
    messagebox.showinfo("Informação", "Memória limpa.")

# Criando a interface gráfica usando Tkinter
root = tk.Tk()
root.title("Gerenciador de Memória")

# Criando uma aba dentro da janela principal
aba_basica = tk.Frame(root)
aba_basica.pack()

# Widgets para adicionar memória
label_nome_memoria = tk.Label(aba_basica, text="Nome:")
label_nome_memoria.pack()
entrada_nome_memoria = tk.Entry(aba_basica)
entrada_nome_memoria.pack()

label_valor_memoria = tk.Label(aba_basica, text="Valor:")
label_valor_memoria.pack()
entrada_valor_memoria = tk.Entry(aba_basica)
entrada_valor_memoria.pack()

botao_adicionar_memoria = tk.Button(aba_basica, text="Adicionar", command=adicionar_memoria_interface)
botao_adicionar_memoria.pack()

# Widgets para remover memória
label_nome_memoria_remover = tk.Label(aba_basica, text="Nome:")
label_nome_memoria_remover.pack()
entrada_nome_memoria_remover = tk.Entry(aba_basica)
entrada_nome_memoria_remover.pack()

botao_remover_memoria = tk.Button(aba_basica, text="Remover", command=remover_memoria_interface)
botao_remover_memoria.pack()

# Widgets para consultar memória
label_nome_memoria_consultar = tk.Label(aba_basica, text="Nome:")
label_nome_memoria_consultar.pack()
entrada_nome_memoria_consultar = tk.Entry(aba_basica)
entrada_nome_memoria_consultar.pack()

botao_consultar_memoria = tk.Button(aba_basica, text="Consultar", command=consultar_memoria_interface)
botao_consultar_memoria.pack()

# Widget para limpar memória
botao_limpar_memoria = tk.Button(aba_basica, text="Limpar Memória", command=limpar_memoria_interface)
botao_limpar_memoria.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
