print('\033[32;1mDESAFIO 96 - Função que Calcula Área\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)


# -----------------------------------------------------------------------


def area(larg, comp):
    a = larg * comp
    print(f'A área de um Terreno {larg}x{comp} é de {a}m.')


# -----------------------------------------------------------------------
# Programa Principal
print('     Controle de Terreno')
print('-' * 30)
l = float(input('LARGURA [m]: '))
c = float(input('COMPRIMENTO [m]: '))
area(l, c)
