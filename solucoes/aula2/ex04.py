#!/usr/bin/env python3

#4 - Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

number1 = int(input("Insert first number: "))
number2 = int(input("Insert second number: "))

#Função somar
def soma(n1, n2):
    return(n1+n2)
#print(str(soma(number1, number2)))  

#Função verificar se >20
def verificarValor():
    return(soma(number1, number2) > 20)
#print(str(verificarValor()))     

#Teste e adição
if (verificarValor()):    
    print(str((soma(number1, number2) + 8)))
else:
    print(str((soma(number1, number2) - 5)))

