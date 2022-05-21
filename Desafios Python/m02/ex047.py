# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 047 - Contagem dos Pares\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def Contador():
    for n in range(1, 51):
        if n % 2 == 0:
            print(n, end=' ')
    print('Acabou!')
# -----------------------------------------------------------------------


# Programa Principal
Contador()
