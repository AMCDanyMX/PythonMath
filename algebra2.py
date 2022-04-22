import numpy as np
from numpy import *

x = np.array([[0, 2, 2],[5, 6, 1],[1, 2, 3]])

y = np.array([[7, 4, 2],[9, 3, 4],[1, 1, 1]])

#operaciones matrices
print(x+y)
print(x-y)
print(x*2)
print(y*5)

#ver dimencion 
print(x.shape)

#ver cantidad de elementos en la matriz
print(y.size)




#Multiplicacion de matrices
# Ejemplo multiplicación de matrices
mat1 = np.arange(1, 13).reshape(3, 4) #matriz de dimension 3x4
print(mat1)

mat2 = np.arange(8).reshape(4,2) #matriz de dimension 4x2
print(mat2)

# Multiplicando x por y 
print(x @ b) #resulta en una matriz de dimension 3x2




#MATRIZ IDENTIDAD
# Creando una matriz identidad de 2x2
miden = np.eye(2)
print(miden)


# Multiplicar una matriz por la identidad nos da la misma matriz
mat = np.array([[4, 7],[2, 6]])
print(mat)

print(miden @ mat)# miden * mat = miden

# Calculando el determinante de la matriz A
print(np.linalg.det(mat))


# Calculando la inversa de A.
matrizinv = np.linalg.inv(mat)
print(matrizinv)


# Trasponiendo una matriz
mat = np.arange(6).reshape(3, 2)
print(mat)

print(np.transpose(mat))


#SISTEMAS DE ECUACIONES  3X3 PARA EJEMPLO CHIDO
# Creando matriz de coeficientes
sistemaec = np.array([[2, 2, 2],
              [-2, 7, 7],
              [7, -1, 4]])
print(sistemaec)

#matriz de resultados
resultados = [2,4,6]
print(resultados)

# Resolviendo sistema de ecuaciones
sistemax = np.linalg.solve(sistemaec, resultados)
print(sistemax)


# Comprobando la solucion
print(sistemaec @ sistemax == resultados)
