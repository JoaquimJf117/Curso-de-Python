# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 050 - Soma dos Pares\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def SomaPar():
    soma= cont = 0
    for n in range(1, 7):
        n = int(input(f'Digite o {n}º número: '))
        if n % 2 == 0:
            soma += n
            cont += 1
    print(f'Recebemos {cont} Pares e a sua soma foi {soma}')
# -----------------------------------------------------------------------


# Programa Principal
SomaPar()
