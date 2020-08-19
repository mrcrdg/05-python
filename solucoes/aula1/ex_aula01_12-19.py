#!/usr/bin/env python3

#12): Escreva a funcão count_digits que retorna quantos dígitos um número tem.
print('ex12')

def count_digits(number):
    return (len(str(number)))
print(count_digits(5456))


#13): Escreva uma funcão strcmp para comparar duas strings, ignorando se as letras são maiúsculas ou minúsculas.
print('ex13')

frase1 = 'asdfg'
frase2 = 'qwer'
frase3 = 'asdfg'
frase4 = 'ASdfg'

print(frase1 == frase2)
print(frase1 == frase3)
print(frase3 == frase2)
print(frase1.lower() == frase4.lower()) # case insensitive

#14): Qual será a saída dos próximos programas?​
print('ex14')

print(2 < 3 and 3 > 1) #Será True
print(2 < 3 or 3 > 1) #Será True
print(2 < 3 or not 3 > 1) #Será False
print(2 < 3 and not 3 > 1) #Será False

#15
print('ex15')

x = 4
y = 5
p = x < y or x < z
print(p)
#Output = True

#16
print('ex16')

#True, False = False, True
a = True
b = False
a, b = False, True
print(a, b)
print(2 < 3)
#Stdout = (False, True), (True)


#**17): O que acontece quando os seguinte códigos são executados? Algum erro acontece? explique a razão​
print('ex17')
#Sim, no caso de x!= 2, o seguinte erro acontece: name 'y' is not defined

x = 2
if x == 2:
    print(x)
else:
    print(y)

#18
print('ex18')
#No caso de x!= 2, o seguinte erro acontece: SyntaxError: invalid syntax x +

x = 2
if x == 2:
    print(x)
#else:
#    x + 

#19): Qual será a saída do seguinte programa?
print('ex19')

x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)

#Saída: x = [3, 1, 3], x = [3, 1, 3, 4], x = [3, 1, 2, 4]



