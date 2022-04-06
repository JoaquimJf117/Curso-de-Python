print('\033[32;1mDESAFIO 94 - Unindo Dicionários e Listas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
pessoa = dict()
galera = list()
soma = media = 0
# -----------------------------------------------------------------------
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('[ERRO!] Por favor, Digite apenas [M] ou [F].')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('[ERRO!] Responda apenas [S] ou [N].')
    if resp == 'N':
        break
print('=' * 50)
print(f'Ao todo temos {len(galera)} Pessoas Cadastradas.')
media = soma / len(galera)
print(f'A média de Idade é de {media:5.2f} Anos.')
print(f'As mulheres Cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Sexo"]} ', end='')
print()
