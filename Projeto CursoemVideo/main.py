from time import sleep
mod = [1, 2, 3]
# -------------------------------------------------------------------
print(f'{"PROJETO CURSO EM VIDEO":^50}')
print('-'*50)
sleep(1)
print(f'{"MÓDULOS":^50}')
print(''' => [Módulo 01]
 => [Módulo 02]
 => [Módulo 03]''')
opção = int(input("Seleciona um Módulo: "))
print('-'*50)
if opção == 1:
    sleep(1)
    print(f'{"[Módulo 01]":^50}\n {"[Lista de Exercícios (1...35)]":^50}')
    print('-'*50)
    print('''    [01] - Deixando Tudo Pronto
    [02] - Respondendo ao Usuário
    [03] - Somando dois Números
    [04] - Dissecando uma Variável
    [05] - Antecessor e Sucessor
    [06] - Dobro, Triplo e Raiz Quadrada
    [07] - Média Aritmética [Clássico]
    [08] - Conversor de Medidas
    [09] - Tabuada [Versão 0]
    [10] - Conversor de Moeda''')
    print('-'*50)
    sleep(1)
    escolha = int(input('Qual Exercício quer Ver: '))
    if escolha == 1:
        sleep(1)
        print(f'{"[01] - Deixando tudo Pronto":^50}')
        print('-'*50)
