import random

print("=== JOKENPÔ ===")
opcoes = ["pedra", "papel", "tesoura"]

# Jogador escolhe
jogador = input("Escolha: Pedra, Papel ou Tesoura: ").lower()

# Computador escolhe
computador = random.choice(opcoes)

print(f"\nVocê escolheu: {jogador}")
print(f"\nO computador escolheu: {computador}")

# Regras do jogo
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("\nVocê venceu!")
else:
    print("\nVocê perdeu!")
