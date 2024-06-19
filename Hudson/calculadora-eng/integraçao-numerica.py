# Funções para integração numérica
def integral_numerica(funcao_str, a, b, n):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None