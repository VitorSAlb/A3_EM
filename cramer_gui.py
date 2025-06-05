import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
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

def ler_valores(campos):
    try:
        return [float(campo.get()) for campo in campos]
    except:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return None

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

def atualizar_interface():
    for widget in frame_campos.winfo_children():
        widget.destroy()
    global entradas
    entradas = []
    tipo = tipo_var.get()

    if tipo == "2x2":
        janela.geometry("500x300")
        labels = ["a11", "a12", "a21", "a22", "b1", "b2"]
        posicoes = [(0,0), (0,2), (1,0), (1,2), (0,4), (1,4)]
    elif tipo == "3x3":
        janela.geometry("500x330")
        labels = ["a11", "a12", "a13", "a21", "a22", "a23", "a31", "a32", "a33", "b1", "b2", "b3"]
        posicoes = [
            (0,0), (0,2), (0,4),
            (1,0), (1,2), (1,4),
            (2,0), (2,2), (2,4),
            (0,6), (1,6), (2,6)
        ]

    for i, label in enumerate(labels):
        tk.Label(frame_campos, text=label, bg="#1e1e1e", fg="white", font=("Helvetica", 10, "bold")).grid(
            row=posicoes[i][0], column=posicoes[i][1], padx=5, pady=5, sticky="e"
        )
        entry = tk.Entry(frame_campos, width=5, bg="#2d2d2d", fg="white", insertbackground="white",
                         relief="flat", highlightbackground="#444", highlightthickness=1)
        entry.grid(row=posicoes[i][0], column=posicoes[i][1]+1, padx=5, pady=5)
        entradas.append(entry)

janela = tk.Tk()
janela.title("Calculadora de Sistemas Lineares")
janela.configure(bg="#1e1e1e")
janela.geometry("500x300")
janela.resizable(False, False)

try:
    icone = tk.PhotoImage(file='calc.png')
    janela.iconphoto(False, icone)
except Exception as e:
    print(f"Erro ao carregar ícone: {e}")

def centralizar(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

tk.Label(janela, text="Calculadora de Sistemas Lineares", bg="#1e1e1e", fg="white",
         font=("Helvetica", 16, "bold")).pack(pady=10)

tipo_var = tk.StringVar(value="2x2")
tk.Label(janela, text="Escolha o tipo de sistema:", bg="#1e1e1e", fg="white", font=("Helvetica", 11)).pack(pady=5)

seletor = ttk.Combobox(janela, textvariable=tipo_var, values=["2x2", "3x3"], state="readonly", font=("Helvetica", 10))
seletor.pack(pady=5)

def on_select(event):
    atualizar_interface()
    seletor.selection_clear()

seletor.bind("<<ComboboxSelected>>", on_select)

frame_campos = tk.Frame(janela, bg="#1e1e1e", bd=1, relief="solid")
frame_campos.pack(pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Helvetica", 14, "bold"), bg="#1e1e1e", fg="lime").pack(pady=5)

resolver_btn = tk.Button(janela, text="Resolver", command=resolver,
                         bg="#2d2d2d", fg="white", font=("Helvetica", 11, "bold"),
                         relief="flat", activebackground="#3e3e3e", padx=10, pady=5)
resolver_btn.pack(pady=10)

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox",
                fieldbackground="#2d2d2d",
                background="#2d2d2d",
                foreground="white")

style.map('TCombobox', 
          fieldbackground=[('readonly', '#2d2d2d')],
          foreground=[('readonly', 'white')])

atualizar_interface()
centralizar(janela)

janela.mainloop()