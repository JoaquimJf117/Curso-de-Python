print('\033[32;1mDESAFIO 55 - Maior e Menor da Sequência\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª Pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O Maior Peso lido foi de {maior}Kg')
print(f'O Menor Peso lido foi de {menor}Kg')
