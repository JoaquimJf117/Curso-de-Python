print('\033[32;1mDESAFIO 78 - Maior Menor Valores em Listas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)
valores = list()
mai = men = 0
# ---------------------------------
for c in range(0, 5):
    valores.append(int(input(f'Digite um Valor para a Posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('-'*60)
print(f'Você Digitou os Valores {valores}')
print(f'O Maior Valor Digitado foi {mai} nas Posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O Menor Valor Digitado foi {men} nas Posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
