# coding: utf-8
import pandas as pd
data = pd.read_csv('users.csv', index_col = 'id')
# Obtener el nombre de todos los usuarios mayores a 30 de Canada, Alemania y Francia
data[(data['edad'] > 30) & ((data['pais'] == 'Canada') | (data['pais'] == 'Germany') | (data['pais'] == 'France'))]
# una mejor forma para hacer múltiples opciones, se utiliza el método ISIN
countries = ['Canada','Germany','France']
data[(data['edad'] > 30) & (data['pais'].isin(countries))]
# Métodos de Strings
# STARTSWITH Permite saber si un String inicia con
data [data['email'].str.startswith('a')]
# usuarios que su correo inicia con A
# ENDSWITH método que muestra los Strings que terminen con
data[data['email'].str.edswith('.com')]
data[data['email'].str.endswith('.com')]
# CONTAINS método que muestra los Strings que contengan la cadena de caracteres
data[data['nombre'].str.contains('Gabriel')]
# str -> startswith - endswith - contains = LIKE 
# AGRUPAMIENTO
# Mostrar en consola la cnatidad de hombres y mujeres del Dataset
# método groupby
data.groupby('genero')
data.groupby('genero')['genero']
data.groupby('genero')['genero'].count()
# Mostrar el país con más mujeres
# filtrar a las mujeres
data[data['genero'] == 'female']
data[data['genero'] == 'female'].groupby('pais')
data[data['genero'] == 'female'].groupby('pais')['pais'].count()
# ordenar
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values()
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values(ascending = False)
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values(ascending = False).head(1)
