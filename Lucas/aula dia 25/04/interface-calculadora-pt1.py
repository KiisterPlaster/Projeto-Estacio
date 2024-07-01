import tkinter as tk
from math import *

class CalculadoraEngenhariaCivil:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")

        # Entrada
        self.entry = tk.Entry(root, width=50, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botões
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('(', 6, 0), (')', 6, 1), ('^', 6, 2), ('clear', 6, 3),
        ]

        for btn_text, row, col in buttons:
            btn = tk.Button(root, text=btn_text, padx=30, pady=20, command=lambda text=btn_text: self.click_btn(text))
            btn.grid(row=row, column=col)

    def click_btn(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif text == 'clear':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calc = CalculadoraEngenhariaCivil(root)
root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Funções de cálculo
def calcular_momento_fletor(carga, distancia, tipo='simples'):
    if tipo == 'simples':
        momento = (carga * distancia) / 4
    elif tipo == 'engastada':
        momento = (carga * distancia) / 8
    else:
        raise ValueError("Tipo de viga não reconhecido. Use 'simples' ou 'engastada'.")
    return momento

def calcular_area_secao_transversal(largura, altura):
    return largura * altura

def calcular_volume_comprimento(area_secao, comprimento):
    return area_secao * comprimento

def calcular_momento_inercia(largura, altura):
    return (largura * altura**3) / 12

# Funções para atualizar a interface
def calcular():
    try:
        opcao = opcao_var.get()
        if opcao == 1:
            carga = float(entry_carga.get())
            distancia = float(entry_distancia.get())
            tipo = tipo_var.get()
            resultado = calcular_momento_fletor(carga, distancia, tipo)
            messagebox.showinfo("Resultado", f"Momento Fletor: {resultado} Nm")
        
        elif opcao == 2:
            largura = float(entry_largura.get())
            altura = float(entry_altura.get())
            resultado = calcular_area_secao_transversal(largura, altura)
            messagebox.showinfo("Resultado", f"Área da Seção Transversal: {resultado} m²")
        
        elif opcao == 3:
            area_secao = float(entry_area_secao.get())
            comprimento = float(entry_comprimento.get())
            resultado = calcular_volume_comprimento(area_secao, comprimento)
            messagebox.showinfo("Resultado", f"Volume do Elemento Estrutural: {resultado} m³")
        
        elif opcao == 4:
            largura = float(entry_largura_inercia.get())
            altura = float(entry_altura_inercia.get())
            resultado = calcular_momento_inercia(largura, altura)
            messagebox.showinfo("Resultado", f"Momento de Inércia: {resultado} m⁴")
        
        else:
            messagebox.showerror("Erro", "Opção inválida.")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da interface
root = tk.Tk()
root.title("Calculadora de Engenharia Civil")

opcao_var = tk.IntVar()

frame1 = tk.Frame(root)
frame1.pack(pady=10)

tk.Label(frame1, text="Escolha uma opção:").pack()

tk.Radiobutton(frame1, text="Calcular Momento Fletor", variable=opcao_var, value=1).pack(anchor='w')
tk.Radiobutton(frame1, text="Calcular Área de Seção Transversal", variable=opcao_var, value=2).pack(anchor='w')
tk.Radiobutton(frame1, text="Calcular Volume de Elemento Estrutural", variable=opcao_var, value=3).pack(anchor='w')
tk.Radiobutton(frame1, text="Calcular Momento de Inércia de Seção Retangular", variable=opcao_var, value=4).pack(anchor='w')

frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="Carga (N):").grid(row=0, column=0, padx=5, pady=5)
entry_carga = tk.Entry(frame2)
entry_carga.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame2, text="Distância (m):").grid(row=1, column=0, padx=5, pady=5)
entry_distancia = tk.Entry(frame2)
entry_distancia.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame2, text="Tipo de Viga:").grid(row=2, column=0, padx=5, pady=5)
tipo_var = tk.StringVar()
tipo_var.set('simples')
tk.OptionMenu(frame2, tipo_var, 'simples', 'engastada').grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame2, text="Largura (m):").grid(row=3, column=0, padx=5, pady=5)
entry_largura = tk.Entry(frame2)
entry_largura.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame2, text="Altura (m):").grid(row=4, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame2)
entry_altura.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame2, text="Área da Seção (m²):").grid(row=5, column=0, padx=5, pady=5)
entry_area_secao = tk.Entry(frame2)
entry_area_secao.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame2, text="Comprimento (m):").grid(row=6, column=0, padx=5, pady=5)
entry_comprimento = tk.Entry(frame2)
entry_comprimento.grid(row=6, column=1, padx=5, pady=5)

tk.Label(frame2, text="Largura (m) para Momento de Inércia:").grid(row=7, column=0, padx=5, pady=5)
entry_largura_inercia = tk.Entry(frame2)
entry_largura_inercia.grid(row=7, column=1, padx=5, pady=5)

tk.Label(frame2, text="Altura (m) para Momento de Inércia:").grid(row=8, column=0, padx=5, pady=5)
entry_altura_inercia = tk.Entry(frame2)
entry_altura_inercia.grid(row=8, column=1, padx=5, pady=5)

tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

# Funções de cálculo
def calcular_momento_fletor(carga, distancia, tipo='simples'):
    if tipo == 'simples':
        momento = (carga * distancia) / 4
    elif tipo == 'engastada':
        momento = (carga * distancia) / 8
    else:
        raise ValueError("Tipo de viga não reconhecido. Use 'simples' ou 'engastada'.")
    return momento

def calcular_area_secao_transversal(largura, altura):
    return largura * altura

def calcular_volume_comprimento(area_secao, comprimento):
    return area_secao * comprimento

def calcular_momento_inercia(largura, altura):
    return (largura * altura**3) / 12

# Funções para atualizar a interface
def mostrar_campos(*args):
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    opcao = opcao_var.get()
    
    if opcao == "Momento Fletor":
        tk.Label(frame_inputs, text="Carga (N):").grid(row=0, column=0, padx=5, pady=5)
        entry_carga.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Distância (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_distancia.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Tipo de Viga:").grid(row=2, column=0, padx=5, pady=5)
        tipo_var.set('simples')
        tk.OptionMenu(frame_inputs, tipo_var, 'simples', 'engastada').grid(row=2, column=1, padx=5, pady=5)
    
    elif opcao == "Área de Seção Transversal":
        tk.Label(frame_inputs, text="Largura (m):").grid(row=0, column=0, padx=5, pady=5)
        entry_largura.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
    
    elif opcao == "Volume de Elemento Estrutural":
        tk.Label(frame_inputs, text="Área da Seção (m²):").grid(row=0, column=0, padx=5, pady=5)
        entry_area_secao.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Comprimento (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_comprimento.grid(row=1, column=1, padx=5, pady=5)
    
    elif opcao == "Momento de Inércia":
        tk.Label(frame_inputs, text="Largura (m):").grid(row=0, column=0, padx=5, pady=5)
        entry_largura_inercia.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_altura_inercia.grid(row=1, column=1, padx=5, pady=5)

def calcular():
    try:
        opcao = opcao_var.get()
        if opcao == "Momento Fletor":
            carga = float(entry_carga.get())
            distancia = float(entry_distancia.get())
            tipo = tipo_var.get()
            resultado = calcular_momento_fletor(carga, distancia, tipo)
            messagebox.showinfo("Resultado", f"Momento Fletor: {resultado} Nm")
        
        elif opcao == "Área de Seção Transversal":
            largura = float(entry_largura.get())
            altura = float(entry_altura.get())
            resultado = calcular_area_secao_transversal(largura, altura)
            messagebox.showinfo("Resultado", f"Área da Seção Transversal: {resultado} m²")
        
        elif opcao == "Volume de Elemento Estrutural":
            area_secao = float(entry_area_secao.get())
            comprimento = float(entry_comprimento.get())
            resultado = calcular_volume_comprimento(area_secao, comprimento)
            messagebox.showinfo("Resultado", f"Volume do Elemento Estrutural: {resultado} m³")
        
        elif opcao == "Momento de Inércia":
            largura = float(entry_largura_inercia.get())
            altura = float(entry_altura_inercia.get())
            resultado = calcular_momento_inercia(largura, altura)
            messagebox.showinfo("Resultado", f"Momento de Inércia: {resultado} m⁴")
        
        else:
            messagebox.showerror("Erro", "Opção inválida.")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da interface
root = tk.Tk()
root.title("Calculadora de Engenharia Civil")

opcao_var = tk.StringVar()
opcao_var.trace('w', mostrar_campos)

frame_opcao = tk.Frame(root)
frame_opcao.pack(pady=10)

tk.Label(frame_opcao, text="Escolha uma opção:").grid(row=0, column=0, padx=5, pady=5)
opcoes = ["Momento Fletor", "Área de Seção Transversal", "Volume de Elemento Estrutural", "Momento de Inércia"]
tk.OptionMenu(frame_opcao, opcao_var, *opcoes).grid(row=0, column=1, padx=5, pady=5)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

entry_carga = tk.Entry(frame_inputs)
entry_distancia = tk.Entry(frame_inputs)
tipo_var = tk.StringVar()
entry_largura = tk.Entry(frame_inputs)
entry_altura = tk.Entry(frame_inputs)
entry_area_secao = tk.Entry(frame_inputs)
entry_comprimento = tk.Entry(frame_inputs)
entry_largura_inercia = tk.Entry(frame_inputs)
entry_altura_inercia = tk.Entry(frame_inputs)

tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import math

# Funções de cálculo de engenharia civil
def calcular_momento_fletor(carga, distancia, tipo='simples'):
    if tipo == 'simples':
        momento = (carga * distancia) / 4
    elif tipo == 'engastada':
        momento = (carga * distancia) / 8
    else:
        raise ValueError("Tipo de viga não reconhecido. Use 'simples' ou 'engastada'.")
    return momento

def calcular_area_secao_transversal(largura, altura):
    return largura * altura

def calcular_volume_comprimento(area_secao, comprimento):
    return area_secao * comprimento

def calcular_momento_inercia(largura, altura):
    return (largura * altura**3) / 12

# Função para cálculos científicos básicos
def evaluate_expression(event=None):
    try:
        result = eval(entry_expression.get())
        entry_expression.delete(0, tk.END)
        entry_expression.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")

# Função para atualizar a interface com campos de cálculo de engenharia civil
def mostrar_campos(*args):
    for widget in frame_inputs.winfo_children():
        widget.grid_forget()

    opcao = opcao_var.get()
    
    if opcao == "Momento Fletor":
        tk.Label(frame_inputs, text="Carga (N):").grid(row=0, column=0, padx=5, pady=5)
        entry_carga.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Distância (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_distancia.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Tipo de Viga:").grid(row=2, column=0, padx=5, pady=5)
        tipo_var.set('simples')
        tk.OptionMenu(frame_inputs, tipo_var, 'simples', 'engastada').grid(row=2, column=1, padx=5, pady=5)
    
    elif opcao == "Área de Seção Transversal":
        tk.Label(frame_inputs, text="Largura (m):").grid(row=0, column=0, padx=5, pady=5)
        entry_largura.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
    
    elif opcao == "Volume de Elemento Estrutural":
        tk.Label(frame_inputs, text="Área da Seção (m²):").grid(row=0, column=0, padx=5, pady=5)
        entry_area_secao.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Comprimento (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_comprimento.grid(row=1, column=1, padx=5, pady=5)
    
    elif opcao == "Momento de Inércia":
        tk.Label(frame_inputs, text="Largura (m):").grid(row=0, column=0, padx=5, pady=5)
        entry_largura_inercia.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_inputs, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
        entry_altura_inercia.grid(row=1, column=1, padx=5, pady=5)

def calcular():
    try:
        opcao = opcao_var.get()
        if opcao == "Momento Fletor":
            carga = float(entry_carga.get())
            distancia = float(entry_distancia.get())
            tipo = tipo_var.get()
            resultado = calcular_momento_fletor(carga, distancia, tipo)
            messagebox.showinfo("Resultado", f"Momento Fletor: {resultado} Nm")
        
        elif opcao == "Área de Seção Transversal":
            largura = float(entry_largura.get())
            altura = float(entry_altura.get())
            resultado = calcular_area_secao_transversal(largura, altura)
            messagebox.showinfo("Resultado", f"Área da Seção Transversal: {resultado} m²")
        
        elif opcao == "Volume de Elemento Estrutural":
            area_secao = float(entry_area_secao.get())
            comprimento = float(entry_comprimento.get())
            resultado = calcular_volume_comprimento(area_secao, comprimento)
            messagebox.showinfo("Resultado", f"Volume do Elemento Estrutural: {resultado} m³")
        
        elif opcao == "Momento de Inércia":
            largura = float(entry_largura_inercia.get())
            altura = float(entry_altura_inercia.get())
            resultado = calcular_momento_inercia(largura, altura)
            messagebox.showinfo("Resultado", f"Momento de Inércia: {resultado} m⁴")
        
        else:
            messagebox.showerror("Erro", "Opção inválida.")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da interface
root = tk.Tk()
root.title("Calculadora Científica com Engenharia Civil")

# Frame para a calculadora científica
frame_calc = tk.Frame(root)
frame_calc.pack(pady=10)

entry_expression = tk.Entry(frame_calc, width=30, font=("Arial", 14))
entry_expression.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(frame_calc, text=text, command=evaluate_expression).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(frame_calc, text=text, command=lambda t=text: entry_expression.insert(tk.END, t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Frame para seleção de cálculos de engenharia civil
frame_opcao = tk.Frame(root)
frame_opcao.pack(pady=10)

opcao_var = tk.StringVar()
opcao_var.trace('w', mostrar_campos)

tk.Label(frame_opcao, text="Escolha um cálculo de engenharia civil:").grid(row=0, column=0, padx=5, pady=5)
opcoes = ["Momento Fletor", "Área de Seção Transversal", "Volume de Elemento Estrutural", "Momento de Inércia"]
tk.OptionMenu(frame_opcao, opcao_var, *opcoes).grid(row=0, column=1, padx=5, pady=5)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

entry_carga = tk.Entry(frame_inputs)
entry_distancia = tk.Entry(frame_inputs)
tipo_var = tk.StringVar()
entry_largura = tk.Entry(frame_inputs)
entry_altura = tk.Entry(frame_inputs)
entry_area_secao = tk.Entry(frame_inputs)
entry_comprimento = tk.Entry(frame_inputs)
entry_largura_inercia = tk.Entry(frame_inputs)
entry_altura_inercia = tk.Entry(frame_inputs)

tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

root.mainloop()
import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CivilEngineeringCalculator:

    @staticmethod
    def area_retangulo(largura, altura):
        return largura * altura

    @staticmethod
    def area_circulo(raio):
        return math.pi * raio ** 2

    @staticmethod
    def area_triangulo(base, altura):
        return (base * altura) / 2

    @staticmethod
    def volume_paralelepipedo(largura, altura, comprimento):
        return largura * altura * comprimento

    @staticmethod
    def volume_cilindro(raio, altura):
        return math.pi * raio ** 2 * altura

    @staticmethod
    def volume_piramide(base_area, altura):
        return (base_area * altura) / 3

    @staticmethod
    def peso_material(volume, densidade):
        return volume * densidade

    @staticmethod
    def momento_fletor_max(carga, comprimento):
        """Calcula o momento fletor máximo para uma viga simplesmente apoiada com carga uniforme"""
        return (carga * comprimento ** 2) / 8

    @staticmethod
    def tensao_maxima(momento_fletor_max, distancia_neutro, momento_inercia):
        """Calcula a tensão máxima em uma viga simplesmente apoiada"""
        return (momento_fletor_max * distancia_neutro) / momento_inercia

class CivilEngineeringCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.create_selector_frame()
        self.create_area_frame()
        self.create_volume_frame()
        self.create_weight_frame()
        self.create_structural_frame()

    def create_selector_frame(self):
        self.selector_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.selector_frame, text="Seletor")

        ttk.Label(self.selector_frame, text="Selecione o tipo de cálculo:").grid(row=0, column=0, padx=10, pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("Áreas")  # Valor padrão

        operations = ["Áreas", "Volumes", "Peso do Material", "Cálculo Estrutural"]
        self.operation_combobox = ttk.Combobox(self.selector_frame, textvariable=self.operation_var, values=operations, state="readonly")
        self.operation_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.operation_combobox.bind("<<ComboboxSelected>>", self.on_operation_select)

    def on_operation_select(self, event):
        selected_operation = self.operation_var.get()

        if selected_operation == "Áreas":
            self.show_area_frame()
        elif selected_operation == "Volumes":
            self.show_volume_frame()
        elif selected_operation == "Peso do Material":
            self.show_weight_frame()
        elif selected_operation == "Cálculo Estrutural":
            self.show_structural_frame()

    def show_area_frame(self):
        self.hide_all_frames()
        self.area_frame.grid(row=1, column=0, sticky="nsew")

    def show_volume_frame(self):
        self.hide_all_frames()
        self.volume_frame.grid(row=1, column=0, sticky="nsew")

    def show_weight_frame(self):
        self.hide_all_frames()
        self.weight_frame.grid(row=1, column=0, sticky="nsew")

    def show_structural_frame(self):
        self.hide_all_frames()
        self.structural_frame.grid(row=1, column=0, sticky="nsew")

    def hide_all_frames(self):
        self.area_frame.grid_forget()
        self.volume_frame.grid_forget()
        self.weight_frame.grid_forget()
        self.structural_frame.grid_forget()

    def create_area_frame(self):
        self.area_frame = ttk.Frame(self.notebook)

        # Conteúdo do frame de Áreas
        ttk.Label(self.area_frame, text="Área do Retângulo").grid(row=0, column=0, pady=10)
        self.ret_largura = tk.DoubleVar()
        self.ret_altura = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.ret_largura).grid(row=0, column=1)
        ttk.Entry(self.area_frame, textvariable=self.ret_altura).grid(row=0, column=2)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_rectangle_area).grid(row=0, column=3)

        ttk.Label(self.area_frame, text="Área do Círculo").grid(row=1, column=0, pady=10)
        self.circulo_raio = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.circulo_raio).grid(row=1, column=1)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_circle_area).grid(row=1, column=3)

        ttk.Label(self.area_frame, text="Área do Triângulo").grid(row=2, column=0, pady=10)
        self.triangulo_base = tk.DoubleVar()
        self.triangulo_altura = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.triangulo_base).grid(row=2, column=1)
        ttk.Entry(self.area_frame, textvariable=self.triangulo_altura).grid(row=2, column=2)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_triangle_area).grid(row=2, column=3)

        self.notebook.add(self.area_frame, text="Cálculo de Áreas")

    def create_volume_frame(self):
        self.volume_frame = ttk.Frame(self.notebook)

        # Conteúdo do frame de Volumes
        ttk.Label(self.volume_frame, text="Volume do Paralelepípedo").grid(row=0, column=0, pady=10)
        self.paral_largura = tk.DoubleVar()
        self.paral_altura = tk.DoubleVar()
        self.paral_comprimento = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.paral_largura).grid(row=0, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.paral_altura).grid(row=0, column=2)
        ttk.Entry(self.volume_frame, textvariable=self.paral_comprimento).grid(row=0, column=3)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_parallelepiped_volume).grid(row=0, column=4)

        ttk.Label(self.volume_frame, text="Volume do Cilindro").grid(row=1, column=0, pady=10)
        self.cilindro_raio = tk.DoubleVar()
        self.cilindro_altura = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.cilindro_raio).grid(row=1, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.cilindro_altura).grid(row=1, column=2)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_cylinder_volume).grid(row=1, column=3)

        ttk.Label(self.volume_frame, text="Volume da Pirâmide").grid(row=2, column=0, pady=10)
        self.piramide_base_area = tk.DoubleVar()
        self.piramide_altura = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.piramide_base_area).grid(row=2, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.piramide_altura).grid(row=2, column=2)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_pyramid_volume).grid(row=2, column=3)

        self.notebook.add(self.volume_frame, text="Cálculo de Volumes")

    def create_weight_frame(self):
        self.weight_frame = ttk.Frame(self.notebook)

        # Conteúdo do frame de Peso do Material
        ttk.Label(self.weight_frame, text="Peso do Material").grid(row=0, column=0, pady=10)
        self.material_volume = tk.DoubleVar()
        self.material_densidade = tk.DoubleVar()
        ttk.Entry(self.weight_frame, textvariable=self.material_volume).grid(row=0, column=1)
        ttk.Entry(self.weight_frame, textvariable=self.material_densidade).grid(row=0, column=2)
        ttk.Button(self.weight_frame, text="Calcular", command=self.calculate_material_weight).grid(row=0, column=3)

        self.notebook.add(self.weight_frame, text="Peso do Material")

   
