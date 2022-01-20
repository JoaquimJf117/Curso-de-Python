print('\033[32;1mDESAFIO 38 - Comparando Números\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))
if num1 > num2:
    print('\033[36;1mO PRIMEIRO\033[m valor é \033[36;1mMAIOR\033[m')
elif num2 > num1:
    print('\033[36;1mO SEGUNDO\033[m valor é \033[36;1mMAIOR\033[m')
else:
    print('\033[36;1mOS DOIS\033[m valor são \033[36;1mIGUAIS\033[m')
