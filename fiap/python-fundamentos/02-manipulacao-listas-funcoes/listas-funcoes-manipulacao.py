#Inventario
print("Inventário de Supermercado")
inventario = ['arroz', 'feijao', 'macarrao', 'carne', 'leite']
print("\n")


#Adicionar um item
print("Adicionando um item...")
inventario.append('cafe')
print(inventario)
print("\n")

#Inserir um item em uma posição específica
print("Inserindo um item na posição 2...")
inventario.insert(2, 'açucar')
print(inventario)
print("\n")

#Adicionar item a uma lista vazia
print("Criando uma nova lista de compras...")
lista_compras = []
print("Adicionando itens à lista de compras...")
lista_compras.append('pao')
lista_compras.append('manteiga')
print(lista_compras)
print("\n")

#Remover um item
print("Removendo um item...")
inventario.remove('carne')
print(inventario)   
print("\n")

#Contar quantos itens tem na lista
print("Quantidade de itens no inventário:")
print(len(inventario))
print("\n")

#Contar quantas vezes um item aparece na lista
print("Quantas vezes 'arroz' aparece no inventário:")
print(inventario.count('arroz'))
print("\n")

#Ordenar a lista
print("Ordenando a lista...")
inventario.sort()
print(inventario)   
print("\n")

#Inverter a ordem da lista
print("Invertendo a ordem da lista...")
inventario.reverse()
print(inventario)

