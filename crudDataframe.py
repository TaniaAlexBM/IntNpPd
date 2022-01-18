# coding: utf-8
import pandas as pd
usuarios = {
'username': ['user1','user2','user3'],
'email': ['user1@example.com','user2@example.com','user3@example.com'],'age': [27,10,30],
'status': [True,True,False]
}
data = pd.DataFrame(usuarios, index = ['a','b','c'])
# Columnas - series
import numpy as np
calificaciones = pd.Series(np.random.randint(5,10,3))
calificaciones
# nueva columna en el dataframe
data['calificaciones'] = calificaciones
data
# no existen los valores en el dataframe porque los índices en la serie calificaciones y en el dataframe data son diferentes
calificaciones = pd.Series(np.random.randint(5,10,3), index = ['a','b','c'])
calificaciones
data['calificaciones'] = calificaciones
data
# Renombrar las columnas
data.rename(
columns = {'calificaciones':'score'})
# el dataframe original no es modificado, se crea un nuevo dataframe
data = data.rename(
columns = {'calificaciones':'score'})
data
# nombre de la columna - atributo del objeto
data['email']
data.email
# eliminar columnas
del data['score']
data
