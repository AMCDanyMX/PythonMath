from fractions import Fraction

print("Fracciones")
print("operaciones basicas")  #Todas las operaciones 
n1 = Fraction(input("Digite un numero fraccionario, ejemplo(4/5) : "))	
print(n1)
n2 = Fraction(input("Digite un número fraccionario, ejemplo(3/4) :"))
print(n2)
print("Resultado suma:" + str(n1+n2))
print("Resultado resta:" + str(n1-n2))
print("Resultado multiplicacion:" + str(n1*n2))
print("Resultado division:" + str(n1/n2))
