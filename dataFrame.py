# coding: utf-8
import pandas as pd
# Dataframe: estructura de datos tipo Excel, con columnas y filas
# la forma más fácil de crear un dataframe es mediante un diccionario
usuarios = {
'username': ['user1','user2','user3'],
'email': ['user1@example.com','user2@example.com','user3@example.com'],'age': [27,10,30],
'status': [True,True,False]
}
pd.DataFrame(usuarios)
# Definir los índices
pd.DataFrame(usuarios, index = ['a','b','c'])
# Valores de una columna
data['username']
data = pd.DataFrame(usuarios, index = ['a','b','c'])
data['username']
data['age']
# Da como resultado una nueva serie con los índices que se asignaron y los valores que estamos requiriendo
data['age']['a']
# otra forma
data.email
# es menos común utilizar esta forma
# trabajar con columnas
data.columns
# los valores
data.values
