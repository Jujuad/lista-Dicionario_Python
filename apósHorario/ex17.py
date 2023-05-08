# Exemplo de tentatativa, pois não consegui gerar o resultado certo nem com pesquisa.


dic = {'a': 7, 'b': {'c': 20, 'd': {'e': 8}}}


def dicionario_profundo(divisor='_', chave1=''):
    dic_final = {}
    for index, lista in dic.items():
        chave_atual = index if not chave1 else f"{chave1}{divisor}{index}"
        if isinstance(lista, dict):
            dic_final.update(dic_final(lista, divisor, chave_atual))
        else:
            dic_final[chave_atual] = lista
    print(dic_final)


dicionario_profundo()
