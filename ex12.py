palavras = {'como': 1, 'para': 2, 'porque': 3, 'talvez': 4, 'sempre': 6}
cont = 0
aux = []
maiores = []
n = int(input("Insiria a quantidade de palavras com maior numero de repeticao que voce deseja: "))

if (n > 5):
    print("Existem 5 palavras")

elif (n < 0):
    print("Erro!")

else:
    for index, lista in palavras.items():
        aux.append(index)
    while (cont < n):
        m = max(aux)
        maiores.append(m)
        aux.remove(m)
        cont = cont + 1
    print(maiores)
