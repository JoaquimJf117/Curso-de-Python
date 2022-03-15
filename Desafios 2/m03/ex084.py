print('\033[32;1mDESAFIO 84 - Lista Composta de Análise de Dados\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
dados = list()
galera = []
mai = men = 0
# -----------------------------------------------------------------------
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer Continuar?[S/N] '))
    if resp in 'Nn':
        break
print('-'*50)
print(f'Ao todo, Você Cadastrou {len(galera)} Pessoas.')
print(f'O Maior Peso foi de {mai}Kg. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O Menor Peso foi de {men}Kg. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
