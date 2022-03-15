print('\033[32;1mDESAFIO 81 - Extraíndo Dados de Uma Lista\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# ----------------------------------------------------------------
listnum = []
while True:
    listnum.append(int(input('Digite um Valor: ')))
    r = str(input('Quer Continuar?[S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(listnum)} Elementos.')
listnum.sort(reverse=True)
print(f'Os Valores em Ordem Decrescente são {listnum}')
if 5 in listnum:
    print('O Valor 5 faz parte da Lista!')
else:
    print('\033[1;31mO Valor 5 não Foi Encontrado na Lista!\033[m')
