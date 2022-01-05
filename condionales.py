# coding: utf-8
import pandas as pd
# Condicionales
# Obtener el nombre de todos los usuarios de Canadá
data = pd.read_csv('users.csv', index_col = 'id')
data
data = data.dropna()
# Obtener el nombre de todos los usuarios de Canadá
data['country'] == 'Canada'
data
data['pais'] == 'Canada'
# genera un serie de valores booleanos
data[data['pais'] == 'Canada']
# únicamente el nombre de los usuarios
data[data['pais'] == 'Canada']['nombre']
# Obtener el nombre y correo electrónico con edad mayor a 50
data['edad'] > 50
# Los operadores relacionales dan como resultado valores booleanos
data['edad'] > 50
data[data['edad'] > 50]
data[data['edad'] > 50]['nombre','email']
data[data['edad'] > 50][['nombre','email']]
# Promedio de todos los usuarios de sexo femenino con edad mayor a 30
data[data['genero'] == 'female']
data[data[('genero'] == 'female') & (data['edad'] > 30)]
data[(data['genero'] == 'female') & (data['edad'] > 30)]
# las condiciones que se van a unir, deben ir entre parentesis por separado
data[(data['genero'] == 'female') & (data['edad'] > 30)]['edad']
data[(data['genero'] == 'female') & (data['edad'] > 30)]['edad'].mean()
