print('\033[32;1mDESAFIO 48 - Soma Ímpares Multiplos de Três\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A Soma de todos os {cont} Valores Solicidados é {soma}')
