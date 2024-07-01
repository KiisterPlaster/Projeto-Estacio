# Funções para funções matemáticas
def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    if math.cos(x) == 0:
        messagebox.showerror("Erro", "Tangente indefinida!")
        return None
    else:
        return math.tan(x)

def logaritmo_natural(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo natural de número não positivo!")
        return None
    else:
        return math.log(x)

def logaritmo_decimal(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo decimal de número não positivo!")
        return None
    else:
        return math.log10(x)