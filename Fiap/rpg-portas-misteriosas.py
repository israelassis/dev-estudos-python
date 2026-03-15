import random

"""
RPG das Portas Misteriosas
--------------------------
Um mini jogo em Python onde o jogador precisa atravessar 5 portas para chegar ao tesouro.
Em cada rodada, uma porta aleatória contém um monstro. Se o jogador escolher essa porta,
perde uma vida. O jogo termina quando o jogador perde todas as vidas ou atravessa as 5 portas.

Regras de Negócio:
- O jogador começa com 2 vidas.
- Cada porta atravessada com segurança dá +10 pontos.
- Se chegar ao baú do tesouro, ganha +50 pontos extras.
- O jogo é baseado em escolhas do usuário e sorteio aleatório.
"""
# variaveis
vidas = 2
pontos = 0
contador_passagens = 0

print("="*30)
print("\nBem-vindo ao RPG das Portas Misteriosas!")
print("\nVocê tem 2 vidas e precisa atravessar 5 portas para chegar ao tesouro.\n")
print("Antes que o Monstro de ache.. Consegue?  == Boa sorte! == ")

# Molde visual das portas
def mostrar_portas():
    print("""
  
    [1]   [2]   [3]   [4]   [5]
   _____ _____ _____ _____ _____
  |     |     |     |     |     |
  |     |     |     |     |     |
  |_____|_____|_____|_____|_____|
     """)

while contador_passagens < 5 and vidas > 0: #Garante que o jogo só roda enquanto o jogador não tiver passado pelas 5 portas e ainda tiver vidas
    """
    Lógica principal:
    - while → controla o loop do jogo (continua até vidas > 0 e passagens < 3).
    - if/else → verifica se o jogador encontrou o monstro ou passou com segurança.
    - contador_passagens → marca quantas portas já foram atravessadas.
    - pontos → acumula a pontuação do jogador.
    """
    mostrar_portas()
    monstro = random.randint(1, 5) #sorteia aleatoriamente a porta do monstro.
    escolha = int(input("\nEscolha uma porta (1, 2, 3, 4 ou 5 ): "))

    if escolha == monstro: #verifica se o jogador caiu na porta errada.
        vidas -= 1
        print("\n💀  Um monstro horrível apareceu! Você perdeu uma vida.")
        print(f"\nVidas restantes: {vidas}\n")
        if vidas == 0:
            print("\tFim de jogo! O monstro gargalha enquanto você foge.")
            break
    
    elif escolha == monstro:
        vidas -= 1
        print("\n💀  Um monstro horrível apareceu! Você perdeu uma vida.")
        print(f"\nVidas restantes: {vidas}\n")
        if vidas == 0:
            print("\tFim de jogo! O monstro gargalha enquanto você foge.")
            break
    
    elif escolha == monstro:
        vidas -= 1
        print("\n💀  Um monstro horrível apareceu! Você perdeu uma vida.")
        print(f"\nVidas restantes: {vidas}\n")
        if vidas == 0:
            print("\tFim de jogo! O monstro gargalha enquanto você foge.")
            break
        
    elif escolha == monstro:
        vidas -= 1
        print("\n💀  Um monstro horrível apareceu! Você perdeu uma vida.")
        print(f"\nVidas restantes: {vidas}\n")
        if vidas == 0:
            print("\tFim de jogo! O monstro gargalha enquanto você foge.")
            break
    
    elif escolha == monstro:
        vidas -= 1
        print("\n💀 Um monstro horrível apareceu! Você perdeu uma vida.")
        print(f"\nVidas restantes: {vidas}\n")
        if vidas == 0:
            print("\nFim de jogo! O monstro gargalha enquanto você foge.")
            break
        
    else:
        pontos += 10
        contador_passagens += 1

        #e vidas chegam a 0 → derrota; se passa 5 portas → vitória com bônus.

        print("\n✅ Você atravessou com segurança +10 pontos.")
        print(f"\nPontuação atual: {pontos}\n")

if contador_passagens == 5 and vidas > 0:
    pontos += 50
    print("\n🎉 Você encontrou o baú do tesouro!")
    print(f"\nPontuação final: {pontos}")


print("\tNos vemos na próxima Aventura!")
print("="*30)