print('\033[32;1mDESAFIO 33 - Maior e Menor Valor\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))
v3 = int(input('Terceiro Valor: '))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O Menor Valor Digitado foi {menor}')
print(f'O Maior Valor Digitado foi {maior}')
