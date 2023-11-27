"""
class - Classe s sao moldes para criar objetos.
As classes geram objetos(instâncias) que podem ter seus próprios atributos e métodos.
Os objetos gerados pelas classes podem usar seus dados internos para realizar varias ações.
Por convenção usamos PascalCase para nomes de classes.
"""

string = 'gabriel' # str
print(string.upper())
print(isinstance(string, str))

class Pessoa:
    
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        
p1 = Pessoa('Gabriel', 'Martins', 18, 1.67)

p2 = Pessoa('88', 'Luiz', 18, 1.87)

#p1 = Pessoa()
#p1.nome = 'Gabriel'
#p1.sobrenome = 'Martins'
#p1.idade = 18
#p1.altura = 1.67

#p2 = Pessoa()
#p2.nome = '88'
#p2.sobrenome = 'Luiz'
#p2.idade = 18
#p2.altura = 1.87

print(p1.nome, p1.sobrenome, p1.idade, p1.altura)

print(p2.nome, p2.sobrenome, p2.idade, p2.altura)


