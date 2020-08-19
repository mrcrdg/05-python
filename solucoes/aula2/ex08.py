#!/usr/bin/env python3

# 8 - Escreva uma funcão show_stars(rows). Se rows for 5, deve-se imprimir o seguinte:

rows = input("Insert a number of rows: ")

for num in range(rows):
    for i in range(num):
        print(str(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")