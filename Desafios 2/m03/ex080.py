print('\033[32;1mDESAFIO 80 - Lista Ordenada sem Repetição\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)
# ---------------------------------

lista = []
for c in range(0, 5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao Final da Lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na Posição {pos} da Lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em Ordem foram: {lista}')
