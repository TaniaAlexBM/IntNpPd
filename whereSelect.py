# coding: utf-8
# WHERE y SELECT
# Permiten crear nuevos arreglos en función de ellas
import numpy as np
calificaciones = np.random.randint(1,11,10)
calificaciones
# Todas las calificaciones mayores e igual a siete son aprobatorias
# dos tipos de mensajes
# "Felicidades! Aprobaste la materia
# "Lo sentimos, no aprobaste la materia"
np.where(
calificaciones >= 7,
'Felicidades, aprobaste la materia',
'Lo sentimos, no aprobaste la materia')
calificaciones
# Se generó un nuevo arreglo y no modificó el arreglo original
# Para SELECT
# Se van a almacenar cuatro tipos de mensajes
# 'Felicidades, aprobaste la materia con 10'
# 'Felicidades, aprobaste la materia' = 8 o 9
# 'Aprobaste la materia' = 7
# 'Lo sentimos, no aprobaste la materia' < 7
condiciones = [
(calificaciones == 10),
((calificaciones == 8) | (calificaciones == 9)),
(calificaciones == 7),
(calificaciones < 7)]
opciones = []
opciones = []
opciones = [
'Felicidades, aprobaste la materia con 10',
'Felicidades, aprobaste la materia',
'Aprobaste la materia',
'Lo sentimos, no aprobaste la materia']
