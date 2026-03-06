"""
•	Antecessor e sucessor (Ex. 5) → brincar com números vizinhos.
•	Dobro, triplo e raiz quadrada (Ex. 6) → explorar transformações numéricas.
•	Média aritmética (Ex. 7) → calcular notas.
•	Conversor de medidas (Ex. 8) → transformar metros em centímetros, etc.
•	Tabuada (Ex. 9) → automatizar cálculos repetitivos.
•	Conversor de moedas (Ex. 10) → simular câmbio.
•	Pintando parede (Ex. 11) → calcular área e tinta necessária.
•	Descontos (Ex. 12) → aplicar porcentagens.
•	Reajuste salarial (Ex. 13) → calcular aumento.
•	Conversor de temperaturas (Ex. 14) → Celsius ↔ Fahrenheit.
•	Aluguel de carros (Ex. 15) → calcular custo por dias e km rodados.
"""

# Ex. 5 - Antecessor e Sucessor
num = int(input("\nDigite um numero: "))
print(f"\nO antecessor do {num} é: \t[{num-1}] e o seu sucessor é [{num+1}]!")

# Ex. 6 - Dobro, Triplo e Raiz Quadrada
num = int(input("\nDigite um numero: "))
print(f"\nO dobro de {num} é: \t[{num*2}], o triplo é: [{num*3}], e a raiz quadrada é: [{num**(1/2):.2f}]!")

# Ex. 7 - Média Aritmética
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"\n A média entre {n1} e {n2} é: [{media:.2f}]")


# Ex. 8 - Conversor de Medidas
metros = float(input("\nDigite a medida em metros: ")) #metro para cm, mm *100, *1000 / metro p/ km, hm, dam / 1000,100,10
km= metros / 1000
hm = metros / 100
dam = metros / 10
cm = metros * 100
mm = metros * 1000
print(f"\n{metros} metros equivalem a: \n{km} km \n{hm} hm \n{dam} dam \n{cm} cm \n{mm} mm")

# Ex. 9 - Tabuada
num =int(input("\nDigite um numero para ver sua tabuada: ")) #uso for para criar a tabuada de 1 a 10
print(f'\nTabuada do {num}:')
for i in range(1,11): #range(1,11) gera uma sequência de números de 1 a 10 (o 11 é exclusivo)
        print(f"{num:.2f} x {i} = {num*i}")

#10 - Conversor de Moedas
real = float(input("\nDigite o valor em reais: "))
dolar = real / 5.25 #considerando a cotação do dólar a R$5,25
print(f"\nR$ {real:.2f} equivalem a US$ {dolar:.2f}")

# Ex. 11 - Pintando Parede
largura = float(input("\nDigite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta = area /2 #considerando que 1 litro de tinta cobre 2 metros quadrados
print(f"\nA área da parede é: {area:.2f} m² e você precisará de {tinta:.2f} litros de tinta para pintá-la.")
#print(f"\nA área da parede é: {{}} m2 e você precisará de {{}} litros de tinta para pintá-la.".format(area, tinta))

# Ex. 12 - Descontos
preco = float(input("\nDigite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
desconto_valor = preco * (desconto / 100)
preco_final = preco - desconto_valor
print(f"\n O preço final do produto com {desconto} % de desconto é: R$ {preco_final:.2f}")

# Ex. 13 - Reajuste Salarial
salario = float(input("\nDigite o salário atual: "))
aumento = float(input("Digite o percentual de aumento: "))
aumento_valor = salario * (aumento / 100)
salario_final = salario + aumento_valor
print(f"\nO salário final com {{}} % de aumento é: R$ {{}}: ".format(aumento, salario_final))

# Ex. 14 - Conversor de Temperaturas
# Celsius para Fahrenheit: F = (C * 9/5) + 32
# Celsius para Kelvin: K = C + 273.15  
# Fahrenheit para Celsius: C = (F - 32) * 5/9
# Fahrenheit para Kelvin: K = (F - 32) * 5/9 + 273.15
# Kelvin para Celsius: C = K - 273.15
# Kelvin para Fahrenheit: F = (K - 273.15) * 9/5 + 32
temp_c = float(input("\nDigite a temperatura em Celsius: "))
temp_f = (temp_c * 9/5) + 32
temp_k = temp_c + 273.15
#print(f"\n A temperatura de {temp_c} ºC equivale a: \n{temp_f} ºF \n{temp_k} ºK")
print(f'\nA temperatura de {{}} ºC equivale a: \n{{}} ºF \n{{}} ºK'.format(temp_c, temp_f, temp_k))

# Ex. 15 - Aluguel de Carros
dias = int(input("\nDigite o número de dias de aluguel: "))
km = float(input("Digite a quantidade de km rodados: "))
custo_dias = dias * 60 #considerando R$60 por dia
custo_km = km * 0.15 #considerando R$0,15 por km
custo_total = custo_dias + custo_km
print(f"\nO custo total do aluguel é: R$ {custo_total:.2f} \n- Custo por dias: R$ {custo_dias:.2f} \n- Custo por km: R$ {custo_km:.2f}")