print('='*15, '\033[1;32mDESAFIO 81\033[m', '='*15)
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer Continuar?[S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'OS valores digitados em Ordem Decrecente são {valores}')
if 5 in valores:
    print('O Valor 5 faz parte da Lista!')
else:
    print('O valor 5 não foi Encontrado na Lista!')
