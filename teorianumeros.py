import math 
#funcion que permite redondear al numero hacía arriba
math.ceil(17.2)

#funcion que permite redondear al numero hacía abajo
math.floor(17.2)

#valo0r absoluto de x
math.fabs(-7)

#Regresa el factorial de un numero x
math.factorial(6)  #6! = 6*5*4*3*2*1

#Retorna una suma precisa en coma flotante de los valores 
# de un iterable. Evita la pérdida de precisión mediante 
# el seguimiento de múltiples sumas parciales intermedias:
math.fsum([2,4.5,6])
math.sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#0.9999999999999999
math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#1.0


#maximo comun divisior de numeros
math.gcd(4,8)

#saber si un numero es infinito
math.isfinite(0)


#La raíz cuadrada del número 16 es 4, por lo que la función math.isqrt devuelve 4:
math.isqrt(16)

#Sin embargo, la raíz cuadrada de 15 es 3.87:
math.sqrt(15)
#3.872983346207417

#por lo que la función math.isqrt devuelve 3:
math.isqrt(15)
#3

