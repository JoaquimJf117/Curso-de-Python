print('\033[32;1mDESAFIO 013 - Reajuste Salarial\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
salario = float(input('Qual é o Salário do Funcionário: R$'))
reajuste = salario + (salario * 15 / 100)
print(f'Um Funcionário que Ganhava R${salario:.2f}, com 15% de '
      f'aumento, passará a Receber R${reajuste:.2f}')
# -----------------------------------------------------------------------
