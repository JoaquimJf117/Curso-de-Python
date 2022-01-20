print('\033[32;1mDESAFIO 56 - Analisador Completo\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
somaidade = mediaidade = maiorhomem = nomevelho = totmulhe20 = 0
for p in range(1, 5):
    print(f'---------- {p}ª PESSOA ----------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulhe20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do Grupo é de {mediaidade}')
print(f'O Homem Mais Velho tem {maiorhomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulhe20} Mulheres com Menos de 20 anos')
