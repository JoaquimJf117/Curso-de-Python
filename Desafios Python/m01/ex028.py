import random
import time
# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 028 - Jogo de Advinhação v.1.0\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
print('='*80)
print('\tEstou Pensando num número entre [0] e [5], tente adivinhar...')
print('='*80)
computador = random.randint(0, 5)
jogador = int(input('\tEm que número o Computador pensou: '))
time.sleep(1)
print('-'*80)
if jogador == computador:
    print('\tPARABÉNS!! Você consegui me Vencer!')
else:
    print(f'\tTry Again! I think this number {computador}')
# -----------------------------------------------------------------------
