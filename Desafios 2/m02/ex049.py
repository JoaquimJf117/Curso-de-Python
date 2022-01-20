print('\033[32;1mDESAFIO 49 - Tabuada V.2.0\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
num = int(input('Digite um número para ver sua Tabuada: '))
for c in range(1, 13):
    print(f'\033[32;1m{num} X {c:2} = {num*c}\033[m')
