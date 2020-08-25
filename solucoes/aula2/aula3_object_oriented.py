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

    __wordlist = []
    wordfreq = []
    worddict = {}

    #Construtor da classe: Abre o arquivo e implementa uma lista com as palavras do texto    
    def __init__(self, fileName):
        self.fileName = open(fileName, "r")
        self.wordlist = self.separarPalavras()     
  
    def __str__(self):
        return ("A quantidade de palavras: " + str(self.wordlist))
   
    #Alocar palavras em uma lista de Strings (lista words[])
    def separarPalavras(self):
            text = self.fileName.read()
            wordlist = text.split()
            return wordlist
    
    # Retorne individualmente cada palavra do texto
    def returnWords(self):
        for w in self.wordlist:
            self.wordlist.count(w)
            print(w) #GAMBS
    
    #Contar a quantidade total de palavras em words[]
    def countWords(self):
        count = len(self.wordlist)
        return count

    #Conte a quantidade de ocorrências de cada palavra do texto
    def wordFreq(self): 
        #for w in self.wordlist:
            #self.wordfreq = self.wordlist.count(w)
        self.wordfreq = [self.wordlist.count(w) for w in self.wordlist]
        return self.wordfreq 

    # Criar um dicionario contendo: a palavra & sua frequencia no texto
    def wordFreqDict(self):
        #self.wordfreq = [self.wordlist.count(w) for w in self.wordlist]
        #print(self.wordfreq)
        self.worddict = dict(list(zip(self.wordlist,self.wordFreq())))
        return self.worddict

    # Identificar as 10 paralvras mais frequentes    
    def top10frequency(self):        
        frequencyWords = sorted(self.worddict.keys(), reverse=True, key=lambda x: x)
        top10words= frequencyWords[0:10]
        
        frequecyList = sorted(self.worddict.values(), reverse=True, key=lambda x: x)        
        top10list= frequecyList[0:10]
        
        frequency = dict(list(zip(top10words,top10list)))
        
        #print(frequencyWords)
        #print(frequecyList)
        #print(frequency)
        return frequency

    # Retornar a média e desvio padrão da quantidade de ocorrências
    def meanAndDeviation(self):
        #Calcular a media: (soma de todos os valores / TotaldePalavras)
        mean = sum(self.wordFreq())/self.countWords()
        
        #Calcular a variâcia (Fazer a diferença entre todos os elementos e a média dos valores, elevar a diferença ao quadrado e somar as diferenças)
        for i in self.wordFreq():
            templist = [pow((i - mean),2)]
        variance = sum(templist)

        #Calcular o Desvio Padrão: (variancia / (TotaldePalavras -1))
        deviation = variance / (self.countWords() - 1)

        return (mean, deviation)


    # Cadastre StopWords (A classe deve possuir um atributo com uma lista de StopWords)

        





#Cria o objeto da classe Textfile
file1 = Textfile(input("Insira o nome do arquivo: "))
print("***** Retorna uma lista de String:")
print(file1)
#print(type(file1))
print("***** Conta quantas palavras existem no texto:")
print(file1.countWords())
print("***** Retorne individualmente cada palavra do texto: ")
#print(file1.returnWords())
print("***** Conte a quantidade de ocorrências de cada palavra do texto:" )
print(file1.wordFreq())
print("***** Imprime a repetição de cada palavra no texto:")
print(file1.wordFreqDict())
print("***** Imprime as 10 paralvras mais frequentes:")
print(file1.top10frequency())
print("***** Retorne a média e o desvio padrão da quantidade de ocorrências:")
print(file1.meanAndDeviation())






