strings = ['mamão', 'maçã', 'peixe', 'pepino']


def contar_substrings():
    n = int(input("Insiria o comprimento de chave desejado: "))
    stringsFinais = {}
    for lista in strings:
        for i in range(len(lista)-n+1):
            substring = lista[i:i+n]
            if substring in stringsFinais:
                stringsFinais[substring] += 1
            else:
                stringsFinais[substring] = 1
    print(stringsFinais)


contar_substrings()
