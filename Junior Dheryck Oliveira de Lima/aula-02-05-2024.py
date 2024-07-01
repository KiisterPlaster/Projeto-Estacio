import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Adicionar botões
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('^', 4, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

        # Criar o menu
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        eng_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Engenharia Civil", menu=eng_menu)
        eng_menu.add_command(label="Área do Círculo", command=self.area_circulo)
        eng_menu.add_command(label="Área do Triângulo", command=self.area_triangulo)
        eng_menu.add_separator()
        eng_menu.add_command(label="Momento em Viga", command=self.momento_viga)
        eng_menu.add_command(label="Carga Máxima em Pilar", command=self.carga_pilar)
        eng_menu.add_separator()
        eng_menu.add_command(label="Vazão em Tubulação", command=self.vazao_tubulacao)
        eng_menu.add_command(label="Velocidade da Água", command=self.velocidade_agua)
        eng_menu.add_separator()
        eng_menu.add_command(label="Lei de Hooke", command=self.lei_hooke)
        eng_menu.add_command(label="Cálculo de Momento Fletor", command=self.calculo_momento_fletor)
        eng_menu.add_command(label="Tensão de Flexão", command=self.tensao_flexao)
        eng_menu.add_command(label="Tensão Efetiva", command=self.tensao_efetiva)
        eng_menu.add_separator()
        eng_menu.add_command(label="Cálculo Água/Cimento", command=self.calculo_agua_cimento)
        eng_menu.add_command(label="Resistência à Compressão", command=self.resistencia_compressao)
        eng_menu.add_separator()
        eng_menu.add_command(label="Equação de Bernoulli", command=self.equacao_bernoulli)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif value == 'sin':
            self.entry.insert(tk.END, "sin(")
        elif value == 'cos':
            self.entry.insert(tk.END, "cos(")
        elif value == 'tan':
            self.entry.insert(tk.END, "tan(")
        else:
            self.entry.insert(tk.END, value)

    def area_circulo(self):
        self.popup_window("Raio do Círculo (m):", self.calculate_area_circulo)

    def calculate_area_circulo(self, raio):
        try:
            raio = float(raio)
            area = 3.14159 * raio**2
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Área do Círculo: {area:.2f} m²")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira um número válido para o raio.")

    def area_triangulo(self):
        self.popup_window("Base do Triângulo (m):", self.get_altura_triangulo)

    def get_altura_triangulo(self, base):
        self.popup_window("Altura do Triângulo (m):", lambda altura: self.calculate_area_triangulo(base, altura))

    def calculate_area_triangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            area = (base * altura) / 2
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Área do Triângulo: {area:.2f} m²")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a base e altura.")

    def momento_viga(self):
        self.popup_window("Força (N):", self.get_distancia_momento)

    def get_distancia_momento(self, forca):
        self.popup_window("Distância (m):", lambda distancia: self.calculate_momento_viga(forca, distancia))

    def calculate_momento_viga(self, forca, distancia):
        try:
            forca = float(forca)
            distancia = float(distancia)
            momento = forca * distancia
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Momento na Viga: {momento:.2f} Nm")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a força e distância.")

    def carga_pilar(self):
        self.popup_window("Área da Secção Transversal do Pilar (m²):", self.get_carga_maxima_pilar)

    def get_carga_maxima_pilar(self, area):
        try:
            area = float(area)
            carga_maxima = 1000 * area  # Assumindo carga máxima de 1000 kN/m² para simplicidade
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Carga Máxima no Pilar: {carga_maxima:.2f} kN")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira um número válido para a área da seção transversal.")

    def vazao_tubulacao(self):
        self.popup_window("Diâmetro da Tubulação (m):", self.get_vazao_tubulacao)

    def get_vazao_tubulacao(self, diametro):
        self.popup_window("Velocidade da Água (m/s):", lambda velocidade: self.calculate_vazao_tubulacao(diametro, velocidade))

    def calculate_vazao_tubulacao(self, diametro, velocidade):
        try:
            diametro = float(diametro)
            velocidade = float(velocidade)
            raio = diametro / 2
            area = 3.14159 * raio**2
            vazao = area * velocidade
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Vazão na Tubulação: {vazao:.2f} m³/s")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para o diâmetro e velocidade.")

    def velocidade_agua(self):
        self.popup_window("Vazão na Tubulação (m³/s):", self.get_velocidade_agua)

    def get_velocidade_agua(self, vazao):
        self.popup_window("Diâmetro da Tubulação (m):", lambda diametro: self.calculate_velocidade_agua(vazao, diametro))

    def calculate_velocidade_agua(self, vazao, diametro):
        try:
            vazao = float(vazao)
            diametro = float(diametro)
            raio = diametro / 2
            area = 3.14159 * raio**2
            velocidade = vazao / area
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Velocidade da Água: {velocidade:.2f} m/s")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a vazão e diâmetro.")

    def lei_hooke(self):
        self.popup_window("Tensão (N/m²):", self.calculate_deformacao_lei_hooke)

    def calculate_deformacao_lei_hooke(self, tensao):
        try:
            tensao = float(tensao)
            deformacao = tensao / 200000  # Módulo de elasticidade do aço típico
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Deformação pela Lei de Hooke: {deformacao:.6f}")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira um número válido para a tensão.")

    def calculo_momento_fletor(self):
        self.popup_window("Força (N):", self.get_distancia_momento_fletor)

    def get_distancia_momento_fletor(self, forca):
        self.popup_window("Distância (m):", lambda distancia: self.calculate_momento_fletor(forca, distancia))

    def calculate_momento_fletor(self, forca, distancia):
        try:
            forca = float(forca)
            distancia = float(distancia)
            momento_fletor = forca * distancia
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Momento Fletor: {momento_fletor:.2f} Nm")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a força e distância.")

    def tensao_flexao(self):
        self.popup_window("Momento Fletor (Nm):", self.get_altura_tensao_flexao)

    def get_altura_tensao_flexao(self, momento):
        self.popup_window("Altura da Seção Transversal (m):", lambda altura: self.calculate_tensao_flexao(momento, altura))

    def calculate_tensao_flexao(self, momento, altura):
        try:
            momento = float(moment)
            altura = float(altura)
            tensao_flexao = momento / (altura * altura / 6)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Tensão de Flexão: {tensao_flexao:.2f} N/m²")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para o momento fletor e altura.")

    def tensao_efetiva(self):
        self.popup_window("Tensão Total (N/m²):", self.get_pressao_intersticial)

    def get_pressao_intersticial(self, tensao_total):
        self.popup_window("Pressão Intersticial (N/m²):", lambda pressao: self.calculate_tensao_efetiva(tensao_total, pressao))

    def calculate_tensao_efetiva(self, tensao_total, pressao_intersticial):
        try:
            tensao_total = float(tensao_total)
            pressao_intersticial = float(pressao_intersticial)
            tensao_efetiva = tensao_total - pressao_intersticial
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Tensão Efetiva: {tensao_efetiva:.2f} N/m²")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a tensão total e pressão intersticial.")

    def calculo_agua_cimento(self):
        self.popup_window("Massa de Água (kg):", self.get_massa_cimento)

    def get_massa_cimento(self, massa_agua):
        self.popup_window("Massa de Cimento (kg):", lambda massa_cimento: self.calculate_agua_cimento(massa_agua, massa_cimento))

    def calculate_agua_cimento(self, massa_agua, massa_cimento):
        try:
            massa_agua = float(massa_agua)
            massa_cimento = float(massa_cimento)
            relacao_agua_cimento = massa_agua / massa_cimento
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Relação Água/Cimento: {relacao_agua_cimento:.2f}")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a massa de água e massa de cimento.")

    def resistencia_compressao(self):
        self.popup_window("Área da Seção Transversal (m²):", self.calculate_resistencia_compressao)

    def calculate_resistencia_compressao(self, area):
        try:
            area = float(area)
            resistencia = 30 * area  # Resistência típica de concreto em N/m²
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Resistência à Compressão: {resistencia:.2f} N/m²")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira um número válido para a área da seção transversal.")

    def equacao_bernoulli(self):
        self.popup_window("Pressão (N/m²):", self.get_densidade_fluido)

    def get_densidade_fluido(self, pressao):
        self.popup_window("Densidade do Fluido (kg/m³):", lambda densidade: self.get_velocidade_fluido(pressao, densidade))

    def get_velocidade_fluido(self, pressao, densidade):
        self.popup_window("Velocidade do Fluido (m/s):", lambda velocidade: self.calculate_equacao_bernoulli(pressao, densidade, velocidade))

    def calculate_equacao_bernoulli(self, pressao, densidade_fluido, velocidade_fluido):
        try:
            pressao = float(pressao)
            densidade_fluido = float(densidade_fluido)
            velocidade_fluido = float(velocidade_fluido)
            altura = pressao / (densidade_fluido * 9.81) + (velocidade_fluido**2) / (2 * 9.81)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, f"Altura do Fluido: {altura:.2f} m")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro: Insira números válidos para a pressão, densidade do fluido e velocidade do fluido.")

    def popup_window(self, message, callback):
        popup = tk.Toplevel()
        popup.title("Informe os Dados")
        label = tk.Label(popup, text=message)
        label.pack(padx=10, pady=10)

        entry = tk.Entry(popup, width=20, borderwidth=3)
        entry.pack(padx=10, pady=10)

        button = tk.Button(popup, text="OK", command=lambda: self.on_ok_button(popup, entry.get(), callback))
        button.pack(padx=10, pady=10)

    def on_ok_button(self, popup, value, callback):
        callback(value)
        popup.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
