
#class - Classe s sao moldes para criar objetos.
#As classes geram objetos(instâncias) que podem ter seus próprios atributos e métodos.
#Os objetos gerados pelas classes podem usar seus dados internos para realizar varias ações.
#Por convenção usamos PascalCase para nomes de classes.


string = 'gabriel' # str
print(string.upper())
print(isinstance(string, str))

class Pessoa:
    """
    A palavra reservada __init__ em Python é um método especial que é chamado automaticamente quando um objeto é criado a partir de uma classe. 
    É conhecido como o construtor da classe.
    A palavra reservada def em Python é usada para definir uma função. A palavra def é uma abreviação de "define".
    
        def -é a palavra-chave que indica o início da definição da função.
        nome_da_funcao - é o nome que você escolhe para a função.
        parametros - são os argumentos que a função aceita. Eles são opcionais e podem ser zero ou mais.
        O corpo da função é onde o código que a função deve executar é escrito.

    A palavra reservada (self) em Python é uma referência ao objeto atual. É usado dentro dos métodos de uma classe para se referir ao objeto que está chamando o método.
    """
    def __init__(self, nome, sobrenome, idade, altura):
        """
        Initializes a new instance of the class.
        
        Args:
            nome (str): The first name of the person.
            sobrenome (str): The last name of the person.
            idade (int): The age of the person.
            altura (float): The height of the person.
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        
p1 = Pessoa('Gabriel', 'Martins', 18, 1.67)
p2 = Pessoa('88', 'Luiz', 18, 1.87)


class Carro:
    def __init__(self, cor, marca, modelo, combustivel, numero_portas, numero_series, rodas):
        """
        Initializes a new instance of the Car class.

        Args:
            cor (str): The color of the car.
            marca (str): The brand of the car.
            modelo (str): The model of the car.
            combustivel (str): The type of fuel the car uses.
            numero_portas (int): The number of doors the car has.
            numero_series (str): The unique serial number of the car.
            rodas (int): The number of wheels the car has.
        """
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel
        self.numero_portas = numero_portas 
        self.numero_series = numero_series
        self.rodas = rodas
    
    def acelerar(self):
        print('Acelerando...')

string = 'gabriel'
print(string.upper())

uno = Carro('uno')
print(uno.name)
uno.acelerar()

celta = Carro('preto', 'celta', 'uno', 'gasolina', 4, 0, 4)
print(celta.nome)
celta.acelerar()



p3 = Carro('preto', 'fiat', 'uno', 'gasolina', 4, 0, 4)

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


#-----------------------------------------------

print(p1.nome, p1.sobrenome, p1.idade, p1.altura)
print(p2.nome, p2.sobrenome, p2.idade, p2.altura)
print(p3.cor, p3.marca, p3.combustivel, p3.rodas, p3.rodas)

