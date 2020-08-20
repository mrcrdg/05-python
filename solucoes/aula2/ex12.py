#!/usr/bin/env python3

# 12 - O python tem uma implementacão padrão de uma funcão sum para achar a soma dos elementos de uma lista, faca sua própria implementacão da funcão
#sum([1, 2, 3])
#6

index = int(input("Insira a quantidade de elementos: "))

def somaLista(index):
    lista = []

    for i in range(0, index):
        elemento = int(input())        
        lista.append(elemento)
    print(lista) 

#Função:
somaLista(index)


