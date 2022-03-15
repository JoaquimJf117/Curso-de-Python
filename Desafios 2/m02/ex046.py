print('\033[32;1mDESAFIO 46 - Contagem Regressiva\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('\033[32;1mBUM! BUM! BUM! POWWOW!\033[m')
