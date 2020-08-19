#!/usr/bin/env python3

# 2) Para doar sangue é necessário:
#Ter entre 16 e 69 anos.
#Pesar mais de 50 kg.
#Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).

#Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h #para uma pessoa e diga se ela pode doar sangue ou não.

idade = int(input("Insira idade: "))
peso = int(input("Insira seu peso: "))
horasSono = int(input("Horas de sono: "))

def doadorSangue(id, ps, hS):
    if ((id < 16) or (id > 69) or (ps < 50) or (hS < 6)):
        return False    
    else:
        return True

if (doadorSangue(idade, peso, horasSono)):
    print("Pode doar sangue.")
else:
    print("Não pode doar sangue.")


