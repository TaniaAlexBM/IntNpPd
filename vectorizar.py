# coding: utf-8
import numpy as np
a = np.random.randint(0,10,20)
a
# Definir la función operación
def operacion(valor):
    return (valor**2) + 2
    
operacion(3)
# Aplicar la función en cada elemento del arreglo
for valor in a:
    print(operacion(valor))
    
# para regresar los resultados como un vector
vector = np.vectorize(operacion)
vector(a)
# se vectorizó la función
# Se puede hacer con una lambda
vector1 = np.vectorize(lambda valor: (valor**2) + 2)
vector1(a)
