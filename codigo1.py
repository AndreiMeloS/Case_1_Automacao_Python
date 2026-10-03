# ==========================================
# 1. IMPORTAR BIBLIOTECAS
# ==========================================

import pyautogui
import time
import pandas as pd


# ==========================================
# 2. CONFIGURAR A VELOCIDADE DA AUTOMAÇÃO
# ==========================================

# Cria uma pausa de 0,5 segundo entre os comandos
pyautogui.PAUSE = 0.5


# ==========================================
# 3. ABRIR O NAVEGADOR
# ==========================================

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")  # Seleciona o primeiro usuário que aparece na tela
pyautogui.press("enter")


# ==========================================
# 4. ACESSAR O SITE
# ==========================================

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

time.sleep(3)

pyautogui.click(x=2448, y=82)
pyautogui.write(link)
pyautogui.press("enter")

# Aguarda o carregamento da página
time.sleep(3)


# ==========================================
# 5. FAZER LOGIN
# ==========================================

# Clica no campo de usuário
pyautogui.click(x=2536, y=377)

# Digita o usuário
pyautogui.write("AndreilsonSouza@AndreiMeloS.onmicrosoft.com")

# Vai para o campo de senha
pyautogui.press("tab")

# Digita a senha
pyautogui.write("CDYam2022*")

# Vai para o botão de login
pyautogui.press("tab")

# Confirma o login
pyautogui.press("enter")


# ==========================================
# 6. IMPORTAR A BASE DE PRODUTOS
# ==========================================

tabela = pd.read_csv("aula_1/produtos.csv")

# Mostra a tabela no terminal
print(tabela)


# ==========================================
# 7. REPETIR O CADASTRO PARA CADA PRODUTO
# ==========================================

for linha in tabela.index:

    # --------------------------------------
    # CADASTRAR UM PRODUTO
    # --------------------------------------

    # Clica no primeiro campo do formulário
    pyautogui.click(x=2372, y=255)

    # Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))

    # Marca
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # Tipo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # Categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    # Preço unitário
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # Custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # Observação
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    # Só preenche se existir uma observação
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Vai para o botão de cadastro
    pyautogui.press("tab")

    # Cadastra o produto
    pyautogui.press("enter")

    # Volta a tela para cima
    pyautogui.scroll(5000)