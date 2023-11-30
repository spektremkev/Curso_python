#demostração de atributos de classe

class Pessoa:
    ANO_ATUAL = 2023

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
    def get_ano_nascimento(self):
        """
        Returns the year of birth based on the current year and the age of the person.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            int: The year of birth.
        """
    #return ANO_ATUAL - self.idade
    #return self.ANO_ATUAL - self.idade
    
p1 = Pessoa('Gabriel', 'Martins', 22, 1.67)
p2 = Pessoa('Maria', 'Silva', 18, 1.55)
p3 = Pessoa('Pedro', 'Santos', 30, 1.75)
p4 = Pessoa('Ana', 'Pereira', 25, 1.65)

print(p1.nome)
print(p1.sobrenome)
print(p1.idade)
print(p1.altura)
print(p1.get_ano_nascimento())

print(p2.nome)
print(p2.sobrenome)
print(p2.idade)
print(p2.altura)
print(p2.get_ano_nascimento())

print(p3.nome)
print(p3.sobrenome)
print(p3.idade)
print(p3.altura)
print(p3.get_ano_nascimento())

print(p4.nome)
print(p4.sobrenome)
print(p4.idade)
print(p4.altura)
print(p4.get_ano_nascimento())

