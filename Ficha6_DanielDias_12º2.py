#Exercício1
#import random

#for i in range(1):
#    print(random.randint(0,9))
    
#for i in range(1):
#    print(random.randint(1,10-1))
    
#Exercício2
#import random

#print(random.randint(0,6))

#Exercício3
#import random

#num=random.randint(1,6)

#print("o nº saído após o lançamento do dado foi:", num)

#Exercício4
#import random

#r=input("Lançar dado(s/n)?:")

#while r == "s":
#    num=random.randint(1,6)
#    print("O nº saído após o lançamento foi:",num)
#    r=input("Lançar dado(s/n)?:")
    
#print("Programa terminado.")

#Exercício5
#import random

#resposta == "1"

#while resposta != "1":
#    resposta=input("Quantos dados(1,2,s-sair)?:")
#    if resposta == "1":
#        num=random.randint(1,6)
#        print("O valor que saiu no dado é ", num)
#    elif resposta == "2":
#        num=random.randint(1,6)
#        num2=random.randint(1,6)
#        print("O valor que saiu no primeiro dado é ", num)
#        print("O valor que saiu no segundo dado é ", num2)
#        print("O valor que saiu no total é ", num + num2)
        
#    else:
#        print("Programa Terminado")
#        break
    
#Exercício6
#No randrange o valor final não é incluído ao intervalo de números possíveis gerados, enquanto que no randint
#o valor final é incluído

#Exercício7
#import random
#num1 = random.randint(1, 50)
#num2 = random.randint(1, 50)
#num3 = random.randint(1, 50)
#num4 = random.randint(1, 50)
#num5 = random.randint(1, 50)

#estrelal = random.randint(1, 11)
#estrela2 = random.randint(1, 11)
#print("A chave do euromilhões é:", num1, num2, num3, num4, num5,
#" e estrelas: ", estrelal, estrela2)

#Exercício8
#import random
#num = random.randint(1, 10)
#print("Adivinha o número oculto entre 1 e 10.")
#while True:
#    a = int(input("Qual é o teu palpite? "))
#    if a == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        print("Erraste. Tenta novamente!")

#Exercício9
#import random
#num = random.randint(1, 10)
#print("Adivinha o número oculto entre 1 e 10.")
#tent = 3
#while tent > 0:
#    n = int(input("Qual é o teu palpite? "))
#    if n == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        tent -= 1
#        if tent > 0:
#            print("Erraste. Tens" , tent , "tentativa(s) restante(s).")
#       else:
#            print("Que pena! Não foi desta. Tenta outra vez!")
            
#Exercício10
#import random
#i = int(input("Qual é o número inicial do intervalo? "))
#f = int(input("Qual é o número final do intervalo? "))
#tent = int(input("Quantas tentativas tens? "))
#num= random.randint(i, f)
#print(f"Adivinha o número oculto entre" ,i , "e" ,f,"!")
#while tent > 0:
#    a = int(input("Qual é o teu palpite? "))
#    if a == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        tent -= 1
#        if tent> 0:
#            print("Erraste. Tens" ,tent , "tentativa(s) restante(s).")
#        else:
#            print("Que pena! Não foi desta. Tenta outra vez!")
            
#Exercício11
#import random
#i = int(input("Qual é o número inicial do intervalo? "))
#f = int(input("Qual é o número final do intervalo? "))
#tent = int(input("Quantas tentativas tens? "))
#num = random.randint(i, f)
#print("Adivinha o número oculto entre" ,i , "e" ,f , "!")
#while tent > 0:
#    try:
#        a = int(input("Qual é o teu palpite? "))
#        if a < i or a > f:
#            print("O número introduzido é inválido! Deve estar entre" ,i , "e" ,f ,".")
#            continue
#        if a == num:
#            print("PARABÉNS!! Acertaste no número!")
#            break
#        else:zx sz
#            tent -= 1
#            if tent > 0:
#               print("Erraste. Tens" ,tent , "tentativa(s) restante(s).")
#            else:
#                print("Que pena! Não foi desta. Tenta outra vez!")
#    except ValueError:
#        print("Entrada inválida! Por favor, introduz um número inteiro.")

    
#Exercício12
#import random   
   
#print("Qual a dimensão do tabuleiro de jogo?")
#a=int(input("Dimensão horizontal:"))
#b=int(input("Dimensão vertical:")) 

#barco_x = random.randint(1, a)
#barco_y = random.randint(1, b)

#tent = 0
#acertou = False
#while not acertou :
#    print("X para a tentativa " ,tent , ": ", end="")
#    x = int(input())
#    print("Y para a tentativa " ,tent ,": ", end="")
#    y = int(input())


#    if x == barco_x and y == barco_y:
#        print("PARABÉNS!!! Acertaste em cheio à", tent, "tentativa.")
#        acertou = True
#    else:
#        dicas=[]
#        if x < a:
#            dicas.append("Este")
#        elif x > a:
#            dicas.append("Oeste")
#        if y < b:
#            dicas.append("Norte")
#        elif y > b:
#            dicas.append("Sul")    
#        print("Água! Tenta para " , ', '.join(dicas) ,)
            
    
#Exercício13
#import random   
   
#print("Qual a dimensão do tabuleiro de jogo?")
#a=int(input("Dimensão horizontal:"))
#b=int(input("Dimensão vertical:"))
#c=int(input("Profundidade:"))

#barco_x = random.randint(1, a)
#barco_y = random.randint(1, b)
#barco_z = random.randint(1, c)

#tent = 0
#acertou = False
#while not acertou :
#    tent += 1
#    print("X para a tentativa " ,tent , ": ", end="")
#    x = int(input())
#    print("Y para a tentativa " ,tent ,": ", end="")
#    y = int(input())
#    print("Z para a tentativa " ,tent ,": ", end="")
#    z = int(input())

#    if x == barco_x and y == barco_y and z == barco_z
#        print("PARABÉNS!!! Acertaste em cheio à", tent, "tentativa.")
#        acertou = True
#    else:
#        dicas=[]
#        if x < a:
#            dicas.append("Este")
#        elif x > a:
#            dicas.append("Oeste")
#        if y < b:
#            dicas.append("Norte")
#        elif y > b:
#            dicas.append("Sul")    
#        if z < c:
#            dicas.append("Acima")
#        elif z > c:
#            dicas.append("Abaixo")
#        print("Água! Tenta para " , ', '.join(dicas) ,)



      










    
        

