print('\033[32;1mDESAFIO 10 - Conversor de Moeda\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
din = float(input('Quanto Dinheiro você têm na Carteira? R$: '))
dolar = din / 3.27
print(f'Com R${din:.2f} você pode Comprar U$${dolar:.2f}')
