print('\033[32;1mDESAFIO 99 - Função que Descobre Maior\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
# print('-' * 50)
from time import sleep


def maior(*num):
    cont = major = 0
    print('-' * 50)
    print('Analisando os Valores Passados....')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            major = valor
        else:
            if valor > major:
                major = valor
        cont += 1
    print(f'Foram Informados {cont} Valores ao Todo.')
    print(f'O maior Valor Informado foi {major}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
