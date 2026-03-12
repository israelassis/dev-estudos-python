import random #escolha aleatroia

print("\n=== JOKENPÔ ===")
opcoes = ["pedra", "papel", "tesoura"]
resposta="S" # reiniciar loop

# Jogador escolhe
print("== Regras do Jogo: \nPedra ganha da tesoura -> Papel ganha da pedra -> Tesoura ganha do papel\n")

while resposta == "S":
    jogador = input("\nEscolha uma Opção:  Pedra,  Papel  ou  Tesoura: ").lower() 

# Computador escolhe
    computador = random.choice(opcoes) #computador escolhe aleatoriamente uma opção da lista opcoes

    print(f"\nVocê escolheu: {jogador}") #escolha da lista
    print(f"\nO computador escolheu: {computador}") #escolha aleatroia - random

# Regras do jogo
    if jogador == computador:
        print("\t Empate!".upper())
    elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
        print("\t ✅ Você venceu!".upper())
    else:
        print("\t ❌ Você perdeu!".upper())

    resposta =input("Deseja jogar novamente: (S/N) ? ").upper()
    print("\n"+"=="*20)
    print("  Jogo Finalizado! Obrigado por jogar.")
    print("=="*20)
    """
    Empate → if
    Vitória do jogador → elif
    Vitória do computador → else
    """
