import tkinter as tk
from tkinter import messagebox


# Preços dos lanches e entregas
PRECOS = {
    'X-Burguer': 8.50,
    'ZipBurguer': 10.50,
    'X-Frango': 14.50,
    'Gringo': 13.00,
}

ENTREGAS = {
    'Entrega (Grátis)': 0.00,
    'Entrega (3)': 3.00,
    'Entrega (5)': 5.00,
    'Entrega (10)': 10.00,
}

# Função para calcular o total
def calcular_total():
    total = 0
    for lanche, quantidade in quantidades.items():
        try:
            qtd = int(quantidade.get())  # Converte a quantidade para inteiro
            total += PRECOS[lanche] * qtd
        except ValueError:
            messagebox.showerror("Erro", "Insira uma quantidade válida para os lanches.")
            return

    entrega = entrega_var.get()
    if entrega:
        total += ENTREGAS[entrega]

    messagebox.showinfo("Total", f"O valor total é: R$ {total:.2f}")

# Interface principal
root = tk.Tk()
root.title("Calculadora de Lanches")

# Aumentar o tamanho da janela
root.geometry("500x500")  # Define o tamanho da janela: largura x altura

# Ajustar a fonte dos widgets
fonte_padrao = ('Arial', 14)

# Frame de lanches (com mais espaçamento e preenchimento)
frame_lanches = tk.LabelFrame(root, text="Lanches", font=fonte_padrao, padx=20, pady=20)
frame_lanches.pack(padx=20, pady=20, fill="both", expand=True)

quantidades = {}
for lanche, preco in PRECOS.items():
    # Label do lanche
    label = tk.Label(frame_lanches, text=f"{lanche} - R$ {preco:.2f}", font=fonte_padrao)
    label.pack(anchor='w', padx=10, pady=10)

    # Entrada de quantidade (largura aumentada)
    quantidade = tk.Entry(frame_lanches, width=10, font=fonte_padrao)
    quantidade.pack(anchor='w', padx=10, pady=10)
    quantidades[lanche] = quantidade

# Frame de entregas (com mais espaçamento e preenchimento)
frame_entregas = tk.LabelFrame(root, text="Entrega", font=fonte_padrao, padx=20, pady=20)
frame_entregas.pack(padx=20, pady=20, fill="both", expand=True)

entrega_var = tk.StringVar(value=None)
for entrega, preco in ENTREGAS.items():
    radio = tk.Radiobutton(frame_entregas, text=f"{entrega} - R$ {preco:.2f}", variable=entrega_var, value=entrega, font=fonte_padrao)
    radio.pack(anchor='w', padx=10, pady=10)

# Botão de calcular (aumentar o tamanho do botão)
btn_calcular = tk.Button(root, text="Calcular Total", command=calcular_total, font=fonte_padrao, width=20)
btn_calcular.pack(pady=20)

root.mainloop()
