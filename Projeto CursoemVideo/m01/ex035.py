print('\033[32;1mDESAFIO 35 - Analisando Triângulos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-=' * 20)
print(' \033[34;1mANALISADOR DE TRIÂNGULO\033[m')
print('-=' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS Segmentos acima \033[33;1mPODEM FORMAR\033[m um Triângulo!')
else:
    print('OS Segmentos acima \033[31;1mNÃO PODEM FORMAR\033[m um Triângulo!')
