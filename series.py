# coding: utf-8
import pandas as pd
# Series: objeto de pandas diseñado para una estructura de una dimensión. Poseen dos arreglos: uno para los valores y el otro para los índices de la serie
pd.Series([1,2,3,4,5])
# índices valores
a = pd.Series([1,2,3,4,5])
type(a)
# tamaño de la serie
a.size
# tipo de datos que almacena la serie
a.dtype
# forma de la serie
a.shape
# índices
a.index
# actualizar el índice
a[4]
a[4] = 500
a
# Se pueden definir que tipo de índices se van a utilizar
pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
b = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
b[c]
b['c']
b['c'] = 10
b
# Nombrar las series
b = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], name = 'Números')
b
# declarar el tipo de elementos que contiene la serie
b = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], name = 'Números', dtype = int)
b
b = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], name = 'Números', dtype = float)
b
