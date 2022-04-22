# Vector como lista de Python
v1 = [2, 4, 6]
print(v1)
#2,4,6

# Vectores con numpy
import numpy as np
v2 = np.ones(3) # vector de solo unos.
print(v2)

v3 = np.array([1, 3, 5]) # pasando una lista a las arrays de numpy
print(v3)

v4 = np.arange(1, 8) # utilizando la funcion arange de numpy
print(v4)


#VECTORES OPERACIONES
# Ejemplo en Python
x = np.arange(1, 5)
y = np.array([2, 4, 6, 8])
print(x, y)

# sumando dos vectores numpy
print(x + y)

# restando dos vectores
print(x - y)
# multiplicando por un escalar
print(x * 2)
print(y * 3)

