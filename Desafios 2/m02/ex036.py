print('\033[32;1mDESAFIO 36 - Aprovando Empréstimo\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
casa = float(input('Valor da Casa: R$'))
salário = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos Anos de Financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma Casa de R${casa:.2f} em {anos} anos, a Prestação será  de R${prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')