import random


##### - Basico ! Sem tratamento de Dados - Sujeito a quebra e vulnerável
"""
print("="*10+" Seja bem Vindo! "+"="*10)
print("_Tente adivinhar o numero aleatório_")

#variaveis
numero_sorteado = random.randint(1,20) #pc escolhe
palpite = 0 #pessoa escolhe

#loop - enquanto o palpite for diferente do numero sorteado
while palpite != numero_sorteado: #enquanto TRUE (é diferente do numero sorteado)
    palpite = int(input("\nAdivinhe o número sorteado: ")) #qual o palpite?

    #conticionais se esta perto ou distante do numero sorteado
    if palpite < numero_sorteado:
        diferenca = numero_sorteado - palpite # diferença entre numero e palpite(se < 5 = proximo ao numero sorteado)
        if diferenca <= 5:
            print("Você errou mas... esta perto!")
        else:
            print("Você errou! Esta bem abaixo")
    elif palpite > numero_sorteado:
        diferenca = numero_sorteado - palpite
        if diferenca <= 5:
            print("Voce errou mas, esta perto!")
        else:
            print("Você errou! Esta muito acima")
    else:
        print(f"Você acertou! O numero sorteado foi: {{}}".format(numero_sorteado))
    """


###### - Jogo Intermediário - Com tratamento de Exceções e Validação de Regras de Negócio

#função - maquininha 

def jogar_adivinhacao():
    print(f"\n{'-'*10} Bem-vindo ao Game! {'-'*10}")

    #criar o ambiente
    num_min = 1
    num_max = 20
    num_sorteado = random.randint(num_min, num_max)
    acertou = False # para encerrar a função! Caso erre, sera TRUE e o programa continua

    while not acertou:
        entrada = input(f"\nAdivinhe o número ({num_min}-{num_max}): ").strip() #strip p/ remover espaços acidentais
        
        #1. Tratamento de Erro: Entrada Vazia
        if not entrada:
            print("⚠️ Erro: Você não digitou nada! == Tente novamente.")
            continue # Fail Fast - Se a entrada é inválida, não perco processamento tentando calcular o resto | Pulo imediato para o proximo ciclo
        try:
            palpite = int(entrada)

            #2. Validação de RN: Fora do range ou negativo
            if palpite < num_min or palpite > num_max:
                print(f"🚫 Entrada inválida! Digite apenas números entre == {NUMERO_MIN} e {NUMERO_MAX} ==.")
                continue

            #3. Logica de comparação
            if palpite == num_sorteado:
                print(f"\t🎉 PARABÉNS! O número aleatório era: {num_sorteado}")
                acertou = True
            else:
                # Calculo de proximidade
                   
                distancia = abs(num_sorteado-palpite) #modulo de x = |x| == distancia: abs(10 - 15) # Resultado: 5 (em vez de -5)
                feedbak = "perto" if distancia <= 5 else "longe" # Padrão TERNÁRIO == Se a distância for <= 5, feedback recebe "perto", senão recebe "longe"
                feedback = "perto" if distancia <= 5 else "longe"
                direcao = "maior" if palpite < num_sorteado else "menor"

                print(f"Você errou! Está {feedbak}. Dica: o número aleatório é {direcao}.")
        
        except ValueError: # Evitar do Python mostrar um erro vermelho assustador!!
            #4. Tratamento de Erro: string no lugar de int
            print(f"Erro: Por favor, digite apenas números inteiros!")

if __name__ == "__main__":
    jogar_adivinhacao()
