import tkinter as tk
import subprocess
root = tk.Tk()
root.title("Sistema de Máquina")
root.geometry("400x300")

def abrir_vscode():
    subprocess.Popen(["C:\\Users\\Joaquim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])

def abrir_cmd():
    subprocess.Popen("cmd")

button_vscode = tk.Button(root, text="Abrir VsCode", command=lambda: abrir_vscode())
button_vscode.pack(pady=20)

button_cmd = tk.Button(root, text="Abrir CMD", command=lambda: abrir_cmd())
button_cmd.pack(pady=20)

root.mainloop()