# coding: utf-8
import numpy as np
lista = [10,20,30,40,50,60]
lista
type(lista)
np.array(lista)
a = np.array(lista)
type(a)
a.size
a.itemsize
a[0]
a[5]
a[a.size - 1]
a[1:5]
a[1:5:2]
a[::-1]
lista = [0,3,4,5]
for i in lista:
    print(a[i])
    
a[lista]
a[[0,0,3,4]]
((a*10) - 10)/2
np.array([1,2,3], dtype = np.float32)
np.arange(0,10)
np.arange(0,20)
np.arange(0,20,2)
np.zeros(10)
np.zeros(10, dtype=np.integer)
np.ones(10, dtype=np.integer)
np.full(10,5)
np.full(10,2.5)
np.random.random(15)
np.random.randint(0,25,10)
np.linspace(0,10,10)
