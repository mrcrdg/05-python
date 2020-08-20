#!/usr/bin/env python3

#10 - Escreva uma funcào que retorna a soma de múltiplos de 3 e 5 entre 0 e limit (parâmetro). Por exemplo, se limite for 20, deve retornar a soma de 3, 5, 6, 9, 10, 12, 15, 18, 20.

limit = int(input("Insira o limite: "))

def showMultiples(limit):
    for i in range(limit+1):
        if i%3 ==0  or i%5 ==0:
            print (i)

showMultiples(limit)
#print(sum(showMultiples(limit)))






