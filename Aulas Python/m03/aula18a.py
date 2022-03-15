print('=' * 15, '\033[1;35mAULA 18 - Listas[Part #2]\033[m', '=' * 15)
# --------------------------------------------------------------------
dados = []
pessoas = []
galera = [['Miguel', 25], ['Berta', 59], ['Joaquim', 20]]
# --------------------------------------------------------------------
dados.append('Joaquim')
dados.append(20)
dados.append('Fernando')
dados.append(23)
dados.append('Maria')
dados.append(19)
pessoas.append(dados[:])
# galera.append(pessoas[:])
print(galera[0][0])  # Miguel
print(galera[1][1])  # 59
print(galera[2][0])  # Joaquim
print(galera[1])  # Berta + 59
