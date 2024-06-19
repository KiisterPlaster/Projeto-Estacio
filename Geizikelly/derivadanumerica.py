import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import sympy as sp

# Funções para derivada numérica
def derivada_numerica(funcao_str, x, h):
    try:
        # Converter a string da função em uma expressão simbólica
        x_sym = sp.symbols('x')
        funcao_expr = sp.sympify(funcao_str)

        # Converter a expressão simbólica em uma função numérica
        funcao = sp.lambdify(x_sym, funcao_expr, 'numpy')

        # Calcular a derivada numérica
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

# Função para transformada de Fourier
def transformada_fourier(sinal):
    try:
        # Verificar se o sinal é um array numpy
        if not isinstance(sinal, np.ndarray):
            raise ValueError("O sinal deve ser um array numpy")
        
        # Calcular a transformada de Fourier
        fourier = np.fft.fft(sinal)
        return fourier
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a transformada de Fourier: {e}")
        return None

# Interface gráfica com Tkinter
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculos de Engenharia")
        self.geometry("600x400")  # Tamanho inicial da janela

        # Configuração da barra de rolagem
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Inicialização do Canvas para suportar rolagem
        self.canvas = tk.Canvas(self, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Ajuste da barra de rolagem para acompanhar o Canvas
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Frame que conterá os botões dentro do Canvas
        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Botões para cada categoria de cálculos
        categorias_calculos = {
            "Hidráulica": {
                "Dimensionamento de Rede Hidráulica": self.calcular_dimensionamento_rede_hidraulica,
                "Tratamento de Água": self.calcular_tratamento_agua,
                "Tratamento de Esgoto": self.calcular_tratamento_esgoto,
                "Fluxo em Tubulação": self.calcular_fluxo_tubulacao,
                "Fluxo em Canal": self.calcular_fluxo_canal
            },
            "Estrutural": {
                "Momento Fletor": self.calcular_momento_fletor,
                "Cortante": self.calcular_cortante,
                "Dimensionamento de Coluna": self.calcular_dimensionamento_coluna,
                "Cálculo de Laje": self.calcular_calculo_laje
            },
            "Solos": {
                "Capacidade de Carga de Estacas": self.calcular_capacidade_carga_estacas,
                "Estabilidade de Talude": self.calcular_estabilidade_talude,
                "Permeabilidade do Solo": self.calcular_permeabilidade_solo,
                "Recalque do Solo": self.calcular_recalque_solo
            }
        }

        # Botão "Cálculos Avançados" para abrir janelas de categorias
        btn_calculos_avancados = ttk.Button(self.inner_frame, text="Cálculos Avançados", command=self.abrir_janela_calculos_avancados)
        btn_calculos_avancados.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Inicializar dicionário para armazenar as janelas secundárias
        self.janelas_secundarias = {}

        # Criar botões para cada funcionalidade dentro das categorias
        row = 1
        for categoria, funcionalidades in categorias_calculos.items():
            lbl_categoria = ttk.Label(self.inner_frame, text=categoria, font=("Arial", 12, "bold"))
            lbl_categoria.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            row += 1
            for funcionalidade, comando in funcionalidades.items():
                btn_funcionalidade = ttk.Button(self.inner_frame, text=funcionalidade, command=comando)
                btn_funcionalidade.grid(row=row, column=0, padx=20, pady=2, sticky="w")

                row += 1

        # Atualizar o tamanho do Canvas
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def abrir_janela_calculos_avancados(self):
        # Verificar se a janela de "Cálculos Avançados" já foi criada
        if 'calculos_avancados' in self.janelas_secundarias:
            self.janelas_secundarias['calculos_avancados'].lift()
        else:
            # Criar nova janela para "Cálculos Avançados"
            self.janelas_secundarias['calculos_avancados'] = tk.Toplevel(self)
            self.janelas_secundarias['calculos_avancados'].title("Cálculos Avançados")

            # Botões para cada categoria de cálculos avançados
            categorias_calculos_avancados = {
                "Derivada Numérica": self.calcular_derivada,
                "Transformada de Fourier": self.calcular_transformada,
                "Força Cortante": self.calcular_cortante,  # Exemplo de cálculo já implementado
                # Adicione outros cálculos avançados aqui
            }

            row = 0
            for nome, comando in categorias_calculos_avancados.items():
                btn_categoria = ttk.Button(self.janelas_secundarias['calculos_avancados'], text=nome, command=comando)
                btn_categoria.grid(row=row, column=0, padx=20, pady=5, sticky="w")
                row += 1

            # Atualizar tamanho da janela
            self.janelas_secundarias['calculos_avancados'].update_idletasks()

    def mostrar_resultado(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    # Funções de cálculo específicas

    def calcular_derivada(self):
        self.tela_derivada = tk.Toplevel(self)
        self.tela_derivada.title("Derivada Numérica")

        # Interface para calcular derivada numérica
        lbl_instrucao = ttk.Label(self.tela_derivada, text="Digite a função f(x):")
        lbl_instrucao.pack(pady=5)

        entry_funcao = ttk.Entry(self.tela_derivada, width=50)
        entry_funcao.insert(0, "x**2 + 2*x + 1")
        entry_funcao.pack(pady=5)

        lbl_x = ttk.Label(self.tela_derivada, text="Valor de x:")
        lbl_x.pack(pady=5)

        entry_x = ttk.Entry(self.tela_derivada, width=20)
        entry_x.insert(0, "1")
        entry_x.pack(pady=5)

        lbl_h = ttk.Label(self.tela_derivada, text="Valor de h:")
        lbl_h.pack(pady=5)

        entry_h = ttk.Entry(self.tela_derivada, width=20)
        entry_h.insert(0, "0.01")
        entry_h.pack(pady=5)

        btn_calcular = ttk.Button(self.tela_derivada, text="Calcular", command=lambda: self.executar_calculo_derivada(entry_funcao.get(), float(entry_x.get()), float(entry_h.get())))
        btn_calcular.pack(pady=10)

        # Área para exibir o resultado
        self.resultado_derivada = ttk.Label(self.tela_derivada, text="", wraplength=300)
        self.resultado_derivada.pack(pady=10)

        btn_voltar = ttk.Button(self.tela_derivada, text="Voltar", command=self.tela_derivada.destroy)
        btn_voltar.pack(pady=10)

    def executar_calculo_derivada(self, funcao_str, x, h):
        resultado = derivada_numerica(funcao_str, x, h)
        if resultado is not None:
            self.resultado_derivada.config(text=f"A derivada numérica da função em x = {x} é {resultado}")

    def calcular_transformada(self):
        self.tela_transformada = tk.Toplevel(self)
        self.tela_transformada.title("Transformada de Fourier")

        # Interface para calcular a transformada de Fourier
        lbl_instrucao = ttk.Label(self.tela_transformada, text="Digite o sinal como um array numpy:")
        lbl_instrucao.pack(pady=5)

        entry_sinal = ttk.Entry(self.tela_transformada, width=50)
        entry_sinal.insert(0, "[0, 1, 0, -1]")
        entry_sinal.pack(pady=5)

        btn_calcular = ttk.Button(self.tela_transformada, text="Calcular", command=lambda: self.executar_calculo_transformada(entry_sinal.get()))
        btn_calcular.pack(pady=10)

        # Área para exibir o resultado
        self.resultado_transformada = ttk.Label(self.tela_transformada, text="", wraplength=300)
        self.resultado_transformada.pack(pady=10)

        btn_voltar = ttk.Button(self.tela_transformada, text="Voltar", command=self.tela_transformada.destroy)
        btn_voltar.pack(pady=10)

    def executar_calculo_transformada(self, sinal_str):
        try:
            # Converter o sinal de string para um array numpy
            sinal = np.array(eval(sinal_str))

            resultado = transformada_fourier(sinal)
            if resultado is not None:
                self.resultado_transformada.config(text=f"Transformada de Fourier do sinal:\n{resultado}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o sinal: {e}")

    def calcular_momento_fletor(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_cortante(self):
        self.tela_cortante = tk.Toplevel(self)
        self.tela_cortante.title("Força Cortante")

        # Interface para calcular a força cortante
        lbl_instrucao = ttk.Label(self.tela_cortante, text="Digite os parâmetros necessários:")
        lbl_instrucao.pack(pady=5)

        lbl_forca = ttk.Label(self.tela_cortante, text="Força aplicada (N):")
        lbl_forca.pack(pady=5)

        entry_forca = ttk.Entry(self.tela_cortante, width=20)
        entry_forca.pack(pady=5)

        lbl_distancia = ttk.Label(self.tela_cortante, text="Distância (m):")
        lbl_distancia.pack(pady=5)

        entry_distancia = ttk.Entry(self.tela_cortante, width=20)
        entry_distancia.pack(pady=5)

        btn_calcular = ttk.Button(self.tela_cortante, text="Calcular", command=lambda: self.executar_calculo_cortante(entry_forca.get(), entry_distancia.get()))
        btn_calcular.pack(pady=10)

        # Área para exibir o resultado
        self.resultado_cortante = ttk.Label(self.tela_cortante, text="", wraplength=300)
        self.resultado_cortante.pack(pady=10)

        btn_voltar = ttk.Button(self.tela_cortante, text="Voltar", command=self.tela_cortante.destroy)
        btn_voltar.pack(pady=10)

    def executar_calculo_cortante(self, forca_str, distancia_str):
        try:
            forca = float(forca_str)
            distancia = float(distancia_str)

            cortante = forca / distancia
            self.resultado_cortante.config(text=f"A força cortante é: {cortante} N/m")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite valores numéricos válidos para força e distância.")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "A distância não pode ser zero.")

    def calcular_forca_normal(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_capacidade_carga_estacas(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_estabilidade_talude(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_permeabilidade_solo(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_recalque_solo(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_fluxo_tubulacao(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_fluxo_canal(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_dimensionamento_rede_hidraulica(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_tratamento_agua(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_tratamento_esgoto(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_area_terreno(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_volume_terreno(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_nivelamento(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_locacao_obra(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_curva_nivel(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_dimensionamento_coluna(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")

    def calcular_calculo_laje(self):
        messagebox.showinfo("Aviso", "Função não implementada ainda.")


# Iniciar a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
