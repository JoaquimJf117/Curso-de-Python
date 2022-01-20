print('\033[32;1mDESAFIO 44 - Gerenciador de Pagamentos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
print('========== \033[32;1mLOJAS FERNANDES\033[m ==========')
preco = float(input('Preço das Compras: R$'))
print('''\033[34;1mFORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão\033[m''')
opcao = int(input('Qual é a sua Opção: '))
if opcao == 1:
    des = preco - (preco * 10 / 100)
    print(f'Sua Compra que Custava R${preco:.2f}, com Desconto de 10% vai passar a Custar R${des:.2f}')
elif opcao == 2:
    des = preco - (preco * 5 / 100)
    print(f'Sua Compra que Custava R${preco:.2f}, com Desconto de 5% vai passar a Custar R${des:.2f}')
elif opcao == 3:
    des = preco
    parcela = des / 2
    print(f'Sua compra será Parcelada em 2x de R${parcela}')
    print(f'Sua Compra que Custava R${preco:.2f}, vai passar a Custar R${des:.2f} no final.')
elif opcao == 4:
    des = preco + (preco * 20 / 100)
    totparc = int(input('Quantas Parcelas: '))
    parcela = des / totparc
    print(f'Sua Compra será Parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
    print(f'Sua Compra que Custava R${preco:.2f}, vai Custar R${des:.2f} no final.')
else:
    des = 0
    print('\033[31;1mOPÇÃO INVÁLIDA de PAGAMENTO. Tente Novamente!\033[m')
print('Obrigado Volte Sempre as nossas Lojas!')
