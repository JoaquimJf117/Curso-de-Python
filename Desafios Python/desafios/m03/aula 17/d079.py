print('='*15, '\033[1;32mDESAFIO 78\033[m', '='*15)
numeros = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com Sucesso...')
    else:
        print('Valor Duplicado! Não vou Adicionar...')
    r = str(input('Quer Continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você Digitou os Valores {numeros}')