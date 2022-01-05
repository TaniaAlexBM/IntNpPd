# coding: utf-8
import pandas as pd
usuarios = {
'username': ['user1','user2','user3','user4','user5'],
'email': ['user1@example.com','user2@example.com','user3@example.com','user4@example.com', 'user5@example.com'],
'age': [10,20,25,30,50],
'status': [True,True,False,False,True]
}
data = pd.DataFrame(usuarios)
data
# índices de tipo String
data = pd.DataFrame(usuarios, index = ['a','b','c','d','e'])
# índices de tipo String
data
data.loc['a'] # para índices de tipo String
data.loc['e']
# SubDataFrame
data.loc['a':'c']
# Sólo algunas columnas
data.loc['a':'c',['username','email']]
# otra forma
data.loc['a':'c'][['username','email']]
