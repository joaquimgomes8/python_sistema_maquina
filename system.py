import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import webbrowser
import os
import time
import threading

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

# Tornar a janela menor (300x400)
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
x = (largura_tela - 300) // 2
y = (altura_tela - 400) // 2
root.geometry(f"300x400+{x}+{y}")

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


# ===== CRONÔMETROS =====
contador_janelas = [0]  # Para dar títulos únicos

def criar_janela_progressivo():
    """Abre uma nova janela independente de cronômetro progressivo"""
    contador_janelas[0] += 1
    n = contador_janelas[0]

    win = tk.Toplevel(root)
    win.title(f"Progressivo #{n}")
    win.geometry("300x210")
    win.configure(bg=COR_FUNDO)
    win.resizable(False, False)

    # Centralizar
    lx = win.winfo_screenwidth()
    ly = win.winfo_screenheight()
    x = (lx - 300) // 2 + n * 30
    y = (ly - 210) // 2 + n * 30
    win.geometry(f"300x210+{x}+{y}")

    frame = tk.Frame(win, bg=COR_FUNDO, padx=15, pady=10)
    frame.pack(expand=True, fill="both")

    # Nome
    lbl_nome = tk.Label(frame, text="Progressivo", font=("Arial", 10, "bold"),
                        bg=COR_FUNDO, fg="#555")
    lbl_nome.pack()

    def renomear():
        resp = simpledialog.askstring("Nome", "Digite o nome:", parent=win)
        if resp:
            lbl_nome.config(text=resp)

    lbl_tempo = tk.Label(frame, text="00:00:00", font=("Arial", 36, "bold"),
                         bg=COR_FUNDO, fg=COR_TITULO)
    lbl_tempo.pack(pady=(5, 8))

    executando = [False]
    segundos = [0]

    def atualizar():
        while executando[0]:
            segundos[0] += 1
            h = segundos[0] // 3600
            m = (segundos[0] % 3600) // 60
            s = segundos[0] % 60
            lbl_tempo.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            time.sleep(1)

    def iniciar():
        if not executando[0]:
            executando[0] = True
            threading.Thread(target=atualizar, daemon=True).start()

    def parar():
        executando[0] = False

    def resetar():
        executando[0] = False
        segundos[0] = 0
        lbl_tempo.config(text="00:00:00")

    btn_frame = tk.Frame(frame, bg=COR_FUNDO)
    btn_frame.pack()

    tk.Button(btn_frame, text="▶ Iniciar", command=iniciar, font=("Arial", 9, "bold"),
              bg="#27AE60", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#1ABC9C", activeforeground="white").grid(row=0, column=0, padx=3)
    tk.Button(btn_frame, text="⏸ Parar", command=parar, font=("Arial", 9, "bold"),
              bg="#E67E22", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#D35400", activeforeground="white").grid(row=0, column=1, padx=3)
    tk.Button(btn_frame, text="↺ Reset", command=resetar, font=("Arial", 9, "bold"),
              bg="#E74C3C", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#C0392B", activeforeground="white").grid(row=0, column=2, padx=3)

    tk.Button(frame, text="✏️ Renomear", command=renomear, font=("Arial", 8),
              bg="#7F8C8D", fg="white", relief="flat", bd=0, padx=8, pady=3, cursor="hand2",
              activebackground="#95A5A6", activeforeground="white").pack(pady=(6, 0))


def criar_janela_regressivo():
    """Abre uma nova janela independente de cronômetro regressivo"""
    contador_janelas[0] += 1
    n = contador_janelas[0]

    win = tk.Toplevel(root)
    win.title(f"Regressivo #{n}")
    win.geometry("320x280")
    win.configure(bg=COR_FUNDO)
    win.resizable(False, False)

    # Centralizar
    lx = win.winfo_screenwidth()
    ly = win.winfo_screenheight()
    x = (lx - 320) // 2 + n * 30
    y = (ly - 280) // 2 + n * 30
    win.geometry(f"320x280+{x}+{y}")

    frame = tk.Frame(win, bg=COR_FUNDO, padx=15, pady=10)
    frame.pack(expand=True, fill="both")

    # Nome
    lbl_nome = tk.Label(frame, text="Regressivo", font=("Arial", 10, "bold"),
                        bg=COR_FUNDO, fg="#555")
    lbl_nome.pack()

    lbl_tempo = tk.Label(frame, text="00:00:00", font=("Arial", 36, "bold"),
                         bg=COR_FUNDO, fg=COR_TITULO)
    lbl_tempo.pack(pady=(3, 3))

    executando = [False]
    segundos_restantes = [0]

    # Spinboxes para HH:MM:SS
    frame_spin = tk.Frame(frame, bg=COR_FUNDO)
    frame_spin.pack(pady=(3, 5))

    tk.Label(frame_spin, text="HH", font=("Arial", 8), bg=COR_FUNDO, fg="#555").grid(row=0, column=0, padx=3)
    tk.Label(frame_spin, text="MM", font=("Arial", 8), bg=COR_FUNDO, fg="#555").grid(row=0, column=1, padx=3)
    tk.Label(frame_spin, text="SS", font=("Arial", 8), bg=COR_FUNDO, fg="#555").grid(row=0, column=2, padx=3)

    spin_h = tk.Spinbox(frame_spin, from_=0, to=99, width=4, font=("Arial", 11), justify="center")
    spin_m = tk.Spinbox(frame_spin, from_=0, to=59, width=4, font=("Arial", 11), justify="center")
    spin_s = tk.Spinbox(frame_spin, from_=0, to=59, width=4, font=("Arial", 11), justify="center")

    spin_h.grid(row=1, column=0, padx=3)
    spin_m.grid(row=1, column=1, padx=3)
    spin_s.grid(row=1, column=2, padx=3)

    tk.Label(frame_spin, text=":", font=("Arial", 14, "bold"), bg=COR_FUNDO, fg=COR_TITULO).grid(row=1, column=0, sticky="e", padx=(0, -10))
    tk.Label(frame_spin, text=":", font=("Arial", 14, "bold"), bg=COR_FUNDO, fg=COR_TITULO).grid(row=1, column=1, sticky="e", padx=(0, -10))

    def aplicar_tempo():
        try:
            h = int(spin_h.get())
            m = int(spin_m.get())
            s = int(spin_s.get())
            total = h * 3600 + m * 60 + s
            if total == 0:
                messagebox.showwarning("Aviso", "Defina pelo menos 1 segundo!", parent=win)
                return
            segundos_restantes[0] = total
            lbl_tempo.config(text=f"{h:02d}:{m:02d}:{s:02d}", fg=COR_TITULO)
        except ValueError:
            messagebox.showwarning("Erro", "Valores inválidos!", parent=win)

    def atualizar():
        while executando[0] and segundos_restantes[0] > 0:
            segundos_restantes[0] -= 1
            h = segundos_restantes[0] // 3600
            m = (segundos_restantes[0] % 3600) // 60
            s = segundos_restantes[0] % 60
            lbl_tempo.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            time.sleep(1)
        if executando[0]:
            executando[0] = False
            lbl_tempo.config(text="⏰ FIM!", fg="#E74C3C")

    def iniciar():
        if segundos_restantes[0] > 0 and not executando[0]:
            lbl_tempo.config(fg=COR_TITULO)
            executando[0] = True
            threading.Thread(target=atualizar, daemon=True).start()

    def parar():
        executando[0] = False

    def resetar():
        executando[0] = False
        segundos_restantes[0] = 0
        spin_h.delete(0, tk.END); spin_h.insert(0, "0")
        spin_m.delete(0, tk.END); spin_m.insert(0, "0")
        spin_s.delete(0, tk.END); spin_s.insert(0, "0")
        lbl_tempo.config(text="00:00:00", fg=COR_TITULO)

    def renomear():
        resp = simpledialog.askstring("Nome", "Digite o nome:", parent=win)
        if resp:
            lbl_nome.config(text=resp)

    # Botão aplicar tempo
    tk.Button(frame, text="⏱ Aplicar Tempo", command=aplicar_tempo,
              font=("Arial", 8, "bold"), bg="#8E44AD", fg="white", relief="flat",
              bd=0, padx=8, pady=3, cursor="hand2",
              activebackground="#7D3C98", activeforeground="white").pack(pady=(0, 5))

    btn_frame = tk.Frame(frame, bg=COR_FUNDO)
    btn_frame.pack()

    tk.Button(btn_frame, text="▶ Iniciar", command=iniciar, font=("Arial", 9, "bold"),
              bg="#27AE60", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#1ABC9C", activeforeground="white").grid(row=0, column=0, padx=3)
    tk.Button(btn_frame, text="⏸ Parar", command=parar, font=("Arial", 9, "bold"),
              bg="#E67E22", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#D35400", activeforeground="white").grid(row=0, column=1, padx=3)
    tk.Button(btn_frame, text="↺ Reset", command=resetar, font=("Arial", 9, "bold"),
              bg="#E74C3C", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
              activebackground="#C0392B", activeforeground="white").grid(row=0, column=2, padx=3)

    tk.Button(frame, text="✏️ Renomear", command=renomear, font=("Arial", 8),
              bg="#7F8C8D", fg="white", relief="flat", bd=0, padx=8, pady=3, cursor="hand2",
              activebackground="#95A5A6", activeforeground="white").pack(pady=(6, 0))


def abrir_cronometros():
    """Abre a janela de seleção de tipo de cronômetro"""
    menu_win = tk.Toplevel(root)
    menu_win.title("Criar Cronômetro")
    menu_win.geometry("250x150")
    menu_win.configure(bg=COR_FUNDO)
    menu_win.resizable(False, False)

    lx = menu_win.winfo_screenwidth()
    ly = menu_win.winfo_screenheight()
    x = (lx - 250) // 2
    y = (ly - 150) // 2
    menu_win.geometry(f"250x150+{x}+{y}")

    tk.Label(menu_win, text="Qual cronômetro deseja criar?",
             font=("Arial", 11, "bold"), bg=COR_FUNDO, fg=COR_TITULO).pack(pady=(15, 15))

    tk.Button(menu_win, text="⏱ Progressivo", command=lambda: [menu_win.destroy(), criar_janela_progressivo()],
              font=("Arial", 10, "bold"), bg="#3498DB", fg="white", relief="flat",
              bd=0, padx=20, pady=8, cursor="hand2",
              activebackground="#2980B9", activeforeground="white").pack(pady=4)

    tk.Button(menu_win, text="⏳ Regressivo", command=lambda: [menu_win.destroy(), criar_janela_regressivo()],
              font=("Arial", 10, "bold"), bg="#E67E22", fg="white", relief="flat",
              bd=0, padx=20, pady=8, cursor="hand2",
              activebackground="#D35400", activeforeground="white").pack()


def abrir_vscode():
    try:
        subprocess.Popen(["C:\\Users\\Joaquim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
    except FileNotFoundError:
        messagebox.showerror("Erro", "VS Code não encontrado!")

def abrir_cmd():
    subprocess.Popen("cmd")

def limpar_temp():
    """Limpa as pastas TEMP, TMP e cache de instaladores do Windows"""
    import shutil
    
    usuario = os.environ.get("USERNAME", "")
    pastas = [
        os.environ.get("TEMP", ""),
        os.environ.get("TMP", ""),
        f"C:\\Users\\{usuario}\\AppData\\Local\\Temp",
        "C:\\Windows\\Temp",
        f"C:\\Users\\{usuario}\\AppData\\Local\\Microsoft\\Windows\\INetCache",
        f"C:\\Windows\\Prefetch",
        f"C:\\Users\\{usuario}\\AppData\\Local\\Microsoft\\Windows\\WER",
    ]
    
    total_apagado = 0
    
    for pasta in pastas:
        if not os.path.exists(pasta):
            continue
        for root_dir, dirs, files in os.walk(pasta, topdown=True, followlinks=False):
            for arquivo in files:
                try:
                    caminho = os.path.join(root_dir, arquivo)
                    os.remove(caminho)
                    total_apagado += 1
                except (PermissionError, OSError):
                    pass
            for diretorio in dirs:
                try:
                    caminho = os.path.join(root_dir, diretorio)
                    shutil.rmtree(caminho, ignore_errors=True)
                except (PermissionError, OSError):
                    pass
    
    # Cache do Windows Installer (*.msi)
    cache_installer = f"C:\\Windows\\Installer\\$PatchCache$"
    if os.path.exists(cache_installer):
        try:
            shutil.rmtree(cache_installer, ignore_errors=True)
        except:
            pass
    
    messagebox.showinfo(
        "Limpeza Concluída",
        f"Limpeza finalizada!\n\n"
        f"Arquivos removidos: ~{total_apagado}\n\n"
        f"Pastas verificadas:\n"
        f"• TEMP do usuário\n"
        f"• TMP do usuário\n"
        f"• Temp do Windows\n"
        f"• Prefetch\n"
        f"• Cache do Navegador\n"
        f"• Cache de Instaladores\n\n"
        f"Nota: Alguns arquivos em uso não puderam ser removidos."
    )

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

# Layout: 5 linhas x 2 colunas
criar_btn(botoes_frame, "💻 VS Code", abrir_vscode, COR_BOTAO, 0, 0)
criar_btn(botoes_frame, "⬛ CMD", abrir_cmd, "#16A085", 0, 1)
criar_btn(botoes_frame, "🧹 Limpeza Temp", limpar_temp, "#8E44AD", 1, 0)
criar_btn(botoes_frame, "🌐 Navegador", abrir_navegador, "#E67E22", 1, 1)
criar_btn(botoes_frame, "🧮 Calculadora", abrir_calculadora, "#D35400", 2, 0)
criar_btn(botoes_frame, "📁 Explorador", abrir_explorador, "#27AE60", 2, 1)
criar_btn(botoes_frame, "📝 Bloco Notas", abrir_bloco_notas, "#2980B9", 3, 0)
criar_btn(botoes_frame, "⚙️ Gerenciador", abrir_gerenciador_tarefas, "#C0392B", 3, 1)
criar_btn(botoes_frame, "⏱ Cronômetros", abrir_cronometros, "#F39C12", 4, 0)

# Botão Sair
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
btn_sair.grid(row=5, column=0, columnspan=2, pady=(6, 0))

def on_enter_sair(e): btn_sair.config(bg="#C0392B")
def on_leave_sair(e): btn_sair.config(bg="#E74C3C")
btn_sair.bind("<Enter>", on_enter_sair)
btn_sair.bind("<Leave>", on_leave_sair)

root.mainloop()