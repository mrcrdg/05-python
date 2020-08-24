#!/usr/bin/env python3

#13 - O que acontece quando a sua funcão sum é chamada com uma lista de strings? Voce consegue fazer a sua funcao funcionar com strings também?

a = 'hello'
b = 'world'
string = (a + b)
print(string)
print(sum(map(len, string)))
