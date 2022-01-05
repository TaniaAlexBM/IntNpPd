# coding: utf-8
import numpy as np
import pandas as pd
pd.Series([1,2,3])
# DataFrame está conformado por series
data = pd.read_csv('users.csv')
data
data['nombre']
# Se puede acceder con corchetes, que es la más común o por atributos
data.edad
data
data = pd.read_csv('users.csv', index_col = 'id')
data
# elementos a partir del índice de las filas ILOC
data.iloc[[4,5,6]]
# regresa un DataFrame
c = data.iloc[[4,5,6]]
dtype(c)
type(c)
# LOC se utliza para DataFrames que tienen como índices Strings
data = pd.read_csv('users.csv', index_col = 'nombre')
data
data['Mr Raff Valkema']
data.loc['Mr Raff Valkema']
# lo ideal es que las columnas tengan el mismo tipo de dato en sí mismas, no es necesario que sea así en toda el DataFrame
# eliminar los registros que no tienen por lo menos un valor
data.dropna()
