# Funções para potenciação e radiciação
def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return a ** 0.5

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return a ** (1 / n)