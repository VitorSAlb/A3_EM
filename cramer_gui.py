import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

# Função para resolver sistemas 2x2 pela Regra de Cramer
def resolver_cramer_2x2(a, b):
    A = np.array(a).reshape(2, 2)
    B = np.array(b)
    det = np.linalg.det(A)
    if det == 0:
        return "Sistema sem solução única"
    Dx = np.linalg.det(np.column_stack((B, A[:,1])))
    Dy = np.linalg.det(np.column_stack((A[:,0], B)))
    x = Dx / det
    y = Dy / det
    return f"x = {x:.2f}, y = {y:.2f}"

# Função para resolver sistemas 3x3 pela Regra de Cramer
def resolver_cramer_3x3(a, b):
    A = np.array(a).reshape(3, 3)
    B = np.array(b)
    det = np.linalg.det(A)
    if det == 0:
        return "Sistema sem solução única"
    Dx = np.linalg.det(np.column_stack((B, A[:,1], A[:,2])))
    Dy = np.linalg.det(np.column_stack((A[:,0], B, A[:,2])))
    Dz = np.linalg.det(np.column_stack((A[:,0], A[:,1], B)))
    x = Dx / det
    y = Dy / det
    z = Dz / det
    return f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}"

# Função que lê os valores digitados nos campos
def ler_valores(campos):
    try:
        return [float(campo.get()) for campo in campos]
    except:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return None

# Função que resolve o sistema com base na escolha
def resolver():
    tipo = tipo_var.get()
    valores = ler_valores(entradas)
    if not valores:
        return
    if tipo == "2x2":
        coef = valores[:4]
        termos = valores[4:]
        resultado.set(resolver_cramer_2x2(coef, termos))
    elif tipo == "3x3":
        coef = valores[:9]
        termos = valores[9:]
        resultado.set(resolver_cramer_3x3(coef, termos))

# Função que cria dinamicamente os campos de entrada com rótulos
def atualizar_interface():
    for widget in frame_campos.winfo_children():
        widget.destroy()
    global entradas
    entradas = []
    tipo = tipo_var.get()
    
    if tipo == "2x2":
        labels = ["a11", "a12", "a21", "a22", "b1", "b2"]
        posicoes = [(0,0), (0,2), (1,0), (1,2), (0,4), (1,4)]
    elif tipo == "3x3":
        labels = ["a11", "a12", "a13", "a21", "a22", "a23", "a31", "a32", "a33", "b1", "b2", "b3"]
        posicoes = [
            (0,0), (0,2), (0,4),
            (1,0), (1,2), (1,4),
            (2,0), (2,2), (2,4),
            (0,6), (1,6), (2,6)
        ]

    for i, label in enumerate(labels):
        tk.Label(frame_campos, text=label, bg="#1e1e1e", fg="white").grid(row=posicoes[i][0], column=posicoes[i][1])
        entry = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white")
        entry.grid(row=posicoes[i][0], column=posicoes[i][1]+1)
        entradas.append(entry)


# Interface principal com tema escuro
janela = tk.Tk()
janela.title("Calculadora de Sistemas Lineares")
janela.configure(bg="#1e1e1e")

tipo_var = tk.StringVar(value="2x2")
tk.Label(janela, text="Escolha o tipo de sistema:", bg="#1e1e1e", fg="white").pack(pady=5)
seletor = ttk.Combobox(janela, textvariable=tipo_var, values=["2x2", "3x3"], state="readonly")
seletor.pack()
seletor.bind("<<ComboboxSelected>>", lambda e: atualizar_interface())

frame_campos = tk.Frame(janela, bg="#1e1e1e")
frame_campos.pack(pady=10)

ttk.Style().theme_use('clam')

tk.Button(janela, text="Resolver", command=resolver).pack(pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Arial", 14), bg="#1e1e1e", fg="lime").pack(pady=5)

atualizar_interface()
janela.mainloop()
