print("Olá!")
print ("Este é o protótipo do jogo Jokenpo")
print ("Vamos jogar?")

print("""
pedra
      
papel
      
tesoura
      """)
try:
    minhaEscolha = input("Jogador 1 - Escolha pedra, papel ou tesoura: ")
    suaEscolha = input("Jogador 2 - Escolha pedra, papel ou tesoura: ")
    if minhaEscolha == "pedra":
        if suaEscolha == "papel":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "tesoura":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif minhaEscolha == "papel":
        if suaEscolha == "pedra":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "tesoura":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif minhaEscolha == "tesoura":
        if suaEscolha == "pedra":
            print("Jogador 2 ganhou! Jogador 1 escolheu ", minhaEscolha)
        elif suaEscolha == "papel":
            print("Jogador 2 perdeu! Jogador 1 escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
        
except:
    print("Algo deu errado!")