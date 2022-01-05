# coding: utf-8
# un arreglo no puede modificar su longitud
# para modificar un arreglo, existen funciones que crean uno nuevo con las modificaciones
import numpy as np
a = np.random.randint(0,10,10)
a
a.size
# INSERT
np.insert(a,0, 200)
# un nuevo arreglo donde se ha añadido 200 en el índice cero
# APPEND
np.append(a,200)
# crea un nuevo arreglo que añade el 200 al final del arreglo
# DELETE
np.delete(a, -1)
# Crea un arreglo en el que se eliminó el último elemento de los que se copiaron del arreglo original
np.resize(a, 5)
# Retorna un nuevo arreglo con un nuevo tamaño
a
b = np.array([10,20,30,40,50])
b
np.concatenate([a,b])
# une los elementos de ambos arreglos
