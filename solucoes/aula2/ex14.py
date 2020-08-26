#!/usr/bin/env python3

#14 - Implemente uma funcão ``product``, para computar o produto de uma lista de números.

#Criar a definir o tamanho de uma lista
lista = []
n = int(input("Insira o tamanho da lista: "))

#Iteração para preencher a lista
def preencherLista(n):
    for i in range(0, n):
        elemento = int(input("Preencha a lista: "))
        lista.append(elemento) #Adicionar elemento ao fim da lista
    return lista

def calcularProduto(lista):
    produto = 1
    for i in lista:
        produto *= i
    return produto

#Retorno da lógica: O produto da lista
print("O produto da lista: " + str(calcularProduto(preencherLista(n))))

#Teste utilizando a função Reduce()
from functools import reduce
calcularProduto = reduce((lambda x, y: x * y), lista)
print("Utilizando a função Reduce(): " + str(calcularProduto))