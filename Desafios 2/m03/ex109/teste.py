import moeda

preço = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O Dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, teremos {moeda.aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, teremos {moeda.reduzir(preço, 13, True)}')
