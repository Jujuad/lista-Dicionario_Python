dic = {1: 'teste1', 2: 'teste2', 3: 'teste3', 1: 'teste1'}

listaInv = []


def inverter_chave_valor():
    inverter = {v: k for k, v in dic.items()}
    for index, lista in inverter.items():
        if lista == lista:
            listaInv.append(index)
    print(listaInv)


inverter_chave_valor()
