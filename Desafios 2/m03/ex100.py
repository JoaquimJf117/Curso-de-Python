print('\033[32;1mDESAFIO 100 - Função para Sortear e Somar\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
from random import *
from time import *


def sorteia(lista):
    print('Sorteando 5 valores da Lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os Valores Pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
