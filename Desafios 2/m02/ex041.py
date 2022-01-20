print('\033[32;1mDESAFIO 41 - Classificando Atletas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
from datetime import date
atual = date.today().year
nasc = int(input('Ano Nascimento: '))
idade = atual - nasc
print(f'O Atleta têm {idade} anos')
#  Classificando
if idade <= 9:
    print('\033[32;1mClassificação: MIRIM\033[m')
elif idade <= 14:
    print('\033[32;1mClassificação: INFANTIL\033[m')
elif idade <= 19:
    print('\033[32;1mClassificação: JUNIOR\033[m')
elif idade <= 25:
    print('\033[32;1mClassificação: SÊNIOR\033[m')
else:
    print('\033[32;1mClassificação: MASTER\033[m')
