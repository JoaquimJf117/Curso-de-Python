print('=' * 15, '\033[1;35mAULA 17 - Listas[Testes]\033[m', '=' * 15)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um Valor: ')))

for c, v in enumerate(valores):
    print(f'Na Posição {c} encontrei o Valor {v}!')
print('End!!!')
