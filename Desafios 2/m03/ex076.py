print('\033[32;1mDESAFIO 76 - Lista de Preço com Tuplas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)

listagem = ('Lápis', 1.75,
            'Borracha', 3,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 8.20,
            'Compasso', 10.99,
            'Mochila', 120.32,
            'Canetas', 12.30,
            'Livro', 34.90)
print('-'*40)
print(f'\033[1;36m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
