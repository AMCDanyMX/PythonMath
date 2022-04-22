#importamos a sympy como sp
import sympy
#Declaramos los símbolos que usaremos
x, y = sympy.symbols('x y')
#Utilizamos el método init_printing
sympy.init_printing(use_unicode=True)


#CALCULANDO DERIVADAS
#Derivadas
sympy.diff(sympy.cos(x), x)

#Derivada de una potencia
sympy.diff(5/x**5, x)

#2ejemplo derivadas
sympy.diff((5/x**5) + (3/x**2), x)

#3er ejemplo derivadas
sympy.diff((x**2+3*x-2)**4, x)

#4to ejempl oderivadas
sympy.diff(sympy.sqrt(x**2 - 2*x + 3))

#Derivada de una función logarítmica
sympy.diff(sympy.log(2*x**4 - x**3 + 3*x**2 - 3*x))


