print('\033[32;1mDESAFIO 015 - Aluguel de Carros\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
day = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))
totpagar = (day * 60) + (km * 0.15)
print(f'O total a pagar é de {totpagar:.2f}')
# -----------------------------------------------------------------------
