frutas = {'maça': 5, 'banana': 8, 'laranja': 12}

frutas_mais_de_5 = []

for index, lista in frutas.items():
    if lista > 5:
        frutas_mais_de_5.append(index)
print(frutas_mais_de_5)
