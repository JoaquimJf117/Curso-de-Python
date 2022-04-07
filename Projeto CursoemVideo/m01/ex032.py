print('\033[32;1mDESAFIO 32 - Ano Bissexto\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
from datetime import date
ano = int(input('Que Ano quer Analisar? 0 para Analisar o Ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é BISSEXTO')
else:
    print(f'O Ano {ano} não é BISSEXTO')
