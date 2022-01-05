# coding: utf-8
import pandas as pd
import numpy as np
data = pd.read_csv('users.csv', index_col = 'id')
# EJERCICIOS
# Mostrar en consola el nombre de todos los usuarios que no poseen un correo electrónico
data[data['email'].isnull()]['nombre']
# Listar el nombre y el correo del usuario más joven de Canadá
data[data['edad'] == data['edad'].min()][['nombre','email']]
# Listar el nombre y el correo de los usuarios más jóvenes de Germany y Canadá
data.iloc[data[data['pais'].isin(['Germany','Canada'])]['edad'].sort_values().head(2).index.values]
# Listar los cinco países con menos cantidad de usuarios
data.groupby('pais')['pais'].count().sort_values().head(5)
# Obtener el país con más usuarios
data.groupby('pais')['pais'].count().sort_values(ascending = False).head(1)
# Obtener el país con más usuarios cuya edad sea mayor a 50
data[data['edad'] > 50].groupby('pais')['pais'].count().sort_values(ascending = False).head(1)
# Obtener la suma total de todos los usuarios de Canadá y Germany
data[data['pais'].isin(['Canada','Germany'])]['pais'].count()
# Mostrar en consola la cantidad de países en el dataset
data.groupby('pais')['pais'].count().size
# Obtener el promedio de edad de cada uno de los países
data.groupby('pais').mean('edad')
# Mostrar en consola el país con más hombres
data[data['genero'] == 'male'].groupby('pais')['pais'].count().sort_values(ascending = False).head(1)
