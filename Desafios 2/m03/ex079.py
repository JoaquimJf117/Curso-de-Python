print('\033[32;1mDESAFIO 79 - Valores Únicos em uma Lista\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)
# ---------------------------------
numeros = list()

while True:
    n = (int(input('Digite um Valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com Sucesso...')
    elif n in numeros:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer Continuar?[S/N] '))
    if r in 'Nn':
        break
print('-'*35)
numeros.sort()
print(f'Você Digitou os Seguintes Valores {numeros}')
