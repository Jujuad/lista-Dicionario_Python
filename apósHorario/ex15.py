dic = {"banana": 3, "abacaxi": 1, "maçã": 2}

lista_tuplas = []


def ordenar_por_valor():
    dic_ordenado = dict(
        sorted(dic.items(), key=lambda item: item[1], reverse=True))
    for index, lista in dic_ordenado.items():
        tupla = (index, lista)
        lista_tuplas.append(tupla)
