#LOGARITMICAS Y EXPONENCIALES
import math
#Retorna e elevado a la x potencia,
# dónde e = 2.718281… es la base de los logaritmos naturales.
# Esto generalmente es más preciso que math.e ** x o pow(math.e, x).
math.exp(7)

#Con dos argumentos, retorna el logaritmo de x en la base dada, calculado como log(x)/log(base).
#Con un argumento, retorna el logaritmo natural de x (en base e).
math.log(5, 3)

#Retorna el logaritmo en base 2 de x. Esto suele ser más preciso que log(x, 2).
#a mano sería  log2(6) = base^numero = 6
math.log2(6)

#Retorna el logaritmo en base 10 de x. Esto suele ser más preciso que log(x, 10).
math.log10(8)

#Retorna x elevado a la potencia y
math.pow(2, 3)


#TRIGONOMETRICAS
#Retorna el arcocoseno de x, en radianes. El resultado está entre 0 y pi.s(x)
math.acos(80)

#Retorna el arcoseno de x, en radianes. El resultado está entre -pi/2 y pi/2.
math.asin(45)

#Retorna la arcotangente de x, en radianes. El resultado está entre -pi/2 y pi/2.
math.atan(30)

#Retorna el coseno de x radianes.
math.cos(25)

#Retorna el seno de x radianes.
math.sin(8)

#Retorna la tangente de x radianes.
math.tan(60)



#CONVERSIÓN ANGULAR
#Convierte el ángulo x de radianes a grados.
math.degrees(180)

#Convierte el ángulo x de grados a radianes.
math.radians(90)


#CONSTANTES
math.pi
#La constante matemática π = 3.141592…, hasta la precisión disponible.

math.e
#La constante matemática e = 2.718281…, hasta la precisión disponible.