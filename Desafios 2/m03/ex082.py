print('\033[32;1mDESAFIO 82 - Dividindo Valores em Várias Listas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------

listnum = list()
pares = list()
impares = list()
while True:
    listnum.append(int(input('Digite um Número: ')))
    r = str(input('QUer Continuar?[S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(listnum):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista Completa é {listnum}')
print(f'A lista de Pares é {pares}')
print(f'A lista de Ímpares é {impares}')
