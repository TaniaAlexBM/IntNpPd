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
