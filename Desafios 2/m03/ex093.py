print('\033[32;1mDESAFIO 93 - Cadastro de Jogador de Futebol\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
jogador = dict()
partidas = list()
# -----------------------------------------------------------------------
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas Partidas {jogador["Nome"]} Jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos Gols na Partida {c+1}: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-'*50)
print(jogador)
print('='*50)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*25)
print(f'O Jogador {jogador["Nome"]} Jogou {len(jogador["Gols"])} Partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    => E na Partida {i}, Ele fez {v} Gols')
print(f'Foi um Total de: {jogador["Total"]} Gols')
