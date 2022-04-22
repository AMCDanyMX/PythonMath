#importamos a sympy como sp
import sympy
#Declaramos los símbolos que usaremos
x, y = sympy.symbols('x y')
#Utilizamos el método init_printing
sympy.init_printing(use_unicode=True)

#Limite1
sympy.limit((2-sympy.sqrt(x-2))/(x**2-36), x, 6)

#Limite2
sympy.limit((x**2-4)/(x-2), x, 2)

#Limite3
sympy.limit((sympy.sin(x))/(x), x, 0)

#Limite4
sympy.limit((5*x**2-8*x-13)/(x**2-5), x, 3)