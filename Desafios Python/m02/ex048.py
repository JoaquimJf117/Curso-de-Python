# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 048 - Soma Ímpares múltiplos de 3\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def ContadorImpares3():
    soma = 0
    cont = 0
    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
            cont += 1
    print(f'A Soma de todos os {cont} valores solicitados é {soma}')
# -----------------------------------------------------------------------


# Programa Principal
ContadorImpares3()
