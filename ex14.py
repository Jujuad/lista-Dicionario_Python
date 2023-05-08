alunos = {'Julia': [8, 9, 10], 'Marcela': [10, 6, 8], 'Joana': [7, 5, 7]}


def media_aluno():
    nome = input("Insira o nome do aluno: ").title()
    lista = alunos[nome]
    media = (lista[0] + lista[1] + lista[2])/3
    print(media)


media_aluno()
