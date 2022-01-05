# coding: utf-8
a = np.random.randint(0,100,50)
a
a >50
# Se compara uno por uno los elementos del arreglo en la condicional
b = np.array([1,2,3,4,5])
b[True,False,False,False,True]
b[[True,False,False,False,True]]
a[a > 50]
# Operadores lógicos
a[(a > 50) & (a < 90)]
a[(a == 10) | (a == 20) | (a == 50)]
