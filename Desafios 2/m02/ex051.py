print('\033[32;1mDESAFIO 51 - Progressão Aritmética\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
print('         10 TERMOS DE UMA PA')
print('-'*40)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(f'{c} ', end='-> ')
print('ACABOU!')
