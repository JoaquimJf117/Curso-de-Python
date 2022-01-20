print('='*15, '\033[1;32mDESAFIO 80\033[m', '='*15)
lista = []
for c in range(0, 5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no Final da Lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na Posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os Valores Digitados em Ordem foram {lista}')
