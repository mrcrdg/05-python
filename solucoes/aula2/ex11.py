#!/usr/bin/env python3

#11 - Escreva uma funcão que imprima todos os números primos entre 0 e limit (um parâmetro).

limit = int(input("Insira o limite: "))

def prime(limit):
    for i in range(2,limit+1):
        multiplos = 0
        for j in range(2,i):
            if i % j ==0:
                multiplos += 1
        if multiplos == 0:
            print ("{} é primo".format(i))

prime(limit)




