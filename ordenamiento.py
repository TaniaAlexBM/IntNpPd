# coding: utf-8
# Ordenar elementos de un arreglo
import numpy as np
a = np.random.randint(0,10,20)
a.sort()
a
# funcion sort
np.sort(a)
a
# con la función sort se modifica al arreglo, mientras que con el métodosort se crea un nuevo arreglo con los elementos ordenados
# orden descendente
a[::-1]
