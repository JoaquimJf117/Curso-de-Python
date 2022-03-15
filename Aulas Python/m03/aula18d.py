print('=' * 15, '\033[1;35mAULA 18 - Listas[Part #2]\033[m', '=' * 15)
# --------------------------------------------------------------------
galera = []
dados = list()
totmai = totmen = 0
# --------------------------------------------------------------------
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()  # Limpando dados
for p in galera:
    if p[1] >= 20:
        print(f'{p[0]} é Maior de Idade.')
        totmai += 1
    else:
        print(f'{p[0]} é Menor de Idade.')
        totmen += 1
print(f'Temos {totmai} Maiores e {totmen} Menores de Idade.')
