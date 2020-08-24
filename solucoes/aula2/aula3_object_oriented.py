#!/usr/bin/env python3

# Modele uma classe que realiza as seguintes operações em um arquivo texto:
# Represente um texto como uma lista de Strings
# Retorne individualmente cada palavra do texto
# Conte a quantidade de ocorrências de cada palavra do texto
# Retorne as 10 palavras mais frequentes
# Retorne a média e desvio padrão da quantidade de ocorrências
# Cadastre StopWords (A classe deve possuir um atributo com uma lista de StopWords)
# Retorne um novo arquivo eliminando todas as StopWords do texto
# Inclua um método que retorne a distância entre duas palavras


class Textfile(object):
        
    def __init__(self, fileName):
        self.fileName = fileName
        self.words = self.fileText()
   
    # Open a file and return its words in an array: 
    def fileText(self):
        with open(self.fileName, "r") as fileOpened:
            text = fileOpened.read()
            words = text.split()
            print(type(words))
            #print(len(words))
            return words

    #Quantidade de palavras em words[]
    def countWords(self):
        return(len(self.words))

    def close(self):
        if self.fileName:
            self.fileName.close()
            self.fileName = None
  
    def __str__(self):
        return ("A quantidade de palavras: " + str(self.words))


texto1 = Textfile(input("Insira o nome do arquivo: "))
print(texto1)
#print(type(texto1))
print(texto1.countWords)