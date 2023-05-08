list = [1, 4, 7, 7, 7, 3, 4, 3]


def contar_elementos():
    dic = {}
    for lista in list:
        if lista in dic:
            dic[lista] += 1
        else:
            dic[lista] = 1
    print(dic)


contar_elementos()
