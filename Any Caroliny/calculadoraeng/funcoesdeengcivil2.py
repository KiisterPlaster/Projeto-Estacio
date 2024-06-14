# Funções de Engenharia Civil
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o momento fletor.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")