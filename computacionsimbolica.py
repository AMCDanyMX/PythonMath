import sympy
x, y = sympy.symbols('x y')


exp = 2*x**2 - 7*x + 3
print(exp)


#multipliquemos por algun numero 
print(exp*5)

#sumemos

#restemos



#CAMBIANDO A SIMBOLOS MAS VISUALES
import sympy
x, y = sympy.symbols('x y')
exp = 2*x**2 - 7*x + 2
sympy.init_printing(use_unicode=True)
exp