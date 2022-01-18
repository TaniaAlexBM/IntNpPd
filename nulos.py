# coding: utf-8
import pandas as pd
# valores nulos en numpy o pandas es con NaN
import numpy as np
np.nan
pd.Series([1,2,np.nan,np.nan,5,6,7,np.nan,8,9])
# Encontrar que valores hacen falta
# isnull - notnull
a = pd.Series([1,2,np.nan,np.nan,5,6,7,np.nan,8,9])
a.isnull
a.isnull()
a.notnull()
# conocer los índices que tengan valores nulos
a[a.isnull()]
a[a.notnull()]
# valores no nulos
