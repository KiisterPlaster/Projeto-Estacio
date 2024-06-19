import tkinter as tk
from math import sqrt

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")
        self.tela_inicial = tk.Frame(root)
        self.tela_funcoes = tk.Frame(root)
        self.resultado_label = None
        self.entrada1 = None
        self.entrada2 = None

        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        self.tela_inicial.pack_forget()
        self.tela_funcoes.pack_forget()
        for widget in self.root.winfo_children():
            widget.pack_forget()
        tk.Label(self.root, text="Bem-vindo à Calculadora Básica").pack(pady=10)
        tk.Button(self.root, text="Funções Matemáticas", command=self.mostrar_tela_funcoes).pack(pady=10)

    def mostrar_tela_funcoes(self):
        self.tela_inicial.pack_forget()
        self.tela_funcoes.pack_forget()
        for widget in self.root.winfo_children():
            widget.pack_forget()
        tk.Label(self.root, text="Escolha uma operação").pack(pady=10)
        tk.Button(self.root, text="Soma", command=lambda: self.criar_tela_operacao("Soma", self.calcular_soma)).pack(pady=5)
        tk.Button(self.root, text="Subtração", command=lambda: self.criar_tela_operacao("Subtração", self.calcular_subtracao)).pack(pady=5)
        tk.Button(self.root, text="Multiplicação", command=lambda: self.criar_tela_operacao("Multiplicação", self.calcular_multiplicacao)).pack(pady=5)
        tk.Button(self.root, text="Divisão", command=lambda: self.criar_tela_operacao("Divisão", self.calcular_divisao)).pack(pady=5)
        tk.Button(self.root, text="Potenciação", command=lambda: self.criar_tela_operacao("Potenciação", self.calcular_potenciacao)).pack(pady=5)
        tk.Button(self.root, text="Raiz Quadrada", command=lambda: self.criar_tela_operacao("Raiz Quadrada", self.calcular_raiz_quadrada, dois_argumentos=False)).pack(pady=5)
        tk.Button(self.root, text="Raiz N-ésima", command=lambda: self.criar_tela_operacao("Raiz N-ésima", self.calcular_raiz_n_esima)).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.mostrar_tela_inicial).pack(pady=10)

    def criar_tela_operacao(self, operacao, calcular_funcao, dois_argumentos=True):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        tk.Label(self.root, text=f"Calculadora de {operacao}").pack(pady=10)
        self.entrada1 = tk.Entry(self.root)
        self.entrada1.pack(pady=5)
        if dois_argumentos:
            self.entrada2 = tk.Entry(self.root)
            self.entrada2.pack(pady=5)
        else:
            self.entrada2 = None
        tk.Button(self.root, text="Calcular", command=calcular_funcao).pack(pady=10)
        self.resultado_label = tk.Label(self.root, text="Resultado: ", pady=10)
        self.resultado_label.pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.mostrar_tela_funcoes).pack(pady=10)

    def mostrar_resultado(self, resultado):
        self.resultado_label.config(text=f"Resultado: {resultado}")

    def validar_entrada(self, entry1, entry2=None):
        if not entry1.get():
            self.mostrar_resultado("Erro: campo vazio")
            return False
        try:
            float(entry1.get())
        except ValueError:
            self.mostrar_resultado("Erro: valor inválido")
            return False

        if entry2:
            if not entry2.get():
                self.mostrar_resultado("Erro: campo vazio")
                return False
            try:
                float(entry2.get())
            except ValueError:
                self.mostrar_resultado("Erro: valor inválido")
                return False
        return True

    def calcular_soma(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            self.mostrar_resultado(a + b)

    def calcular_subtracao(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            self.mostrar_resultado(a - b)

    def calcular_multiplicacao(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            self.mostrar_resultado(a * b)

    def calcular_divisao(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            if b == 0:
                self.mostrar_resultado("Erro: divisão por zero")
            else:
                self.mostrar_resultado(a / b)

    def calcular_potenciacao(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            base = float(self.entrada1.get())
            expoente = float(self.entrada2.get())
            self.mostrar_resultado(base ** expoente)

    def calcular_raiz_quadrada(self):
        if self.validar_entrada(self.entrada1):
            numero = float(self.entrada1.get())
            if numero < 0:
                self.mostrar_resultado("Erro: número negativo")
            else:
                self.mostrar_resultado(sqrt(numero))

    def calcular_raiz_n_esima(self):
        if self.validar_entrada(self.entrada1, self.entrada2):
            numero = float(self.entrada1.get())
            indice = float(self.entrada2.get())
            if numero < 0 and indice % 2 == 0:
                self.mostrar_resultado("Erro: índice par para número negativo")
            else:
                self.mostrar_resultado(numero ** (1 / indice))

# Criação da interface gráfica
root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
