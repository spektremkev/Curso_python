#Metodos de classe
#São metodos onde "self" sera "cls", ou seja 
#ao inves de receber a instandia no primeiro 
#parametro, receberemos o nome da classe

class Pessoa:
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

    @classmethod
    def metodo_de_classe(cls):
        """
        A class method that prints 'Metodo de classe'.
        """
        print('Metodo de classe')
        
    @classmethod
    def cria_de_classe_idade(cls, nome, sobrenome, idade, altura):
        """
        Creates an instance of the class using the given parameters.

        Parameters:
            nome (str): The first name of the person.
            sobrenome (str): The last name of the person.
            idade (int): The age of the person.
            altura (float): The height of the person.

        Returns:
            The created instance of the class.
        """
        return cls('Gabriel', 'Martins', 30, 1.69)

p1 = Pessoa('Gabriel', 'Martins', 30, 1.69)
print(p1)
print(Pessoa.cria_de_classe_idade)

Pessoa.metodo_de_classe()