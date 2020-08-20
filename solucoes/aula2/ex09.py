#!/usr/bin/env python3

# 9 - Escreva uma funcão chamada showNumbers, que recebe o parâmetro limit. A funcão deve imprimir todos os números entre 0 e limit com uma label para identificar se o número é par ou ímparPor exemplo, se o limite for 3, deve-se imprimir:

limit = int(input("Insira um numero: "))

def showNumbers (limit):
    for i in range(limit+1):
        if (par(i)):
            print(str(i) + ' PAR')
        else:
            print(str(i) + ' IMPAR')

def par(n):
    return (n % 2 == 0)

showNumbers (limit)
    


