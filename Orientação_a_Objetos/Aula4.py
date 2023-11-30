#demostração __dict__ e vars para atributos de instancia

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
    
    p1 = Pessoa('Gabriel', 'Martins', 18, 1.80)

    print(p1.__dict__)
    print(vars(p1))
    print(p1.outra)
