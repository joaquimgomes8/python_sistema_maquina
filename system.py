import tkinter as tk
import subprocess
root = tk.Tk()
root.title("Sistema de Máquina")
root.geometry("400x300")

def abrir_vscode():
    subprocess.Popen(["C:\\Users\\Joaquim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])

button = tk.Button(root, text="Abrir VsCode", command=lambda: abrir_vscode())
button.pack(pady=20)






root.mainloop()