#!/usr/bin/env python3

#1 - Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.

n1 = int(input("Insert first number: "))
n2 = int(input("Insert second number: "))

def menorNumero(a, b):
    return(a > b)

if (menorNumero(n1,n2)):
    print (n1 + ' é maior que ' + n2)
else:
    print(n2 + ' é maior que ' + n1)

