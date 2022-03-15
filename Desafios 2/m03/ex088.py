print('\033[32;1mDESAFIO 88 - Aposte No Mega Sena\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
from random import randint
from time import sleep
lista = list()
jogos = list()
# -----------------------------------------------------------------------
print(f'{"JOGA NA MEGA SENA":^50}')
print('-'*50)
quant = int(input('Quantos Jogos Você quer que Eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*5, f'SORTEANDO {quant} JOGOS ', '-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo{i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)
