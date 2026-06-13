import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import os

# Cores e estilo
COR_BOTAO = "#2980B9"
COR_BOTAO_HOVER = "#1ABC9C"
COR_FUNDO = "#ECF0F1"
COR_TEXTO = "#FFFFFF"
COR_TITULO = "#2C3E50"

root = tk.Tk()
root.title("Sistema Pessoal")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Tornar a janela menor (300x330)
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x = (largura_tela - 300) // 2
y = (altura_tela - 330) // 2
root.geometry(f"300x330+{x}+{y}")

# Frame principal com padding reduzido
main_frame = tk.Frame(root, bg=COR_FUNDO, padx=15, pady=10)
main_frame.pack(fill="both", expand=True)

# Título compacto
titulo = tk.Label(
    main_frame,
    text="🚀 SISTEMA PESSOAL",
    font=("Arial", 13, "bold"),
    bg=COR_FUNDO,
    fg=COR_TITULO
)
titulo.pack(pady=(0, 8))

# Frame para os botões
botoes_frame = tk.Frame(main_frame, bg=COR_FUNDO)
botoes_frame.pack(expand=True)

def criar_btn(frame, texto, comando, cor=COR_BOTAO, linha=0, coluna=0):
    """Cria um botão compacto"""
    btn = tk.Button(
        frame,
        text=texto,
        font=("Arial", 9),
        bg=cor,
        fg=COR_TEXTO,
        activebackground=COR_BOTAO_HOVER,
        activeforeground=COR_TEXTO,
        relief="flat",
        bd=0,
        padx=8,
        pady=6,
        cursor="hand2",
        width=16,
        command=comando
    )
    btn.grid(row=linha, column=coluna, padx=4, pady=4)

    def on_enter(e): btn.config(bg=COR_BOTAO_HOVER)
    def on_leave(e): btn.config(bg=cor)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

def abrir_vscode():
    try:
        subprocess.Popen(["C:\\Users\\Joaquim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
    except FileNotFoundError:
        messagebox.showerror("Erro", "VS Code não encontrado!")

def abrir_cmd():
    subprocess.Popen("cmd")

def abrir_powershell():
    subprocess.Popen("powershell")

def abrir_navegador():
    try:
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return
        webbrowser.open("https://www.google.com")
    except Exception:
        webbrowser.open("https://www.google.com")

def abrir_calculadora():
    subprocess.Popen("calc")

def abrir_explorador():
    subprocess.Popen("explorer")

def abrir_bloco_notas():
    subprocess.Popen("notepad")

def abrir_gerenciador_tarefas():
    subprocess.Popen("taskmgr")

def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        root.destroy()

# Layout compacto: 4 linhas x 2 colunas
criar_btn(botoes_frame, "💻 VS Code", abrir_vscode, COR_BOTAO, 0, 0)
criar_btn(botoes_frame, "⬛ CMD", abrir_cmd, "#16A085", 0, 1)
criar_btn(botoes_frame, "⚡ PowerShell", abrir_powershell, "#8E44AD", 1, 0)
criar_btn(botoes_frame, "🌐 Navegador", abrir_navegador, "#E67E22", 1, 1)
criar_btn(botoes_frame, "🧮 Calculadora", abrir_calculadora, "#D35400", 2, 0)
criar_btn(botoes_frame, "📁 Explorador", abrir_explorador, "#27AE60", 2, 1)
criar_btn(botoes_frame, "📝 Bloco Notas", abrir_bloco_notas, "#2980B9", 3, 0)
criar_btn(botoes_frame, "⚙️ Gerenciador", abrir_gerenciador_tarefas, "#C0392B", 3, 1)

# Botão Sair compacto
btn_sair = tk.Button(
    botoes_frame,
    text="❌ Sair",
    font=("Arial", 9, "bold"),
    bg="#E74C3C",
    fg=COR_TEXTO,
    activebackground="#C0392B",
    activeforeground=COR_TEXTO,
    relief="flat",
    bd=0,
    padx=8,
    pady=6,
    cursor="hand2",
    width=36,
    command=sair
)
btn_sair.grid(row=4, column=0, columnspan=2, pady=(6, 0))

def on_enter_sair(e): btn_sair.config(bg="#C0392B")
def on_leave_sair(e): btn_sair.config(bg="#E74C3C")
btn_sair.bind("<Enter>", on_enter_sair)
btn_sair.bind("<Leave>", on_leave_sair)

root.mainloop()