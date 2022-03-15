print('\033[32;1mDESAFIO 59 - Analise de Dados em uma Tuplas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite último número: ')))
print(f'Você digitou os Valores: {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3)+1}ª Posição')
else:
    print('O Valor 3 não foi Digitado em nenhuma Posição')
print(f'Os Valores Pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
