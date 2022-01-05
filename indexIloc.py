# coding: utf-8
import pandas as pd
pd.read_csv('users.csv')
data = pd.read_csv('users.csv', index_col = 'id')
data
# Limpiar el DataFrame
# eliminar las filas que carezcan de algún valor
data.dropna()
# crea un nuevo dataframe
# colocar valor donde existan NaN
data.fillna('nuevo valor')
# también crea un nuevo DataFrame
# define los valores que se van a escribir en cada columna en un diccionario
data.fillna({})
data.fillna({})
data.fillna({'name':'Sin nombre','email':'example@example.com'})
get_ipython().run_line_magic('save', 'limpieza.py 1-15')
import pandas as pd
data = pd.read_csv('users.csv', index_col = 'id')
# obtener valores con respecto a las filas
# se hace mediante los índices, que están guardados en un arreglo diferente
# loc, obtener filas con respecto a índices de tipo string
# iloc, obtener filas con respecto a índices de tipo entero
data.iloc[0]
# se obtiene una serie con los valores de la fila
data.iloc[199]
# generar subdataframe con iloc
data.iloc[0:5]
data.iloc[:5] # como el índice inicial es cero, se puede omitir
data.iloc[:3, [0,2,4]]
data.iloc[:3, ['name','gender','enmail']]
data.iloc[:3, ['nombre','genero','email']]
data
data.columns
data.iloc[:3, ['nombre','genero','email']]
data.iloc[:3] [['nombre','genero','email']]
