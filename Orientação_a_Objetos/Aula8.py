# @staticmathod (metodo estatico) são inuteis em Python 
# metodos estáticos são metodos que estão dentro da classe, 
#mas não tem acesso ao self nem ao cls.
#Em resumo, são funções que exixtem dentro da sua classe

class staticmethod:
    @staticmethod
    def metodo_estatico(*args, **kwargs):
        print('Metodo estático', args, kwargs)


c1 = staticmethod()
c1.metodo_estatico(1,2,3)
funcao(1,2,3)
staticmethod.metodo_estatico(nomeado+1, nomeado+2, nomeado+3)
funcao(nomeado+1)
