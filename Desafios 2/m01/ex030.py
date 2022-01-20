print('\033[32;1mDESAFIO 30 - Par ou Ímpar\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
num = int(input('Me Diga um Número Qualquer: '))
if num % 2 == 0:
    print(f'O Número {num} é \033[34;1mPAR\033[m')
else:
    print(f'O Número {num} é \033[34;1mÍMPAR\033[m')
