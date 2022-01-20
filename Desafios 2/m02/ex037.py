print('\033[32;1mDESAFIO 37 - Conversor de Bases Numéricas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
num = int(input('Digite um Número Inteiro: '))
print('''Escolha uma das Bases para Conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print(f'{num} Convertido para BINÁRIO é igual a \033[32m{bin(num)[2:]}\033[m')
elif opcao == 2:
    print(f'{num} Convertido para OCTAL é igual a \033[32m{oct(num)[2:]}\033[m')
elif opcao == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a \033[32m{hex(num)[2:]}\033[m')
else:
    print('OPÇÃO INVÁLIDA. Tente Novamente.')
