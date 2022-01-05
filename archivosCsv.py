# coding: utf-8
import pandas as pd
# importar un archivo .csv
data = pd.read_csv('users.csv', index_col = 'id')
data
# index_col le indica a pandas que columna utilizar como índices
# head(): primeras filas
# tail(): últimas filas
data.head(15)
data.tail()
data.tail(15)
