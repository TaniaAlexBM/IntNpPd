# coding: utf-8
import numpy as np
A = np.array([
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])
A
#Dimensiones de un arreglo
A.ndim
# Forma del arreglo
A.shape
# Axi0 = Filas
# Axi1 = Columnas
# Un elemento de la matriz A[0][0]
A[0][0]
A[1][2]
2# A[axi0][axi1]
# Otra forma A[axi0, axi1]
A
A[1,2]
A[1,:3]
# con índices
A[0,[0,4]]
# Valores de columnas
A[:,3]
A[[0,2],3]
get_ipython().run_line_magic('save', 'matrices 2-24')
