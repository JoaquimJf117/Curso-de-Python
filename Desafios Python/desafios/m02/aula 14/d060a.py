print('=' * 15, '\033[1;32mDESAFIO 60\033[m', '=' * 15)
n = int(input('Digite um número para Calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}!= '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))
