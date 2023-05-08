dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'b': 4, 'a': 5, 'f': 6}

lista_dic = [dic1, dic2]


def combinar_dicionarios():
    dic_final = {}
    for dic in lista_dic:
        for index, lista in dic.items():
            if index in dic_final:
                dic_final[index] += lista
            else:
                dic_final[index] = lista
    print(dic_final)


combinar_dicionarios()
