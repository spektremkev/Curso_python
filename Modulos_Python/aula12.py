#Investigando o funcionamento do modulo OS

import os

print(os.getcwd())



diretorio = "/caminho/do/diretorio"
arquivos = os.listdir(diretorio)

print("Arquivos no diretório:", arquivos)

diretorio_atual = os.getcwd()
print("Diretório atual:", diretorio_atual)



diretorio = "/caminho/do/novo/diretorio"
os.mkdir(diretorio)
print("Diretório criado com sucesso!")






caminho_antigo = "/caminho/do/arquivo_ou_diretorio_antigo"
caminho_novo = "/caminho/do/arquivo_ou_diretorio_novo"

os.rename(caminho_antigo, caminho_novo)
print("Arquivo ou diretório renomeado com sucesso!")