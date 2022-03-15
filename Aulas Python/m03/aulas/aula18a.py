print('=' * 15, '\033[1;35mAULA 18 - Listas[Testes]\033[m', '=' * 15)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
