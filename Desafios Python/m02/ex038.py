# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 030 - Comparando Valores Inteiros\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def CompararValores():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    if num1 < num2:
        print('O SEGUNDO valor é MAIOR!')
    elif num1 > num2:
        print('O PRIMEIRO Valor é MAIOR')
    else:
        print('NENHUM valor é MAIOR ambos são IGUAIS!')
# -----------------------------------------------------------------------


# Programa Principal
CompararValores()
