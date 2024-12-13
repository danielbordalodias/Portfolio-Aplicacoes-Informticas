palavra = input("Qual a palavra?(Escreve a palavra em maiúsculas) ")
tentativas = int(input("Quantas tentativas erradas?"))
print("\n" * 20)

print("Para jogar o jogo da forca, sempre que for escrever a letra, use sempre maiúsculas nas tentativas.")
print("Bom jogo!")
print("\n" * 5)

palavra_escondida = "_" * len(palavra)
erros = 0
letras_jogador = ""

while tentativas > erros and "_" in palavra_escondida:
    print("Palavra:", palavra_escondida)
    letra = input("Qual a letra? ")

    if letra in letras_jogador:
            print("Já tentaste essa letra! Escreve outra.")
            continue

    letras_jogador += letra 

    if letra in palavra:
            palavra_escondidan = ""
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_escondidan += letra
                else:
                    palavra_escondidan += palavra_escondida[i]
            palavra_escondida = palavra_escondidan
    else:
            erros += 1
            print("Erros:", erros)

    if erros == tentativas:
            print("\nGAME OVER!")
            print("Erraste", erros, "vezes!")
            print("A palavra era:", palavra)
            break

if "_" not in palavra_escondida:
    print("\nParabéns! Advinhaste a palavra!")
    print("A palavra era:", palavra)
else:
    print("\nFim do jogo.")
