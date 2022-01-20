print('\033[32;1mDESAFIO 6 - Dobro, Triplo e Raiz Quadrada\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
valor = int(input('Digite um Número: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print(f'O Dobro de {valor} vale {dobro}.')
print(f'O Triplo de {valor} vale {triplo}')
print(f'A Raiz Quadrada de {valor} vale {raiz:.2f}.')
