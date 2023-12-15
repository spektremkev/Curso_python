#Investigando o funcionamento do modulo OS

import os

print(os.getcwd())



diretorio = "D:\linguagens_de_programação\Curso_python\Curso_python\Exercicios_aula_5"
arquivos = os.listdir(diretorio)

print("Arquivos no diretório:", arquivos)

diretorio_atual = os.getcwd()
print("Diretório atual:", diretorio_atual)





diretorio = "D:\linguagens_de_programação\Curso_python\Curso_python\Exercicios_aula_5"
os.mkdir(diretorio)
print("Diretório criado com sucesso!")


"""
caminho_antigo = "D:\linguagens_de_programação\Curso_python\Curso_python\Exercicios_aula_5\Aula5correção.py"
caminho_novo = "/caminho/do/arquivo_ou_diretorio_novo"

os.rename(caminho_antigo, caminho_novo)
print("Arquivo ou diretório renomeado com sucesso!")

"""