print('\033[32;1mDESAFIO 28 - Jogo de Adivinha V.1.0\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
from time import sleep
from random import randint
computador = randint(0, 5)  # Faz o Computador "PENSAR NUM NÚMERO"
print('-=' * 30)
print('  \033[34;1mVou Pensar em um Número entre 0 e 5. Tente Adivinhar...\033[m')
print('-=' * 30)
jogador = int(input('Em que Número eu Pensei? '))  # Jogador tenta Adivinhar
print('\033[35;1mPROCESSANDO...\033[m')
sleep(2)
if computador == jogador:
    print('\033[32;1mPARABÉNS! Você Consegui me Venceu.\033[m')
else:
    print(f'\033[31;1mGANHEI! Eu pensei no Número {computador} e não no {jogador}!\033[m')
