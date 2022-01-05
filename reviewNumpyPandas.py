# coding: utf-8
import pandas as pd
import numpy as np
# EJERCICIOS
data = pd.read_csv('users.csv', index_col = 'id')
# Obtener el nombre de todos los usarios con una edad mayo a 20
data[data['edad'] > 20]
# Obtener el nombre de todos los usarios con una edad mayor a 40
data[data['edad'] > 40]
# con QUERY
data.query('edad > 40')
# Sólo deben ser los nombres
data[data['edad'] > 40]['nombre']
# Obtener el nombre de todos los usuarios mayores a 20 y de sexo femenino
data[(data['edad'] > 20) & (data['genero'] == 'female')]['nombre']
# con QUERY
data.query('edad > 40 & genero == "female"')
# Obtener todos los usuarios cuyo correo no termine con @example.com
data[data['email'].str.endswith('@example.com')]
# Para filtrar strings se tiene .str + startwith/endswith/contains
# para negar se antepone ~
data[data['email'].str.endswith('@example.com')]
data[~data['email'].str.endswith('@example.com')]
# Obtener el nombre y el correo de todos aquellos usuarios del país Germany, Finland o Canada
data[(data['pais'] == 'Germany') | (data['pais'] == 'Finland') | (data['pais'] == 'Canada')]
# con QUERY
data.query('pais in ("Germany","Finland","Canada")')
# con el atributo ISIN
data[data['pais'].isin(['Germany','Finland','Canada'])]
# contar los registros del filtrado
data[data['pais'].isin(['Germany','Finland','Canada'])].count()
# Obtener el nombre y correo de todos los usuarios de sexo femenino del país Germany
data[data['genero'] == 'female']
data[(data['genero'] == 'female') & (data['pais'] == 'Germany')]
# con QUERY
data.query('genero == "female" and pais == "Germany"')
# Obtener la cantidad de usuarios de sexo masculino de Canada
data[(data['genero'] == 'male') & (data['pais'] == 'Canada')]
# contar cuantos registros son en función del genero
data[(data['genero'] == 'male') & (data['pais'] == 'Canada')]['genero'].count()
# Mostrar en consola la cantidad de hombres y mujeres
data.groupby('genero').count()
# acceder a los índices
data.groupby('genero').count().index.values
data.groupby('genero')['genero'].count()
# otra forma
data.value_counts(data['genero']).count()
data.value_counts(data['genero'])
# Mostrar el país con más mujeres
data[data['genero'] == 'female']
# agrupar los usuarios por países
data[data['genero'] == 'female'].groupby('pais')['pais']
data[data['genero'] == 'female'].groupby('pais')
data[data['genero'] == 'female'].groupby('pais')['pais'].count()
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values()
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values(ascending = False)
data[data['genero'] == 'female'].groupby('pais')['pais'].count().sort_values(ascending = False).head(1)
# Obtener los cinco países con más usuarios
data.groupby('pais').count()
data.groupby('pais')['pais'].count()
# ordenar
data.groupby('pais')['pais'].count().sort_values('pais')
data.groupby('pais')['pais'].count().sort_values()
data.groupby('pais')['pais'].count().sort_values(ascending = False)
# hay un empate, por lo que se mostrarán ambos
data.groupby('pais')['pais'].count().sort_values(ascending = False).head(2)
# pideron 5 países
data.groupby('pais')['pais'].count().sort_values(ascending = False).head(5)
