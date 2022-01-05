# coding: utf-8
# Transposición
import numpy as np
a = np.arange(0,10)
a.size
a = np.arange(0,10).reshape(2,5)
a
a.T
# T no modifica a la matriz, sólo muestra la transpuesta
a.transpose()
# transpose() no modifica a la matriz, sólo muestra la transpuesta
