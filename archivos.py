# coding: utf-8
# Leer archivos del sistema con Numpy
import numpy as np
a = np.random.randint(0,10,10)
a
np.savetxt('Arreglo.txt', a)
get_ipython().run_line_magic('load', 'arreglo.txt')
get_ipython().run_line_magic('load', 'Arreglo.txt')
# %load Arreglo.txt
0.000000000000000000e+00
3.000000000000000000e+00
1.000000000000000000e+00
9.000000000000000000e+00
4.000000000000000000e+00
6.000000000000000000e+00
1.000000000000000000e+00
7.000000000000000000e+00
6.000000000000000000e+00
8.000000000000000000e+00
np.savetxt('Arreglo.txt', a, fmt = '%i')
# %load Arreglo.txt
0.000000000000000000e+00
3.000000000000000000e+00
1.000000000000000000e+00
9.000000000000000000e+00
4.000000000000000000e+00
6.000000000000000000e+00
1.000000000000000000e+00
7.000000000000000000e+00
6.000000000000000000e+00
8.000000000000000000e+00
get_ipython().run_line_magic('load', 'arreglo.txt')
get_ipython().run_line_magic('load', 'Arreglo.txt')
# %load Arreglo.txt
0
3
1
9
4
6
1
7
6
8
# Se guarda el arreglo como enteros
# LOADTXT retorna un nuevo arreglo
b = np.loadtxt('Arreglo.txt')
b
b.dtype
b = np.loadtxt('Arreglo.txt',dtype=int)
b.dtype
# Almacenar o crear matrices
# Se recomienda la extensión csv
a
a.size
a.reshape((2,5))
c = a.reshape((2,5))
c
np.savetxt('matriz.csv', c, delimiter=',')
get_ipython().run_line_magic('load', 'matriz.csv')
# %load matriz.csv
0.000000000000000000e+00,3.000000000000000000e+00,1.000000000000000000e+00,9.000000000000000000e+00,4.000000000000000000e+00
6.000000000000000000e+00,1.000000000000000000e+00,7.000000000000000000e+00,6.000000000000000000e+00,8.000000000000000000e+00
np.savetxt('matriz.csv', c, delimiter=',', fmt='%i')
get_ipython().run_line_magic('load', 'matriz.csv')
# %load matriz.csv
0,3,1,9,4
6,1,7,6,8
d = np.loadtxt('matriz.csv', delimiter=',')
d
d = np.loadtxt('matriz.csv', delimiter=',', dtype=int)
d
# savetxt y loadtxt trabajan con archivos de texto plano
# save y load trabajan con archivos binarios
np.save('arreglo_binario.npy',a)
get_ipython().run_line_magic('load', 'arreglo_binario.npy')
b = load('arreglo_binario.npy')
b = np.load('arreglo_binario.npy')
b
