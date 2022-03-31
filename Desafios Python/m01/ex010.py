print('\033[32;1mDESAFIO 010 - Conversor de Moeda\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
real = float(input('Quanto Dinheiro você tem na Carteira? R$'))
dolar = real / 3.27
print(f'Com R${real:.2f} você pode Comprar US${dolar:.2f}')
# -----------------------------------------------------------------------
