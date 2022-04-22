#importamos a sympy como sp
import sympy
#Declaramos los símbolos que usaremos
x, y = sympy.symbols('x y')
#Utilizamos el método init_printing
sympy.init_printing(use_unicode=True)


#integral 1
sympy.integrate(1/x**2)


#integal 2
sympy.integrate(3*x**2)


#ntegral 3
sympy.integrate(x**2*sympy.log(5*x))

