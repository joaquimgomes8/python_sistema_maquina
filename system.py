import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import webbrowser
import os

# Cores e estilo
COR_PRIMARIA = "#2C3E50"
COR_SECUNDARIA = "#3498DB"
COR_BOTAO = "#2980B9"
COR_BOTAO_HOVER = "#1ABC9C"
COR_FUNDO = "#ECF0F1"
COR_TEXTO = "#FFFFFF"
COR_TITULO = "#2C3E50"

root = tk.Tk()
root.title("Sistema Pessoal")
root.geometry("500x500")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Centralizar a janela na tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x = (largura_tela - 500) // 2
y = (altura_tela - 500) // 2
root.geometry(f"500x500+{x}+{y}")

# Frame principal com padding
main_frame = tk.Frame(root, bg=COR_FUNDO, padx=30, pady=20)
main_frame.pack(fill="both", expand=True)

# Título do sistema
titulo = tk.Label(
    main_frame,
    text="🚀 SISTEMA PESSOAL",
    font=("Arial", 20, "bold"),
    bg=COR_FUNDO,
    fg=COR_TITULO
)
titulo.pack(pady=(0, 5))

# Subtítulo
subtitulo = tk.Label(
    main_frame,
    text="Selecione uma ferramenta para abrir",
    font=("Arial", 10),
    bg=COR_FUNDO,
    fg="#7F8C8D"
)
subtitulo.pack(pady=(0, 20))

# Frame para os botões (grid layout)
botoes_frame = tk.Frame(main_frame, bg=COR_FUNDO)
botoes_frame.pack(expand=True)

def criar_botao(frame, texto, comando, cor=COR_BOTAO, linha=0, coluna=0, icone=""):
    """Cria um botão estilizado"""
    btn = tk.Button(
        frame,
        text=f"  {icone}  {texto}",
        font=("Arial", 11, "bold"),
        bg=cor,
        fg=COR_TEXTO,
        activebackground=COR_BOTAO_HOVER,
        activeforeground=COR_TEXTO,
        relief="flat",
        bd=0,
        padx=20,
        pady=12,
        cursor="hand2",
        width=18,
        height=1,
        command=comando
    )
    btn.grid(row=linha, column=coluna, padx=8, pady=8, sticky="ew")

    # Efeito hover (entrar)
    def on_enter(event):
        btn.config(bg=COR_BOTAO_HOVER)

    # Efeito hover (sair)
    def on_leave(event):
        btn.config(bg=cor)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Funções dos botões
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
        # Tenta abrir o Chrome primeiro
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return
        # Fallback: abre o navegador padrão
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

# Linha 1: VS Code e CMD
criar_botao(botoes_frame, "VS Code", abrir_vscode, COR_BOTAO, 0, 0, "💻")
criar_botao(botoes_frame, "CMD", abrir_cmd, "#16A085", 0, 1, "⬛")

# Linha 2: PowerShell e Navegador
criar_botao(botoes_frame, "PowerShell", abrir_powershell, "#8E44AD", 1, 0, "⚡")
criar_botao(botoes_frame, "Navegador", abrir_navegador, "#E67E22", 1, 1, "🌐")

# Linha 3: Calculadora e Explorador
criar_botao(botoes_frame, "Calculadora", abrir_calculadora, "#D35400", 2, 0, "🧮")
criar_botao(botoes_frame, "Explorador", abrir_explorador, "#27AE60", 2, 1, "📁")

# Linha 4: Bloco de Notas e Gerenciador
criar_botao(botoes_frame, "Bloco de Notas", abrir_bloco_notas, "#2980B9", 3, 0, "📝")
criar_botao(botoes_frame, "Gerenciador Tarefas", abrir_gerenciador_tarefas, "#C0392B", 3, 1, "⚙️")

# Linha 5: Botão Sair (ocupa 2 colunas)
btn_sair = tk.Button(
    botoes_frame,
    text="  ❌  Sair",
    font=("Arial", 11, "bold"),
    bg="#E74C3C",
    fg=COR_TEXTO,
    activebackground="#C0392B",
    activeforeground=COR_TEXTO,
    relief="flat",
    bd=0,
    padx=20,
    pady=12,
    cursor="hand2",
    width=40,
    command=sair
)
btn_sair.grid(row=4, column=0, columnspan=2, pady=(15, 0), ipadx=10)

def on_enter_sair(event):
    btn_sair.config(bg="#C0392B")

def on_leave_sair(event):
    btn_sair.config(bg="#E74C3C")

btn_sair.bind("<Enter>", on_enter_sair)
btn_sair.bind("<Leave>", on_leave_sair)

# Rodapé
rodape = tk.Label(
    main_frame,
    text="Desenvolvido por Joaquim © 2026",
    font=("Arial", 8),
    bg=COR_FUNDO,
    fg="#95A5A6"
)
rodape.pack(pady=(15, 0))

root.mainloop()