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
# Função corrigida para resolver sistemas 3x3 com Regra de Cramer
def resolver_cramer_3x3(a, b):
    A = np.array(a).reshape(3, 3)
    B = np.array(b)
    det = np.linalg.det(A)
    if det == 0:
        return "Sistema sem solução única"

    A_x = A.copy()
    A_y = A.copy()
    A_z = A.copy()

    A_x[:, 0] = B
    A_y[:, 1] = B
    A_z[:, 2] = B

    Dx = np.linalg.det(A_x)
    Dy = np.linalg.det(A_y)
    Dz = np.linalg.det(A_z)

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
        coef = valores[0:4]  # a11, a12, a21, a22
        termos = valores[4:6]  # b1, b2
        resultado.set(resolver_cramer_2x2(coef, termos))
    elif tipo == "3x3":
        coef = valores[0:9]  # a11, ..., a33
        termos = valores[9:12]  # b1, b2, b3
        resultado.set(resolver_cramer_3x3(coef, termos))


# Função que cria dinamicamente os campos de entrada com rótulos
def atualizar_interface():
    for widget in frame_campos.winfo_children():
        widget.destroy()
    global entradas
    entradas = []
    tipo = tipo_var.get()

    if tipo == "2x2":
        # Coeficientes
        for i in range(2):
            for j in range(2):
                label = tk.Label(frame_campos, text=f"a{i+1}{j+1}", bg="#1e1e1e", fg="white")
                label.grid(row=i, column=j * 2)
                campo = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white")
                campo.grid(row=i, column=j * 2 + 1)
                entradas.append(campo)
        # Termos independentes
        for i in range(2):
            label = tk.Label(frame_campos, text=f"b{i+1}", bg="#1e1e1e", fg="white")
            label.grid(row=i, column=4)
            campo = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white")
            campo.grid(row=i, column=5)
            entradas.append(campo)

    elif tipo == "3x3":
        # Coeficientes
        for i in range(3):
            for j in range(3):
                label = tk.Label(frame_campos, text=f"a{i+1}{j+1}", bg="#1e1e1e", fg="white")
                label.grid(row=i, column=j * 2)
                campo = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white")
                campo.grid(row=i, column=j * 2 + 1)
                entradas.append(campo)
        # Termos independentes
        for i in range(3):
            label = tk.Label(frame_campos, text=f"b{i+1}", bg="#1e1e1e", fg="white")
            label.grid(row=i, column=6)
            campo = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white")
            campo.grid(row=i, column=7)
            entradas.append(campo)


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
