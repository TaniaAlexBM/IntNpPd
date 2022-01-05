# coding: utf-8
import pandas as pd
# Ordenamiento
data = pd.read_csv('users.csv', index_col = 'id')
# Obtener el usuario más joven de Canadá
data[data['pais'] == 'Canada']
# ordenar con respecto a la edad
data[data['pais'] == 'Canada'].sort_value('edad')
data[data['pais'] == 'Canada'].sort_values('edad')
data[data['pais'] == 'Canada'].sort_values('edad').head(1)
# Obtener a los cinco usuarios más viejos de Alemania
data[data['pais'] == 'Germany'].sort_values('edad', ascending = False).head(5)
# Obtener todos los usuarios entre las edades 40 y 50
data[(data['edad'] >=40) & (data['edad'] <= 50)]
data[data['edad'].between(40.50)]
data[data['edad'].between(40,50)]
# between es un método más legible
