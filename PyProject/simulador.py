print('-'*50)
print('              \033[1;32mSimulador de Eleição\033[m')
print('-'*50)

partidos = ('FNLA', 'UNITA', 'PRS', 'CASA-CE', 'MPLA')
cores = ('Azul', '\033[1;33m'
         'Verde', '\033[1;32m'
         'Amarelo', '\033[1;34m'
         'Limpa', '\033[m')
# print(partidos[0])
print('''    [ 0 ] para Votar
    [ 1 ] para ver os Presidentes
    [ 2 ] para ver Total de Votos
    [ 3 ] para Sair''')
totU = totM = totF = totP = totC = 0
voto = int(input('Escolha: '))
while voto != 3:
    if voto == 0:
        print('''    [ 1 ] UNITA
    [ 2 ] PRS
    [ 3 ] CASA-CE
    [ 4 ] MPLA
    [ 5 ] FNLA
    [ 6 ] Sair''')
        votop = int(input('Escolha o Partido: '))
        if votop == 1:
            print(f'Votaste na {partidos[1]}') # UNITA
            totU += 1
        elif votop == 2:
            print(f'Votaste no {partidos[2]}') # PRS
            totP += 1
        elif votop == 3:
            print(f'Votaste na {partidos[3]}') # CASA-CE
            totC += 1
        elif votop == 4:
            print(f'Votaste no {partidos[4]}') # MPLA
            totM += 1
        elif votop == 5:
            print(f'Votaste no {partidos[0]}') # FNLA
        elif votop == 6:
            print('''    [ 0 ] para Votar
    [ 1 ] para ver os Presidentes
    [ 2 ] para ver Total de Votos
    [ 3 ] para Sair''')
            voto = int(input('Escolha: '))
    elif voto == 1:
        print(f'''[{partidos[1]}] Aldaberto Raul Danda 
[{partidos[2]}] Manuel Garcia 
[{partidos[3]}] Abel Chivukuvuku 
[{partidos[4]}] João Manuel Gonçalves Lourenço
[{partidos[0]}] Miguel Afonso''')
        print('\033[1;35m-\033[m'*35)
        print('''[ 0 ] para Votar
[ 1 ] para ver os Presidentes
[ 2 ] para ver Total de Votos
[ 3 ] para Sair''')
        voto = int(input('Escolha: '))
    elif voto == 2:
        print(f'{partidos[1]} recebeu Total de {totU} Votos.')
        print(f'{partidos[2]} recebeu Total de {totP} Votos.')
        print(f'{partidos[3]} recebeu Total de {totC} Votos.')
        print(f'{partidos[4]} recebeu Total de {totM} Votos.')
        print(f'{partidos[0]} recebeu Total de {totF} Votos.')
        print('\033[1;35m-\033[m' * 35)
        print('''[ 0 ] para Votar
[ 1 ] para ver os Presidentes
[ 2 ] para ver Total de Votos
[ 3 ] para Sair''')
        voto = int(input('Escolha: '))
    elif voto == 3:
        print('\033[1;31mTerminando o Simulador...\033[m')