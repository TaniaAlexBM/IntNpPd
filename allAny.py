# coding: utf-8
import numpy as np
A = np.array([
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])
a = np.random.randint(0,100,50)
# Si todos los elementos son mayores a 50
np.all(a > 50)
# no todos los elementos cumplen la condición
np.all(a >= 0)
# todos los elementos cumplen con la condición
np.any((a >= 0) & (a >= 100))
np.any((a >= 0) & (a <= 100))
# Por lo menos uno cumple con la condición
np.any(a > 10)
np.any(a > 200)
