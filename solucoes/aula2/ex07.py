#!/usr/bin/env python3

#7 - Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

argument = input("Insert a month: ")

def mes(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        
    }
    print (switcher.get(argument, "Invalid month"))
    func = mes.get(argument, lambda: "Invalid month")
    print (func())






