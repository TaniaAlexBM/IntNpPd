# coding: utf-8
import pandas as pd
# Diccionarios
colores = {
'rojo': 100,
'verde': 200,
'azul': 300,
'negro': 400
}
pd.Series(colores)
a = pd.Series(colores)
a['rojo']
