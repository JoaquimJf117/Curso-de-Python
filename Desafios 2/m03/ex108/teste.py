import moeda

preço = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O Dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, teremos {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Reduzindo 13%, teremos {moeda.moeda(moeda.reduzir(preço, 13))}')
