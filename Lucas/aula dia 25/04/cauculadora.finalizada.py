import math

class CivilEngineeringCalculator:

    @staticmethod
    def area_retangulo(largura, altura):
        """Calcula a área de um retângulo"""
        return largura * altura

    @staticmethod
    def area_circulo(raio):
        """Calcula a área de um círculo"""
        return math.pi * raio ** 2

    @staticmethod
    def area_triangulo(base, altura):
        """Calcula a área de um triângulo"""
        return (base * altura) / 2

    @staticmethod
    def volume_paralelepipedo(largura, altura, comprimento):
        """Calcula o volume de um paralelepípedo"""
        return largura * altura * comprimento

    @staticmethod
    def volume_cilindro(raio, altura):
        """Calcula o volume de um cilindro"""
        return math.pi * raio ** 2 * altura

    @staticmethod
    def volume_piramide(base_area, altura):
        """Calcula o volume de uma pirâmide"""
        return (base_area * altura) / 3

    @staticmethod
    def peso_material(volume, densidade):
        """Calcula o peso de um material dado seu volume e densidade"""
        return volume * densidade

# Exemplo de uso:
calc = CivilEngineeringCalculator()

# Cálculos de área
print(f"Área do retângulo: {calc.area_retangulo(5, 10)} m²")
print(f"Área do círculo: {calc.area_circulo(7)} m²")
print(f"Área do triângulo: {calc.area_triangulo(6, 8)} m²")

# Cálculos de volume
print(f"Volume do paralelepípedo: {calc.volume_paralelepipedo(5, 10, 2)} m³")
print(f"Volume do cilindro: {calc.volume_cilindro(7, 10)} m³")
print(f"Volume da pirâmide: {calc.volume_piramide(20, 15)} m³")

# Cálculo de peso de material
print(f"Peso do material: {calc.peso_material(10, 2500)} kg")
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

class CivilEngineeringCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.create_area_frame()
        self.create_volume_frame()
        self.create_weight_frame()

    def create_area_frame(self):
        self.area_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.area_frame, text="Cálculo de Áreas")

        # Widgets for Rectangle Area
        ttk.Label(self.area_frame, text="Área do Retângulo").grid(row=0, column=0, pady=10)
        self.ret_largura = tk.DoubleVar()
        self.ret_altura = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.ret_largura).grid(row=0, column=1)
        ttk.Entry(self.area_frame, textvariable=self.ret_altura).grid(row=0, column=2)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_rectangle_area).grid(row=0, column=3)

        # Widgets for Circle Area
        ttk.Label(self.area_frame, text="Área do Círculo").grid(row=1, column=0, pady=10)
        self.circulo_raio = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.circulo_raio).grid(row=1, column=1)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_circle_area).grid(row=1, column=3)

        # Widgets for Triangle Area
        ttk.Label(self.area_frame, text="Área do Triângulo").grid(row=2, column=0, pady=10)
        self.triangulo_base = tk.DoubleVar()
        self.triangulo_altura = tk.DoubleVar()
        ttk.Entry(self.area_frame, textvariable=self.triangulo_base).grid(row=2, column=1)
        ttk.Entry(self.area_frame, textvariable=self.triangulo_altura).grid(row=2, column=2)
        ttk.Button(self.area_frame, text="Calcular", command=self.calculate_triangle_area).grid(row=2, column=3)

    def create_volume_frame(self):
        self.volume_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.volume_frame, text="Cálculo de Volumes")

        # Widgets for Parallelepiped Volume
        ttk.Label(self.volume_frame, text="Volume do Paralelepípedo").grid(row=0, column=0, pady=10)
        self.paral_largura = tk.DoubleVar()
        self.paral_altura = tk.DoubleVar()
        self.paral_comprimento = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.paral_largura).grid(row=0, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.paral_altura).grid(row=0, column=2)
        ttk.Entry(self.volume_frame, textvariable=self.paral_comprimento).grid(row=0, column=3)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_parallelepiped_volume).grid(row=0, column=4)

        # Widgets for Cylinder Volume
        ttk.Label(self.volume_frame, text="Volume do Cilindro").grid(row=1, column=0, pady=10)
        self.cilindro_raio = tk.DoubleVar()
        self.cilindro_altura = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.cilindro_raio).grid(row=1, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.cilindro_altura).grid(row=1, column=2)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_cylinder_volume).grid(row=1, column=3)

        # Widgets for Pyramid Volume
        ttk.Label(self.volume_frame, text="Volume da Pirâmide").grid(row=2, column=0, pady=10)
        self.piramide_base_area = tk.DoubleVar()
        self.piramide_altura = tk.DoubleVar()
        ttk.Entry(self.volume_frame, textvariable=self.piramide_base_area).grid(row=2, column=1)
        ttk.Entry(self.volume_frame, textvariable=self.piramide_altura).grid(row=2, column=2)
        ttk.Button(self.volume_frame, text="Calcular", command=self.calculate_pyramid_volume).grid(row=2, column=3)

    def create_weight_frame(self):
        self.weight_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.weight_frame, text="Peso do Material")

        # Widgets for Material Weight
        ttk.Label(self.weight_frame, text="Peso do Material").grid(row=0, column=0, pady=10)
        self.material_volume = tk.DoubleVar()
        self.material_densidade = tk.DoubleVar()
        ttk.Entry(self.weight_frame, textvariable=self.material_volume).grid(row=0, column=1)
        ttk.Entry(self.weight_frame, textvariable=self.material_densidade).grid(row=0, column=2)
        ttk.Button(self.weight_frame, text="Calcular", command=self.calculate_material_weight).grid(row=0, column=3)

    def calculate_rectangle_area(self):
        largura = self.ret_largura.get()
        altura = self.ret_altura.get()
        area = CivilEngineeringCalculator.area_retangulo(largura, altura)
        messagebox.showinfo("Resultado", f"Área do Retângulo: {area:.2f} m²")

    def calculate_circle_area(self):
        raio = self.circulo_raio.get()
        area = CivilEngineeringCalculator.area_circulo(raio)
        messagebox.showinfo("Resultado", f"Área do Círculo: {area:.2f} m²")

    def calculate_triangle_area(self):
        base = self.triangulo_base.get()
        altura = self.triangulo_altura.get()
        area = CivilEngineeringCalculator.area_triangulo(base, altura)
        messagebox.showinfo("Resultado", f"Área do Triângulo: {area:.2f} m²")

    def calculate_parallelepiped_volume(self):
        largura = self.paral_largura.get()
        altura = self.paral_altura.get()
        comprimento = self.paral_comprimento.get()
        volume = CivilEngineeringCalculator.volume_paralelepipedo(largura, altura, comprimento)
        messagebox.showinfo("Resultado", f"Volume do Paralelepípedo: {volume:.2f} m³")

    def calculate_cylinder_volume(self):
        raio = self.cilindro_raio.get()
        altura = self.cilindro_altura.get()
        volume = CivilEngineeringCalculator.volume_cilindro(raio, altura)
        messagebox.showinfo("Resultado", f"Volume do Cilindro: {volume:.2f} m³")

    def calculate_pyramid_volume(self):
        base_area = self.piramide_base_area.get()
        altura = self.piramide_altura.get()
        volume = CivilEngineeringCalculator.volume_piramide(base_area, altura)
        messagebox.showinfo("Resultado", f"Volume da Pirâmide: {volume:.2f} m³")

    def calculate_material_weight(self):
        volume = self.material_volume.get()
        densidade = self.material_densidade.get()
        peso = CivilEngineeringCalculator.peso_material(volume, densidade)
        messagebox.showinfo("Resultado", f"Peso do Material: {peso:.2f} kg")

if __name__ == "__main__":
    root = tk.Tk()
    app = CivilEngineeringCalculatorApp(root)
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
import tkinter as tk
import math

class CalculadoraEngenhariaCivil:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")

        # Entrada
        self.entry = tk.Entry(root, width=50, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Botões
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('cos', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('tan', 2, 4), ('log', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4), (')', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3), ('sqrt', 4, 4), ('clear', 4, 5),
            ('pi', 5, 0), ('e', 5, 1), ('x²', 5, 2), ('x³', 5, 3), ('ln', 5, 4), ('=', 5, 5),
            ('Area', 6, 0), ('Volume', 6, 1)
        ]

        for btn_text, row, col in buttons:
            btn = tk.Button(root, text=btn_text, padx=15, pady=10, command=lambda text=btn_text: self.click_btn(text))
            btn.grid(row=row, column=col)

    def click_btn(self, text):
        if text == '=':
            try:
                expression = self.entry.get()
                expression = expression.replace('^', '**')
                expression = expression.replace('pi', str(math.pi))
                expression = expression.replace('e', str(math.e))
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif text == 'clear':
            self.entry.delete(0, tk.END)
        elif text == 'Area':
            self.entry.insert(tk.END, 'Área = ')
        elif text == 'Volume':
            self.entry.insert(tk.END, 'Volume = ')
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calc = CalculadoraEngenhariaCivil(root)
root.mainloop()
import tkinter as tk
import math

class CalculadoraEngenhariaCivil:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")

        # Entrada
        self.entry = tk.Entry(root, width=50, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Botões organizados em grupos
        basic_ops = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('clear', 4, 0)
        ]

        trigonometric_ops = [
            ('sin', 1, 4), ('cos', 1, 5),
            ('tan', 2, 4), ('log', 2, 5),
            ('(', 3, 4), (')', 3, 5)
        ]

        advanced_ops = [
            ('sqrt', 4, 4), ('pi', 5, 0), ('e', 5, 1),
            ('^', 4, 5), ('x²', 5, 2), ('x³', 5, 3),
            ('ln', 5, 4)
        ]

        engineering_ops = [
            ('Area', 6, 0), ('Volume', 6, 1)
        ]

        # Adicionar botões aos grupos
        self.create_buttons(basic_ops)
        self.create_buttons(trigonometric_ops)
        self.create_buttons(advanced_ops)
        self.create_buttons(engineering_ops)

    def create_buttons(self, buttons):
        for btn_text, row, col in buttons:
            btn = tk.Button(self.root, text=btn_text, padx=15, pady=10, command=lambda text=btn_text: self.click_btn(text))
            btn.grid(row=row, column=col)

    def click_btn(self, text):
        if text == '=':
            try:
                expression = self.entry.get()
                expression = expression.replace('^', '**')
                expression = expression.replace('pi', str(math.pi))
                expression = expression.replace('e', str(math.e))
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif text == 'clear':
            self.entry.delete(0, tk.END)
        elif text == 'Area':
            self.entry.insert(tk.END, 'Área = ')
        elif text == 'Volume':
            self.entry.insert(tk.END, 'Volume = ')
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calc = CalculadoraEngenhariaCivil(root)
root.mainloop()
