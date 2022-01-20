print('\033[32;1mDESAFIO 58 - Jogo da Advinha V.2.0\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
from random import randint
computador = randint(0, 10)
print('Sou seu Computador...')
print('Acabei de pensar em um número entre 0 e 10. '
      '\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual foi seu Palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'\033[36mAcertou! com {palpites} Tentativas')
