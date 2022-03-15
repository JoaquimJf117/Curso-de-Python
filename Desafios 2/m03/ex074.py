print('\033[32;1mDESAFIO 59 - Maior e Menor Valores eom Tuplas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)
from random import randint

sort = (randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))
print(f'Os Valores Sorteados foram: ', end='')
for n in sort:
    print(f'{n} ', end='')
print(f'\nO Maior Valor Sorteado Foi: {max(sort)}')
print(f'O Menor Valor Sorteado Foi: {min(sort)}')
