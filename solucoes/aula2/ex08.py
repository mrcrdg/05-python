#!/usr/bin/env python3

# 8 - Escreva uma funcão show_stars(rows). Se rows for 5, deve-se imprimir o seguinte:

rows = int(input("Insert a number of rows: "))

def showStars (row):
    print ("```")
    screen = "*"
    for i in range(row):
        print(screen)
        screen = screen + "*"
    print("```")

showStars(rows)