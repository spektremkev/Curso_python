"""
Argumentos nomeados e não nomeados em funcões Python
Argumentos nomeados tem nome com sinal de igual.
Argumento nao nomeado recede apenas o argumento (valor)
"""

def soma (x, y):
    print(x, y)

soma (1, 2)

def soma2 (x, y, z):
    print(x, y, z)

soma2 (1, 2, 3)

def soma3 (x, y, z):
    print(f'{x=} y={y}','|','x + y =', x + y)

soma3 (1, 2)
soma3 (y=2, x=1)


def soma3 (x, y, z):
    print(f'{x=} y={y} y={z}', '|', 'x + y + z =', x + y + z)

soma3 (1, 2, 3)
soma3 (y=2, x=1, z=3)