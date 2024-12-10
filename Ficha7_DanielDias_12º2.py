#Exercício1
#s=(input("Escreve uma frase:"))
#print( len(s) )

#Exercício2
#s=(input("Escreve uma frase:"))

#frase_nova = ""

#for l in s:
#    if l == " ":
#        frase_nova += "_"
#    else:
#        frase_nova += l

#print(frase_nova)

#Exercício3
#s=(input("Escreve uma frase:"))

#for i in range(len(s)-1, -1, -1):
#     print(s[i], end="")

#Exercício4
#s=(input("Escreve uma frase:"))

#contador_espaço = 0
#contador_letras = 0

#for l in s:
#    if l == " ":
#        contador_espaço += 1
#    else:
#        contador_letras += 0

#print("O número de espaços nesta frase é", contador_espaço)

#Exercício5
#s=(input("Escreve uma frase:"))

#if s[-1] == ".":
#    print("A frase apresentada acaba com ponto final.")
#else:
#    print("A frase apresentada não acaba em ponto final.")

#Exercício6
#s=(input("Escreve um nome:"))

#if s[-1] == "a":
#    print("Provavelmente é uma rapariga.")
#else:
#    print("Provavelmente é um rapaz.")

#Exercício7
#s=(input("Escreve uma frase:"))

#if s[-1] == "!":
#    print("A frase apresentada é exclamativa.")
#elif s[-1] == "?":
#    print("A frase apresentada é interrogativa.")
#else:
#    print("A frase apresentada é afirmativa.")

#Exercício8
#s=(input("Escreve uma frase:"))

#if s[-1] == "!":
#    print("A frase apresentada é exclamativa.")
#elif s[-1] == "?":
#    print("A frase apresentada é interrogativa.")
#elif s[-1] == "?" and s[-2] == "!":
#    print("A frase apresentada é interrogativa exclamativa.")
#elif s[-1] == "!" and s[-2] == "?":
#print("A frase apresentada é interrogativa exclamativa.")
#else:
#    print("A frase apresentada é afirmativa.")

#Exercício9
"""
Atendendo ao formato normal do zoom do terminal, o número de caracteres que se pode escrever em cada linha da consola
pode ser determinado por:

a=input()
print(len(a))

O número de caracteres é 149.
"""

#Exercício10
#s=(input("Escreve um frase:"))

#largura_terminal=149
#espacos = largura_terminal - len(s)

#if espacos > 0:
#    print(" " * espacos + s)
#else:
#    print(s)

#Exercício11
#s=(input("Escreve um frase:"))

#largura_terminal=149
#espacos = 75 - len(s)

#if espacos > 0:
#    print(" " * espacos + s)
#else:
#    print(s)

#Exercício12
s=(input("Escreve um frase:"))

print("Escolha o tipo de alinhamento que quer(1,2,3)\n")
print("1 - Esquerda")
print("2 - Centro")
print("3 - Direita\n")
escolha=(input("Alinhamento:"))

if escolha not in ['1','2','3']:
    print("Escolha inválida, executa o programa novamente.")







