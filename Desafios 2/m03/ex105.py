print('\033[32;1mDESAFIO 105 - Analisando e Gerando Dicionários\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)


def notas(*n, sit=False):
    """
    -> função para analisar Notas e Situações de vários Alunos
    :param n: uma ou mais Notas dos Alunos (Aceita Várias)
    :param sit: Valor Opcional, indicando se deve ou não adicionar a situação
    :return: dicionário sobre várias informações sobre a situação da turma
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa Principal
resp = notas(5.5, 2.5, 5, 6, sit=True)
print(resp)
help(notas)
