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

# Aumentar a janela (300x400) para caber os cronômetros
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
def abrir_cronometros():
    """Abre a janela de cronômetros (progressivo e regressivo)"""
    cron_win = tk.Toplevel(root)
    cron_win.title("Cronômetros")
    cron_win.geometry("320x260")
    cron_win.configure(bg=COR_FUNDO)
    cron_win.resizable(False, False)

    # Centralizar
    largura_tela = cron_win.winfo_screenwidth()
    altura_tela = cron_win.winfo_screenheight()
    x = (largura_tela - 320) // 2
    y = (altura_tela - 260) // 2
    cron_win.geometry(f"320x260+{x}+{y}")

    frame_atual = None

    def limpar_frame():
        nonlocal frame_atual
        if frame_atual:
            frame_atual.destroy()

    # ------ PROGRESSIVO ------
    def abrir_progressivo():
        limpar_frame()
        nonlocal frame_atual
        frame_atual = tk.Frame(cron_win, bg=COR_FUNDO)
        frame_atual.pack(expand=True, fill="both", padx=15, pady=10)

        lbl_tempo = tk.Label(frame_atual, text="00:00:00", font=("Arial", 36, "bold"),
                             bg=COR_FUNDO, fg=COR_TITULO)
        lbl_tempo.pack(pady=(20, 15))

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

        btn_frame = tk.Frame(frame_atual, bg=COR_FUNDO)
        btn_frame.pack()

        tk.Button(btn_frame, text="▶ Iniciar", command=iniciar, font=("Arial", 9, "bold"),
                  bg="#27AE60", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#1ABC9C", activeforeground="white").grid(row=0, column=0, padx=4)
        tk.Button(btn_frame, text="⏸ Parar", command=parar, font=("Arial", 9, "bold"),
                  bg="#E67E22", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#D35400", activeforeground="white").grid(row=0, column=1, padx=4)
        tk.Button(btn_frame, text="↺ Resetar", command=resetar, font=("Arial", 9, "bold"),
                  bg="#E74C3C", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#C0392B", activeforeground="white").grid(row=0, column=2, padx=4)

    # ------ REGRESSIVO ------
    def abrir_regressivo():
        limpar_frame()
        nonlocal frame_atual
        frame_atual = tk.Frame(cron_win, bg=COR_FUNDO)
        frame_atual.pack(expand=True, fill="both", padx=15, pady=10)

        lbl_tempo = tk.Label(frame_atual, text="00:00:00", font=("Arial", 36, "bold"),
                             bg=COR_FUNDO, fg=COR_TITULO)
        lbl_tempo.pack(pady=(10, 5))

        executando = [False]
        segundos_restantes = [0]

        def perguntar_tempo():
            resposta = simpledialog.askinteger(
                "Tempo Regressivo",
                "Digite o tempo em segundos:",
                parent=cron_win,
                minvalue=1,
                maxvalue=86400
            )
            if resposta:
                segundos_restantes[0] = resposta
                h = resposta // 3600
                m = (resposta % 3600) // 60
                s = resposta % 60
                lbl_tempo.config(text=f"{h:02d}:{m:02d}:{s:02d}")

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
            lbl_tempo.config(text="00:00:00", fg=COR_TITULO)

        btn_frame1 = tk.Frame(frame_atual, bg=COR_FUNDO)
        btn_frame1.pack(pady=(5, 5))

        tk.Button(btn_frame1, text="⏱ Definir Tempo", command=perguntar_tempo,
                  font=("Arial", 9, "bold"), bg="#8E44AD", fg="white", relief="flat",
                  bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#7D3C98", activeforeground="white").pack()

        btn_frame2 = tk.Frame(frame_atual, bg=COR_FUNDO)
        btn_frame2.pack()

        tk.Button(btn_frame2, text="▶ Iniciar", command=iniciar, font=("Arial", 9, "bold"),
                  bg="#27AE60", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#1ABC9C", activeforeground="white").grid(row=0, column=0, padx=4)
        tk.Button(btn_frame2, text="⏸ Parar", command=parar, font=("Arial", 9, "bold"),
                  bg="#E67E22", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#D35400", activeforeground="white").grid(row=0, column=1, padx=4)
        tk.Button(btn_frame2, text="↺ Resetar", command=resetar, font=("Arial", 9, "bold"),
                  bg="#E74C3C", fg="white", relief="flat", bd=0, padx=10, pady=5, cursor="hand2",
                  activebackground="#C0392B", activeforeground="white").grid(row=0, column=2, padx=4)

    # Botões de seleção do tipo de cronômetro
    tk.Button(cron_win, text="⏱ Progressivo", command=abrir_progressivo,
              font=("Arial", 10, "bold"), bg="#3498DB", fg="white", relief="flat",
              bd=0, padx=15, pady=8, cursor="hand2",
              activebackground="#2980B9", activeforeground="white").pack(pady=(10, 0))

    tk.Button(cron_win, text="⏳ Regressivo", command=abrir_regressivo,
              font=("Arial", 10, "bold"), bg="#E67E22", fg="white", relief="flat",
              bd=0, padx=15, pady=8, cursor="hand2",
              activebackground="#D35400", activeforeground="white").pack(pady=(5, 0))


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