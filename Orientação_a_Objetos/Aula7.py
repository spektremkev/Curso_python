#Gerador números aleatorios
import random
import ctypes

# Carrega a biblioteca compartilhada
my_module = ctypes.CDLL('./my_module.so')

# Define as assinaturas das funções C++
my_module.my_function.argtypes = [ctypes.c_int]
my_module.my_function.restype = ctypes.c_int



random_number = random.randint(1, 1000)
print(random_number)

print(my_module.my_function(random_number))


