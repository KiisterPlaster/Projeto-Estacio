import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraEngenhariaCivil:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Engenharia Civil")
        
        self.create_widgets()

    def create_widgets(self):
        # Frame para a entrada e resultado
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)
        
        self.label_entrada = tk.Label(self.entry_frame, text="Entrada:")
        self.label_entrada.grid(row=0, column=0, padx=10)
        
        self.entry_entrada = tk.Entry(self.entry_frame, width=20)
        self.entry_entrada.grid(row=0, column=1, padx=10)
        
        self.label_resultado = tk.Label(self.entry_frame, text="Resultado:")
        self.label_resultado.grid(row=1, column=0, padx=10)
        
        self.entry_resultado = tk.Entry(self.entry_frame, width=20)
        self.entry_resultado.grid(row=1, column=1, padx=10)
        
        # Frame para botões de operações básicas
        self.operacoes_frame = tk.Frame(self.root)
        self.operacoes_frame.pack(pady=20)
        
        btn_somar = tk.Button(self.operacoes_frame, text="+", width=5, command=lambda: self.calcular('+'))
        btn_somar.grid(row=0, column=0, padx=10)
        
        btn_subtrair = tk.Button(self.operacoes_frame, text="-", width=5, command=lambda: self.calcular('-'))
        btn_subtrair.grid(row=0, column=1, padx=10)
        
        btn_multiplicar = tk.Button(self.operacoes_frame, text="*", width=5, command=lambda: self.calcular('*'))
        btn_multiplicar.grid(row=0, column=2, padx=10)
        
        btn_dividir = tk.Button(self.operacoes_frame, text="/", width=5, command=lambda: self.calcular('/'))
        btn_dividir.grid(row=0, column=3, padx=10)
        
        # Frame para botões de cálculos de Engenharia Civil
        self.engenharia_civil_frame = tk.Frame(self.root)
        
        btn_forca_normal = tk.Button(self.engenharia_civil_frame, text="Força Normal", width=15, command=self.calcular_forca_normal)
        btn_forca_normal.grid(row=0, column=0, padx=10, pady=5)
        
        btn_momento_fletor = tk.Button(self.engenharia_civil_frame, text="Momento Fletor", width=15, command=self.calcular_momento_fletor)
        btn_momento_fletor.grid(row=1, column=0, padx=10, pady=5)
        
        btn_dimensionamento_coluna = tk.Button(self.engenharia_civil_frame, text="Dimens. de Coluna", width=15, command=self.calcular_dimensionamento_coluna)
        btn_dimensionamento_coluna.grid(row=2, column=0, padx=10, pady=5)
        
        btn_dimensionamento_laje = tk.Button(self.engenharia_civil_frame, text="Dimens. de Laje", width=15, command=self.calcular_dimensionamento_laje)
        btn_dimensionamento_laje.grid(row=3, column=0, padx=10, pady=5)
        
        btn_voltar = tk.Button(self.engenharia_civil_frame, text="Voltar", width=15, command=self.voltar_menu_principal)
        btn_voltar.grid(row=4, column=0, padx=10, pady=5)
        
        # Botão para abrir a aba de Engenharia Civil
        btn_engenharia_civil = tk.Button(self.operacoes_frame, text="Engenharia Civil", width=15, command=self.mostrar_engenharia_civil)
        btn_engenharia_civil.grid(row=1, column=0, columnspan=4, pady=10)
        
        # Esconder inicialmente o frame de Engenharia Civil
        self.engenharia_civil_frame.pack_forget()
        
    def calcular(self, operador):
        try:
            expressao = self.entry_entrada.get()
            resultado = eval(expressao)
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular: {str(e)}")
    
    def calcular_forca_normal(self):
        try:
            n = float(self.entry_entrada.get())
            a = float(input("Digite a área: "))
            resultado = n / a
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Força Normal: {str(e)}")
    
    def calcular_momento_fletor(self):
        try:
            f = float(self.entry_entrada.get())
            l = float(input("Digite o braço de alavanca: "))
            resultado = f * l
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Momento Fletor: {str(e)}")
    
    def calcular_dimensionamento_coluna(self):
        try:
            fcd = float(self.entry_entrada.get())
            fck = float(input("Digite a resistência característica do concreto: "))
            resultado = fcd / fck
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Dimensionamento de Coluna: {str(e)}")
    
    def calcular_dimensionamento_laje(self):
        try:
            f = float(self.entry_entrada.get())
            a = float(input("Digite a área da laje: "))
            resultado = f / a
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular Dimensionamento de Laje: {str(e)}")
    
    def mostrar_engenharia_civil(self):
        self.operacoes_frame.pack_forget()
        self.engenharia_civil_frame.pack(pady=20)
    
    def voltar_menu_principal(self):
        self.engenharia_civil_frame.pack_forget()
        self.operacoes_frame.pack(pady=20)
        self.entry_entrada.delete(0, tk.END)
        self.entry_resultado.delete(0, tk.END)

# Função principal
def main():
    root = tk.Tk()
    app = CalculadoraEngenhariaCivil(root)
    root.mainloop()

if __name__ == "__main__":
    main()
