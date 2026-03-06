
# objetivo é criar uma lista de supermercado e realizar algumas operações de manipulação de listas, como adicionar, remover, contar itens, ordenar e inverter a ordem da lista.
"""
    1. Criar uma lista de supermercado com alguns itens.
    2. Adicionar um item à lista usando o método append().
    3. Criar uma nova lista de compras e adicionar itens a ela.
    4. Remover um item da lista usando o método remove().
    5. Contar quantos itens tem na lista usando a função len().
    6. Contar quantas vezes um item aparece na lista usando o método count().
    8. Inverter a ordem da lista usando o método reverse().
    10. Imprimir a lista em cada etapa para mostrar as mudanças.
    12. Certificar-se de que o código seja claro e fácil de entender.
    13. Salvar o arquivo e executar o código para ver os resultados.
"""

#Criando uma lista de supermercado
print("\nCriando uma lista de supermercado")
print("=" * 30 + "\n")
lista_supermercado=[]
valor_item_lista=[]
resposta="S" #variável para controlar o loop de entrada de itens

#Adicionando itens à lista de supermercado
while resposta.upper() == "S":
    item = input("Insira um item na lista de supermercado: ")
    lista_supermercado.append(item)
    
    valor_item=float(input("Insira o valor do item: "))
    valor_item_lista.append(valor_item)
    
    resposta = input("Deseja adicionar outro item? (S/N): ")

"""
  ##  Adicionar função para remover item da lista_supermercado ##

"""

#Saida
print("\nLista de supermercado criada: ")
print(", ".join(lista_supermercado)) #join para imprimir os itens da lista separados por vírgula
print("\nValores dos itens na lista:")
print(valor_item_lista)
print("\nQuantidade de itens na lista de supermercado: ")
print(len(lista_supermercado))


