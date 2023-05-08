dic = {1: 'teste1', 2: 'teste2', 3: 'teste3', 4: 'teste4'}
dic2 = {1: 'teste11', 2: 'teste2', 3: 'teste3', 4: 'teste14'}

listaIgual = []


def encontrar_valores_comuns():
    for index, lista in dic.items():
        for index2, lista2 in dic2.items():
            if lista == lista2:
                listaIgual.append(index)
    print(listaIgual)


encontrar_valores_comuns()
