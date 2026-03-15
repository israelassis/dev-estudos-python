import random

def jogar_rpg_portas():
  """
  Executa o mini-jogo RPG das Portas Misteriosas.
  """

  # Inicialização de variáveis
  vidas = 3
  portas_atravessadas = 0
  total_portas = 5

  print("--------------------------")
  print("Bem-vindo ao RPG das Portas Misteriosas!")
  print("Sua missão: Atravessar 5 portas misteriosas para encontrar o tesouro lendário.")
  print(f"Cuidado! Uma porta aleatória em cada rodada contém um monstro espreitando.\nVocê começa com {vidas} vidas. Boa sorte!")
  print("--------------------------")
  print("""\n
      [1]   [2]   [3]   [4]   [5]
   _____ _____ _____ _____ _____
  |     |     |     |     |     |
  |     |     |     |     |     |
  |_____|_____|_____|_____|_____|
     """)

  # Loop principal do jogo - continua enquanto tiver vidas e portas para atravessar
  while vidas > 0 and portas_atravessadas < total_portas:
    print(f"\n--- Rodada {portas_atravessadas + 1} ---")
    print(f"Você está diante de {total_portas - portas_atravessadas} portas misteriosas.")

    # Sorteia qual porta contém o monstro (entre 1 e o número de portas restantes)
    porta_monstro = random.randint(1, total_portas - portas_atravessadas)

    # Solicita a escolha do jogador
    try:
      # Validação simples para garantir que a entrada é um número inteiro válido
      escolha = int(input(f"Escolha uma porta (1 a {total_portas - portas_atravessadas}): "))

      if escolha < 1 or escolha > (total_portas - portas_atravessadas):
          print("Porta inválida! Tente novamente.")
          continue # Reinicia o loop para a mesma rodada

    except ValueError:
      print("Entrada inválida! Por favor, digite um número inteiro.")
      continue # Reinicia o loop para a mesma rodada

    # Verifica a escolha do jogador
    if escolha == porta_monstro:
      print("\nOH NÃO! Você abriu a porta e deu de cara com um monstro terrível!")
      vidas -= 1
      if vidas > 0:
        print(f"Você lutou bravamente, mas perdeu uma vida. Restam {vidas} vidas.")
      else:
        print("Infelizmente, você perdeu todas as suas vidas lutando contra o monstro.")
    else:
      print("\nUfa! Você atravessou a porta com segurança.")
      portas_atravessadas += 1
      print(f"Você já atravessou {portas_atravessadas} de {total_portas} portas.")

  # Mensagem final dependendo do resultado
  print("\n--------------------------")
  if portas_atravessadas == total_portas:
    print("PARABÉNS! Você atravessou todas as portas misteriosas e encontrou o TESOURO LENDÁRIO!")
    print("Sua coragem e astúcia o levaram à vitória!")
  else:
    print("FIM DE JOGO. Mais sorte na próxima vez, aventureiro!")
  print("--------------------------")

# Inicia o jogo
if __name__ == "__main__":
  jogar_rpg_portas()