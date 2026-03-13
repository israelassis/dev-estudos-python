import math #importar todo modulo math
# <from math import sqrt, ceil> == importado apenas sqrt e ceil de math
import random



print("="*30)
print("Exercícios de Fixação do Curso em Vídeo" + "\nPython Mundo 01")
print("="*30 + "\n")

print("Antecesor e Sucessor de um Número! ")
num = random.randint(1,100) # numeros aleatroios entre 1 e 100
print(f"Numero escolhido: {{}}".format(num))
print(f"\tO antecessor do {num} é: {num-1} e o seu sucessor é {num+1}!")


print("\nDobro, Triplo e Raiz Quadrada de um Número! ")
#  n = math.sqrt(num)  === usando o modulo math
num = random.randint(1,100)
print(f"Numero escolhido: {{}}".format(num))
raiz=math.sqrt(num)
dobro=num*2
triplo=num*3
print(f"\tO dobro é: {{:.2f}}, o triplo é: {{:.2f}} e a raiz quadrada é: {{:.2f}}".format(dobro, triplo, raiz))


print("\nMédia Aritmética de um Número! ")
n1= random.randint(1,10)
n2= random.randint(1,10)
n3= random.randint(1,10)
media = (n1 + n2 + n3) / 3
print(f"1º Nota: {n1:.2f} + 2º Nota: {n2:.2f} + 3º Nota: {n3:.2f} ")
print(f"\tA média entre as 3 notas é: {media:.2f}")


print("\nConversor de Medidas")
num = random.randint(1,100) #metro para cm, mm *100, *1000 / metro p/ km, hm, dam / 1000,100,10
print(f"Convertendo {num} para:")
km= num / 1000
hm = num / 100
dam = num / 10
cm = num * 100
mm = num * 1000
print(f"\t{num} metros equivalem a: \n{km} km \n{hm} hm \n{dam} dam \n{cm} cm \n{mm} mm")


print("\nTabuada de um Número! ")
num = random.randint(1,100) #uso for para criar a tabuada de 1 a 10
print(f'\tTabuada do {num}:')
for i in range(1,11): #range(1,11) gera uma sequência de números de 1 a 10 (o 11 é exclusivo)
        print(f"{num:.2f} x {i} = {num*i}")


print("\nConversor de Moedas")
num = random.randint(1,100)
print(f"Converter {num} para Dolar")
dolar = num / 5.25 #considerando a cotação do dólar a R$5,25
print(f"\tR$ {num:.2f} reais, equivalem a US$ {dolar:.2f} dolares")


print("\nPintando Parede")
largura = random.randint(1,100)
altura = random.randint(1,100)
print(f"Largura: {largura} e Altura: {altura}")
area = largura * altura
tinta = area /2 #considerando que 1 litro de tinta cobre 2 metros quadrados
print(f"\tA área da parede é: {area:.2f} m² e você precisará de {tinta:.2f} litros de tinta para pintá-la.")
#print(f"\nA área da parede é: {{}} m2 e você precisará de {{}} litros de tinta para pintá-la.".format(area, tinta))


print("\nDescontos")
preco = random.randint(1,100)
desconto = random.randint(1,100)
desconto_valor = preco * (desconto / 100)
preco_final = preco - desconto_valor
print(f"Preço original R$: {preco} + Desconto de {desconto}")
print(f"\tO preço final do produto com {desconto} % de desconto é: R$ {preco_final:.2f}")


print("\nReajuste Salarial")
salario = random.randint(1,100)
aumento = random.randint(1,100)
aumento_valor = salario * (aumento / 100)
salario_final = salario + aumento_valor
print(f"Salario Inicial R$: {salario} + Aumento de {aumento}%")
print(f"\tO salário final com {{}} % de aumento é: R$ {{}}:, e o salario reajustado é R$ {{}} reais ".format(aumento, aumento_valor, salario_final))


# Ex. 14 - Conversor de Temperaturas
# Celsius para Fahrenheit: F = (C * 9/5) + 32
# Celsius para Kelvin: K = C + 273.15  
# Fahrenheit para Celsius: C = (F - 32) * 5/9
# Fahrenheit para Kelvin: K = (F - 32) * 5/9 + 273.15
# Kelvin para Celsius: C = K - 273.15
# Kelvin para Fahrenheit: F = (K - 273.15) * 9/5 + 32
print("\nConversor de Temperatura")
temp_c = random.randint(1,100)
temp_f = (temp_c * 9/5) + 32
temp_k = temp_c + 273.15
#print(f"\n A temperatura de {temp_c} ºC equivale a: \n{temp_f} ºF \n{temp_k} ºK")
print(f'\tA temperatura de {{}} ºC equivale a: \n{{}} ºF \n{{}} ºK'.format(temp_c, temp_f, temp_k))


print("\nAluguel de Carros")
dias = random.randint(1,100)
km = random.randint(1,100)
custo_dias = dias * 60 #considerando R$60 por dia
custo_km = km * 0.15 #considerando R$0,15 por km
custo_total = custo_dias + custo_km
print(f"Alugando um carro por {dias} dias e rodar por {km} KM:")
print(f"\tO custo total do aluguel é: R$ {custo_total:.2f} \n- Custo por dias: R$ {custo_dias:.2f} \n- Custo por km: R$ {custo_km:.2f}")


print("\nTrazer a parte inteira de um Número: ")
num = random.uniform(1,10) #retorna random float
print(f"\nA porção inteira do numero: {{:.2f}} é:  {{}}".format(num, math.trunc(num)))



print("Calcular a hipotenusa de um triangulo retangulo")
cat_oposto = random.randint(1,100)
cat_adjacente = random.randint(1,100)
# hipotenusa = math.sqrt(cat_oposto ** 2 + cat_adjacente ** 2)
hipotenusa = math.hypot(cat_oposto, cat_adjacente) # praticidade do modulo
print(f"\nCateto Oposto: {{:.2f}} e Cateto Adjacente é: {{:.2f}}".format(cat_oposto, cat_adjacente))
print(f"\tA hipotenusa vai medir {{:.2f}}".format(hipotenusa))


print("Calculo de Ângulos:")
angulo = random.randint(1,100)
sen = math.sin(math.radians(angulo)) # converte para radianos, depois converte para Seno
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"\nAngulo de {{:.2f}}. \nPossui: SEN = {{:.2f}} | COS = {{:.2f}} | TAN = {{:.2f}}".format(angulo,sen,cos,tan))


print("Sorteio de Nomes")
nome1 = str(input("Digite o 1º nome: "))
nome2 = str(input("Digite o 2º nome: "))
nome3 = str(input("Digite o 3º nome: "))
nome4 = str(input("Digite o 4º nome: "))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f"\nO nomes do sorteio são: {{}} | {{}} | {{}} | {{}}".format(nome1, nome2, nome3, nome4))
print(f"\nVamos embaralhar as opções: {{}} ".format(lista, random.shuffle(lista))) # shuffle = embaralhar
print(f"\tO nome escolhido no sorteio foi === {{}}. \nP.A.R.A.B.E.N.S  {{}}!".format(escolhido,escolhido.upper()))



print("\n== Final ==")
