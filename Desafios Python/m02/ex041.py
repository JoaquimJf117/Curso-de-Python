# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 041 - Classificando Atletas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
from datetime import date
# -----------------------------------------------------------------------
print(f'{"Confederação Nacional de Natação":^25}')


def ClassificandoAtleta():
    atleta = int(input('Ano de Nascimento: '))
    today = date.today().year
    idade = today - atleta
    print(f'O Atleta tem {idade} anos')
    if idade <= 9:
        print('Classificação: MIRIM')
    elif 9 < idade <= 14:
        print('Classificação: INFANTIL')
    elif 14 < idade <= 19:
        print('Classificação: JUNIOR')
    elif 19 < idade <= 25:
        print('Classificação: SÊNIOR')
    else:
        print('Classificação: MASTER')
# -----------------------------------------------------------------------


# Programa Principal
ClassificandoAtleta()
