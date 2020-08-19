#!/usr/bin/env python3

#5 - Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.
import math

number = int(input("Insert a number: "))

#Verifica se number é positivo
def positivo(n):
    return(n >= 0)

#Operacoes
if (positivo(number)):
    print(math.sqrt(number))
else:
    print(number**2)
