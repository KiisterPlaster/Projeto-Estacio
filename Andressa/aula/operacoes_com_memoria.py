# Funções para operações com memória
def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")
    

    # Funções de memória
def adicionar_memoria(nome, valor):
    # ... (implementar a lógica para adicionar o valor à memória)

 def remover_memoria(nome):
    # ... (implementar a lógica para remover o valor da memória)

  def consultar_memoria(nome):
    # ... (implementar a lógica para consultar o valor na memória)

   def limpar_memoria():
    # ... (implementar a lógica para limpar a memória)

# Funções de memória
    def adicionar_memoria(nome, valor):
    # ... (implementar a lógica para adicionar o valor à memória)

     def remover_memoria(nome):
    # ... (implementar a lógica para remover o valor da memória)

      def consultar_memoria(nome):
    # ... (implementar a lógica para consultar o valor na memória)

       def limpar_memoria():
    # ... (implementar a lógica para limpar a memória)

# Funções de Engenharia Civil (implementar de acordo com suas necessidades)
        def momento_fletor(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o momento fletor)

         def cortante(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o cortante)

# ... (implementar outras funções de engenharia civil que você desejar)

# Interface gráfica principal
          app = tk.Tk()
app.title("Calculadora Avançada")

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
label_titulo_memoria.pack()

# ... (implementar interfaces para as funções de memória)