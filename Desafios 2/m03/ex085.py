print('\033[32;1mDESAFIO 85 - Lista Composta de Análise de Dados\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
valores = [[], []]
valor = 0
# -----------------------------------------------------------------------
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º Valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
    valores.append(valor)
print('-'*50)
valores[0].sort()
valores[1].sort()
print(f'Os Valores Pares Digitados Foram: {valores[0]}')
print(f'Os Valores Ímpares Digitados Foram: {valores[1]}')
