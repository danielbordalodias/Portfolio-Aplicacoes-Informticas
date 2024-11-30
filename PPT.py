import random

print("Bem-vindo ao jogo do Pedra, Papel ou Tesoura!")
    
while True:
    njogadas = int(input("Quantas rondas vai ter a partida?: "))
        

    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0
    
    
    for i in range(njogadas):
        print("Ronda",i+1)
        
        while True:
            print("Escolhe a tua jogada:")
            print("1 - Pedra; 2 - Papel; 3 - Tesoura")
            jogada_jogador = input("Jogada:")
            
            jogada_computador = random.randint(1,3)
            
            if jogada_jogador in ['1','2','3'] :
                print("Escolheste", jogada_jogador)
                print("O Computador escolheu", jogada_computador) 
            else:
                print("Escolha inválida. Perdeste esta rodada.")
            vitorias_computador += 1
            break
    
            
            
    if jogada_jogador == '1' and jogada_computador == 1:
        print("Empate.")
        empates += 1
    elif jogada_jogador == '2' and jogada_computador == 2:
        print("Empate.")
        empates += 1
    if jogada_jogador == '3' and jogada_computador == 3:
        print("Empate.")
        empates += 1
    
    
    if jogada_jogador == '1' and jogada_computador == 2:
        print("O computador venceu esta rodada.")
        vitorias_computador += 1
    elif jogada_jogador == '1' and jogada_computador == 3:
        print("Venceste esta rodada.")
        vitorias_jogador += 1
    if jogada_jogador == '2' and jogada_computador == 1:
        print("Venceste esta rodada.")
        vitorias_jogador += 1
    elif jogada_jogador == '2' and jogada_computador == 3:
        print("O computador venceu esta rodada.")
        vitorias_computador += 1
    if jogada_jogador == '3' and jogada_computador == 1:
        print("O computador venceu esta rodada.")
        vitorias_computador += 1
    elif jogada_jogador == '3' and jogada_computador == 2:
        print("Venceste esta rodada.")
        vitorias_jogador += 1
    
        

    print("Obrigado por jogar! Aqui estão os resultados:")
    print("Vitórias do jogador:", vitorias_jogador,)
    print("Vitórias do computador:", vitorias_computador,)
    print("Empates:", empates,)
        

    jogar_novamente = input("Deseja jogar outra partida? (S/N): ")
    if jogar_novamente != 'S':
        print("Obrigado por jogar! Até a próxima!")
        break