print('\033[32;1mDESAFIO 52 - Números Primos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
num = int(input('Digite um Número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33;1m', end='')
        tot += 1
    else:
        print('\033[31;1m', end='')
    print(f'{c} ', end=' ')
print(f'\033[m\nO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
