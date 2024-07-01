import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.create_widgets()

    def create_widgets(self):
        # Display da calculadora
        self.display = tk.Entry(self.master, font=('Arial', 14), width=20, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botões numéricos
        self.create_numeric_buttons()

        # Botões de operações
        self.create_operator_buttons()

        # Botão de limpar
        self.create_clear_button()

        # Botões de funções de engenharia civil
        self.create_engineering_buttons()

    def create_numeric_buttons(self):
        # Criar botões numéricos (0-9)
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0'
        ]
        row = 1
        col = 0
        for button in buttons:
            btn = tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 12), command=lambda num=button: self.append_to_display(num))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 2:
                col = 0
                row += 1

    def create_operator_buttons(self):
        # Criar botões de operações (+, -, *, /, =)
        operators = ["+", "-", "*", "/", "="]
        row = 1
        col = 3
        for operator in operators:
            btn = tk.Button(self.master, text=operator, padx=20, pady=20, font=('Arial', 12), command=lambda op=operator: self.append_to_display(op))
            if operator == "=":
                btn.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
            else:
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                row += 1

    def create_clear_button(self):
        # Criar botão de limpar (C)
        btn = tk.Button(self.master, text="C", padx=20, pady=20, font=('Arial', 12), command=self.clear_display)
        btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_engineering_buttons(self):
        # Criar botões de funções de engenharia civil
        btn_forca_normal = tk.Button(self.master, text="Força Normal", padx=10, pady=20, font=('Arial', 12), command=self.calcular_forca_normal)
        btn_forca_normal.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")

        btn_momento_fletor = tk.Button(self.master, text="Momento Fletor", padx=10, pady=20, font=('Arial', 12), command=self.calcular_momento_fletor)
        btn_momento_fletor.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")

        btn_dimensionamento_coluna = tk.Button(self.master, text="Dimensionar Coluna", padx=10, pady=20, font=('Arial', 12), command=self.calcular_dimensionamento_coluna)
        btn_dimensionamento_coluna.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        btn_dimensionamento_laje = tk.Button(self.master, text="Dimensionar Laje", padx=10, pady=20, font=('Arial', 12), command=self.calcular_dimensionamento_laje)
        btn_dimensionamento_laje.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

    def append_to_display(self, value):
        current = self.display.get()
        if value == "=":
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao calcular: {e}")
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, current + value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calcular_forca_normal(self):
        try:
            n = float(self.display.get())
            a = float(input("Digite a área: "))  # Entrada adicional necessária
            resultado = n / a
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Força Normal: {e}")

    def calcular_momento_fletor(self):
        try:
            f = float(self.display.get())
            l = float(input("Digite o braço de alavanca: "))  # Entrada adicional necessária
            resultado = f * l
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Momento Fletor: {e}")

    def calcular_dimensionamento_coluna(self):
        try:
            fcd = float(self.display.get())
            fck = float(input("Digite a resistência característica do concreto: "))  # Entrada adicional necessária
            resultado = fcd / fck
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Dimensionamento de Coluna: {e}")

    def calcular_dimensionamento_laje(self):
        try:
            f = float(self.display.get())
            a = float(input("Digite a área da laje: "))  # Entrada adicional necessária
            resultado = f / a
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Dimensionamento de Laje: {e}")


# Função principal
def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
