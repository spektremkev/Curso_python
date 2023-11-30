#Demostração de como manter o estado do objeto dentro da classe.

class Camera:
    def __init__(self, cor, marca, modelo, filmando=False, zoom=False):
        """
        Initializes a new instance of the class.

        Parameters:
            cor (str): The color of the object.
            marca (str): The brand of the object.
            modelo (str): The model of the object.
            filmando (bool, optional): Indicates if the object is currently recording.
            zoom (bool, optional): Indicates if the object has zoom functionality.

        Returns:
            None
        """
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.filmando = filmando
        self.zoom = zoom
        
"""Records a video by setting the `filmando` attribute to True and printing 'Filmando...'.
    Parameters:
        self (object): The instance of the class.
    Returns:
        None
"""       
def filmar(self):
    self.filmando = True
    print('Filmando...')


c1 = Camera('preto', 'canon', '5d')
c2 = Camera('cinza', 'nikon', 'd3500')

print(c1.filmando)
print(c2.filmando)

