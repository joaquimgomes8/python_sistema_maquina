# 🚀 Python Sistema Máquina

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![Status](https://img.shields.io/badge/status-ativo-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

> Painel de atalhos em Python para abrir ferramentas do dia a dia com um clique, de forma rápida e centralizada.

---

## 📋 Sobre o Projeto

O **Python Sistema Máquina** é uma aplicação desktop desenvolvida em **Python + Tkinter** que reúne, em uma única janela, **botões de atalho para abrir as ferramentas mais usadas no dia a dia** — como editores de código, navegadores, pastas do sistema, terminais, entre outras.

---

## ✨ Funcionalidades

- ✅ **Painel de atalhos** — botões configuráveis para abrir qualquer programa, pasta ou comando.
- ✅ **Abertura rápida do VS Code** — comando configurado para funcionar em **qualquer máquina**, não apenas na máquina original.
- ✅ **Interface compacta** — layout ajustado para ocupar pouco espaço na tela.
- ✅ **Gerenciamento de cronômetros** — funcionalidade integrada com correções e melhorias contínuas.
- ✅ **Multiplataforma** — funciona em Windows (foco principal), com estrutura adaptável.

---

## 🚀 Como Usar

### Opção 1 — Executável (sem precisar instalar Python)

1. Acesse a pasta **`dist/`** do repositório.
2. Baixe o executável gerado (`system.exe` ou equivalente).
3. Dê **duplo clique** para abrir o painel de atalhos.

> 💡 Nenhuma instalação adicional necessária nessa modalidade.

### Opção 2 — Executar pelo código-fonte (requer Python)

**Pré-requisito:** Python 3.8 ou superior.

```bash
# Clone o repositório
git clone https://github.com/joaquimgomes8/python_sistema_maquina.git

# Entre na pasta
cd python_sistema_maquina

# (Opcional) Crie um ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # Linux/macOS

# Execute
python system.py
