#!/usr/bin/env python3

# 6 - Escreva uma funcão para verificar a velocidade de motoristas. Essa funcão deve ter um parametro: speed.
#1.  Se speed menor que 70, deve imprimir “Ok”.
#2.  Case contrário, para cada 5km/h acima do limite (70), o radar deve aplicar um ponto na carteira do motorista, imprimindo quantos pontos foram retirados. Por exemplo, se speed é 80, Deve imprimir: “Pontos: 2”.
#3.  Se o motorista tomar mais que 12 pontos, a funcão deve imprimir: “Licen suspended”

speed= int(input("Insira a velocidade: "))

#Função que verifica speed abaixo da velocidade permitida
def velocidade(speed):
    return (speed <= 70)

#Função somar a pontuação 
def somarPontos(speed):
    return((speed/5) - 14)

#Regras
if (velocidade(speed)):
    print("Velocidade OK")
elif (somarPontos(speed) < 12):
    print("Pontos retirados: " + str(somarPontos(speed)))
else:
    print("Carteira suspensa.")