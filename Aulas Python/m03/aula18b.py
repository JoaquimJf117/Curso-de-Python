print('=' * 15, '\033[1;35mAULA 18 - Listas[Part #2]\033[m', '=' * 15)
# --------------------------------------------------------------------
teste = list()
galera = list()
# --------------------------------------------------------------------
teste.append('Joaquim')
teste.append(20)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
