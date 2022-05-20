# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 030 - Par ou Ímpar\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
tipo = ['Par', 'Ímpar']
num = int(input('Digite um número Qualquer: '))

if num % 2 == 0:
    print(f'O número {num} é {tipo[0]}')
else:
    print(f'O número {num} é {tipo[1]}')
# -----------------------------------------------------------------------
