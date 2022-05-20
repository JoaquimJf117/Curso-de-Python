# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 033 - Maior e Menor Valor\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def MaiorMenor():
    n1 = int(input('Primeiro Número: '))
    n2 = int(input('Segundo Número: '))
    n3 = int(input('Terceiro Número: '))

    # Verificando o Maior Valor [Forma de Rodeio]
    if n1 > n2 and n1 > n3:
        print(f'O Maior valor digitado foi {n1}')
    elif n2 > n1 and n2 > n3:
        print(f'O Maior valor digitado foi {n2}')
    elif n3 > n1 and n3 > n2:
        print(f'O Maior valor digitado foi {n3}')

    # Verificando o Menor Valor [Forma Simples]
    menor = n1
    if n2 < n1 and n2 < n3:
        menor = n2
    elif n3 < n1 and n3 < n2:
        menor = n3
    print(f'O Menor valor digitado foi {menor}')
# -----------------------------------------------------------------------


# Programa Principal
MaiorMenor()
