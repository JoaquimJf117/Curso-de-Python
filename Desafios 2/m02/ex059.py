print('\033[32;1mDESAFIO 59 - Criando Menu de Opções\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''\033[32;1m    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa\033[m''')
    opcao = int(input('Qual é a sua Opção: '))
    if opcao == 1:
        soma = v1 + v2
        print(f'\033[33;1mA Soma entre {v1} + {v2} = {soma}')
    elif opcao == 2:
        multi = v1 * v2
        print(f'\033[35;1mA Multiplicação entre {v1} x {v2} = {multi}')
    elif opcao == 3:
        if v1 > v2:
            print(f'\033[34mEntre {v1} e {v2} Maior é {v1}')
        elif v1 < v2:
            print(f'\033[33mEntre {v1} e {v2} Maior é {v2}')
        else:
            print('\033[35mOs dois valores são Iguais, não exite Maior entre eles.')
    elif opcao == 4:
        print('\033[37mInsere Novos Números!\033[m')
        v1 = int(input('\033[36mPrimeiro Valor: '))
        v2 = int(input('Segundo Valor: \033[m'))
    elif opcao == 5:
        print('Finalizando..')
    else:
        print('\033[35mOpção inválida. Tente Novamente')
    print('=-' * 25)
print('\033[31;1mFim do Programa! Volte Sempre...')
