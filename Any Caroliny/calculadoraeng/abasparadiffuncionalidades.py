# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app)
aba_avancada = tk.Frame(app)
aba_memoria = tk.Frame(app)
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_memoria.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack()

label_a_soma = tk.Label(aba_basica, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = tk.Entry(aba_basica)
entrada_a_soma.pack()

label_b_soma = tk.Label(aba_basica, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = tk.Entry(aba_basica)
entrada_b_soma.pack()

def soma_interface(entrada_a, entrada_b):
    a = float(entrada_a.get())
    b = float(entrada_b.get())
    resultado = a + b
    label_resultado_soma.config(text="Resultado: " + str(resultado))

botao_somar = tk.Button(aba_basica, text="Somar", command=lambda: soma_interface(entrada_a_soma, entrada_b_soma))
botao_somar.pack()

label_resultado_soma = tk.Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = tk.Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack()

# ... (implementar interfaces para integração, derivada e transformada de Fourier)

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")
label_titulo_memoria.pack()

# ... (implementar interfaces para as funções de memória)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil.pack()