#Demostração de como salvar a classe em arquivo em JSON
#Salvar os dados da classe em um arquivo JSON e depois crie novamente as instancias
#da classe com os dados salvos 
#criem arquivo separados 

import json
#importando a biblioteca json

#class que recebe os dados do usuario e os armasem na variavel
class UserData:
    def __init__(self):
        self.cor = input("Digite a cor do carro: ")
        self.marca = input("Digite a marca do carro: ")
        self.modelo = input("Digite o modelo do carro: ")
        self.combustivel = input("Digite o tipo de combustivel do carro: ")
        self.numero_portas = input("Digite o numero de portas do carro: ")
        self.numero_series = input("Digite o numero de serie do carro: ")
        self.rodas = input("Digite o numero de rodas do carro: ")

#Class que abre o arquivo json e armazena os dados das variaveis criadas acima
class Json:
    def __init__(self):
        self.user = UserData()
        self.data = json.dumps(self.user.__dict__)
        print(self.data)

#Chamando a classe Json e imprimindo os dados
j = Json()
#print(j.data)qwe

#Criando o arquivo json e salvando os dados e define localidade do arquivo

caminho_arquivo = "D:\linguagens_de_programação\Curso_python\Curso_python\Exercicios_aula_5\dados.json"
with open('dados.json', 'w') as f:
    json.dump(j.data, f)

