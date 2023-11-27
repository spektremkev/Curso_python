"""
Valores padrão para parametros
Ao definir uma funçao, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o paramentros, o valor padrão será usados.
Refatorar: editar o seu código.
"""

def soma(x, y=0):
    print(x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)


def soma(x, y=0):
    print(x, y, '|', 'x + y =', x + y)

soma(1, 2)
soma(1)


