dic = {'a': [14, 2], 'b': [4, 5, 8], 'c': [6, 7, 9], 'd': [10, 2, 1]}


def filtrar_dicionario():
    limite = int(input("Insiria o limite desejado: "))
    dic_final = {}
    for index, lista in dic.items():
        soma = sum(lista)
        if soma > limite:
            dic_final[index] = lista
    print(dic_final)


filtrar_dicionario()
