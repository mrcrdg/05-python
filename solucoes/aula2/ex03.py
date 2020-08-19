#!/usr/bin/env python3

# 3 - Considere uma equação do segundo grau f(x)=a⋅x2+b⋅x+c. 
# A partir dos coeficientes, determine se a equação possui duas raízes reais, uma, ou se não possui.

a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))

def bhaskara(a, b, c):
    
    delta = (b**2 - (4 * a * c))
    print (delta)
    if (delta > 0):
        return 2
    elif (delta == 0):
        return 1       
    else:
        return 0

print ("Quantidade de raízes: "+ str(bhaskara(a, b, c)))


