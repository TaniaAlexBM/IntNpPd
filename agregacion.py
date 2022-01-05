# coding: utf-8
import numpy as np
A = np.array([
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])
# Desviación estándar
A.std()
# Suma de todos los elementos del arreglo
A.sum()
# valor mínimo
A.min()
# valor máximo
A.max()
# promedio
A.mean()
# Información de filas o columnas
# Suma total de una fila
A[1]
A[1].sum()
# valor máximo de una fila
A[2].max()
# valor mínimo de una fila
A[2].min()
# promedio de una fila
# promedio de una columna
A[:,2].mean()
A[:,4].mean()
get_ipython().run_line_magic('save', 'agregacion 25-49')
