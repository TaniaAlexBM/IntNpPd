# coding: utf-8
import numpy as np
A = np.array([
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])
# Transposición
A.T
A[:,4].sum
A[:,4].sum()
A.T[4].sum()
A.shape
A.T.shape
get_ipython().run_line_magic('save', 'transposicion 50-59')
