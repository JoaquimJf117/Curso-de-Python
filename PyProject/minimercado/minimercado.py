print('-' * 40)
print(f'\033[34;1m{"MINIMERCADO JF":^40}\033[m')
print('-' * 40)
print('''\033[32;1m           SECTORES\033[m
[ 1 ] Máterias Escolares
[ 2 ] Máterias de Construções
[ 3 ] Máterias Electrônico
[ 4 ] Exit''')
while True:
    opcao = int(input('Qual Sector deseja Visitar? '))
    if opcao == 1:
        print('-' * 45)
        print(f'\033[32;1m{"SECTOR A":^40}\033[m')
        print('-' * 45)
        mescola = ('Lápis', 30,
                   'Caderno', 100,
                   'Caneta', 70,
                   'Borracha', 45,
                   'Livro', 2500,
                   'Estojo', 500,
                   'Compasso', 300,
                   'Mochila', 1500)
        for pos in range(0, len(mescola)):
            if pos % 2 == 0:
                print(f'{mescola[pos]:.<30}', end='')
            else:
                print(f'{mescola[pos]:.>10.2f}Kz')
    elif opcao == 2:
        print('-' * 45)
        print(f'\033[32;1m{"SECTOR B":^40}\033[m')
        print('-' * 45)
        mcons = ('Bota de Borracha', 1500,
                 'Macacão de Pedreiro', 3500,
                 'Martelo de Borracha', 2000,
                 'Machado', 1500,
                 'Pá', 1000,
                 'Capacete', 800,
                 'Colher de Pedreiro', 1000,
                 'Andaimer', 10000)
        for item in range(0, len(mcons)):
            if item % 2 == 0:
                print(f'{mcons[item]:.<30}', end='')
            else:
                print(f'{mcons[item]:.>10.2f}Kz')
    elif opcao == 3:
        print('-' * 45)
        print(f'\033[32;1m{"SECTOR C":^40}\033[m')
        print('-' * 45)
        melec = ('Computador', 95000,
                 'CPU', 75000,
                 'Mouse', 2500,
                 'Teclado', 4500,
                 'Impressora', 55000,
                 'PlayStation 3', 170000,
                 'Hard Disk', 7500,
                 'Pendrive', 3500)
        for item in range(0, len(melec)):
            if item % 2 == 0:
                print(f'{melec[item]:.<30}', end='')
            else:
                print(f'{melec[item]:.>10.2f}')
    elif opcao == 4:
        break
print('\033[34mObrigado Pela Preferencia! Volte Sempre...')
