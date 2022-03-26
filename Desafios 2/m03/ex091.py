print('\033[32;1mDESAFIO 91 - Jogando Dados\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
from random import randint
from time import sleep
from operator import itemgetter
# -----------------------------------------------------------------------
jogadores = {'jogador1': randint(0, 6),
             'jogador2': randint(0, 6),
             'jogador3': randint(0, 6),
             'jogador4': randint(0, 6)}
rank = list()
# -----------------------------------------------------------------------
print('-' * 15, 'Valores Sorteados', '-' * 15)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no Dado.')
    sleep(1)
print('-' * 50)
print('=' * 15, '\033[33mRANKING DOS JOGADORES\033[m', '=' * 15)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
# print(f'Vencedor: é o {max(jogadores)}')
print(f'-'*15, 'O Jogo Terminou', '-'*15)
