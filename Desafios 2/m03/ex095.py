print('\033[32;1mDESAFIO 95 - Cadastro de Jogador de Futebol [V2]\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
time = list()
jogador = dict()
partidas = list()
# -----------------------------------------------------------------------
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas {jogador["Nome"]} Jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos Gols na Partida {c}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('[ERRO!] Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar Dados de Qual Jogador [999 para Parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'[ERRO!] Não existe Jogador com Código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} Gols.')
    print('-'*40)
print('<<< Volte Sempre >>>')
