#!/usr/bin/env python3

a = 2 + 3
print('2 + 3 is', a)

#​ 2)Crie um script Python que imprime na tela hello, world! quatro vezes.​

i = 0
for i in range(4):
    print('Hello!')

# 3)Crie um script python com o seguinte conteúdo e veja a saída:​`​1 + 2`

a = 1 + 2
print ("1 + 2")
print(a)

#4)
x = 4
y = x + 1
x = 2
print(x,y)
#2,5

#5)
x, y = 2, 6
x, y = y, x + 2
print(x,y)
#6 4

#6)
a, b = 2, 3
#c, b = a, c + 1 - Erro de leitura do compilador
c = a
b = c + 1
print(a, b, c)
#2, 3, 2

#7): Quantas multiplicacões são executadas quando cada uma das linhas de código são executadas?​

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5)) # São executadas 2 multiplicações 5 * 5
print(square(2*5)) # são executadas 34 multiplicações 2 * 5 * 2 * 5

#8): Qual será a saída dos próximos programas?​
print('ex8')

x = 1
def f():
    return x
print(x)
print(f())
#Saídas serão: 1 e 1

#9):​​
print('ex9')

x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)
#Saídas serão: 1, 2, 2


#10):​
print('ex10')

x = 1
def f():
    x = 2 #Substitui a posição da linha inferior
    y = x	
    return x + y
print(x)
print(f())
print(x)
#Saídas serão: 1, 4, 1

#11):​
print('ex11')

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)
#Saídas serão: (2, 9)











