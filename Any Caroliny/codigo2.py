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

    def create_numeric_buttons(self):
        for i in range(10):
            if i == 0:
                btn_text = "0"
            else:
                btn_text = str(i)

            btn = tk.Button(self.master, text=btn_text, padx=20, pady=10, font=('Arial', 12), command=lambda num=btn_text: self.append_to_display(num))
            btn.grid(row=(3 - (i-1)//3), column=(i-1)%3, padx=5, pady=5)

    def create_operator_buttons(self):
        operators = ["+", "-", "*", "/", "="]
        row = 1
        col = 3
        for operator in operators:
            if operator == "=":
                btn = tk.Button(self.master, text=operator, padx=20, pady=10, font=('Arial', 12), command=self.calculate)
            else:
                btn = tk.Button(self.master, text=operator, padx=20, pady=10, font=('Arial', 12), command=lambda op=operator: self.append_to_display(op))
            btn.grid(row=row, column=col, padx=5, pady=5)
            row += 1

    def create_clear_button(self):
        btn = tk.Button(self.master, text="C", padx=20, pady=10, font=('Arial', 12), command=self.clear_display)
        btn.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

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

    def calculate(self):
        current = self.display.get()
        try:
            result = eval(current)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular: {e}")

    def clear_display(self):
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
