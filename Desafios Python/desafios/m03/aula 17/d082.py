print('='*15, '\033[1;32mDESAFIO 81\033[m', '='*15)
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-='*30)
print(f'A Lista Completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A Lista de Ímpares é {ímpares}')
