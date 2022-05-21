# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 049 - Tabuada[v2.0]\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
print(f'{"Consultar Tabuada":^50}')


def Tabuada():
    numero = int(input('Digite um Número: '))
    for tab in range(1, 13):
        print(f'{numero} x {tab:2} = {numero*tab}')
# -----------------------------------------------------------------------


# Programa Principal
Tabuada()
