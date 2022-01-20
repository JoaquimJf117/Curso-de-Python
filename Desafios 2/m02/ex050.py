print('\033[32;1mDESAFIO 50 - Soma dos Pares\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
cont = soma = 0
for c in range(1, 7):
    num = int(input(f'Digite {c}º Valor: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'\033[34;1mVocê Informou {cont} Números PARES e a Soma foi {soma}\033[m')
