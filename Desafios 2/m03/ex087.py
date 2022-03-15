print('\033[32;1mDESAFIO 87 - Matriz em Python[Part #2]\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
# -----------------------------------------------------------------------
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-'*50)
print(f'A Soma dos Valores Pares é: {spar}!')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A Soma dos Valores da Terceira Coluna é: {scol}!')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O Maior Valor da Segunda Linha é: {mai}!')
