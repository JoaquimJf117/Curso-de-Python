# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 037 - Conversor de Bases Numéricas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def BasesConversor():
    numero = int(input('Digite um número Inteiro: '))
    print('''Escolha uma das Bases para Conversão:
    [ 1 ]Converter para BINÁRIO
    [ 2 ]Converter para OCTAL
    [ 3 ]Converter para HEXADECIMAL''')
    opção = int(input('Faça a sua Escolha: '))
    if opção == 1:
        print(f'{numero} convertido para BINÁRIO é = \033[1;34m{bin(numero)[2:]}\033[m')
    elif opção == 2:
        print(f'{numero} convertido para OCTAL é = \033[1;34m{oct(numero)[2:]}\033[m')
    elif opção == 3:
        print(f'{numero} convertido para HEXADECIMAL é = \033[1;34m{hex(numero)[2:]}\033[m')
    else:
        print('Opção Inválida. Tente novamente!')
# -----------------------------------------------------------------------


# Programa Principal
BasesConversor()
