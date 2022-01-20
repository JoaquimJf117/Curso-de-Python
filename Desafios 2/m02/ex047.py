print('\033[32;1mDESAFIO 47 - Contagem de Pares\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 70)
#   for c in range(2, 51, 2):
for c in range(1, 51):
    if c % 2 == 0:
        print(f'\033[31;1m{c}\033[m', end=' ')
print('\033[32;1mACABOU!\033[m')
