# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 046 - Contagem Regressiva\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
import time
# -----------------------------------------------------------------------


def Contador():
    for c in range(10, -1, -1):
        time.sleep(1)
        print(c)
    print('Finalizamos a Contagem!')


# -----------------------------------------------------------------------


# Programa Principal
Contador()
