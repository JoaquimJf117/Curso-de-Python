print('\033[32;1mDESAFIO 103 - Função do Jogador\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)


def ficha(jog='<desconhecido>', g=0):
    print(f'O Jogador {jog} fez {g} gol(s) no Campeonato.')


# Programa Principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Numero de Gol(s): '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
