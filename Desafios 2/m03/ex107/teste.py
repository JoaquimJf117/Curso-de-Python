import moeda

preço = float(input('Digite o Preço: R$'))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O Dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10% teremos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo 13% teremos {moeda.reduzir(preço, 13)}')
