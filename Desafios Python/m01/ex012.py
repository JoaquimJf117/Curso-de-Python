print('\033[32;1mDESAFIO 012 - Calculando Descontos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
produto = float(input('Qual é o preço do Produto: R$'))
desconto = produto - (produto * 5 / 100)
print(f'O Produto que Custava R${produto:.2f}, na promoção com '
      f'Desconto de 5% vai custar R${desconto:.2f}')
# -----------------------------------------------------------------------
