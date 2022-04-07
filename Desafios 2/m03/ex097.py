print('\033[32;1mDESAFIO 97 - Print Especial\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa Principal
escreva('Joaquim Fernandes')
escreva('Curso de Python no Youtube')
escreva('CeV')
