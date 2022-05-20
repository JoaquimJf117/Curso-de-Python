# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 034 - Aumento Múltiplos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def AumentoSalarial():
    func_salario = float(input('Salário do Funcionário:AOA '))
    if func_salario <= 1250:
        novo_func_salario = func_salario + (func_salario * 15 / 100)
        print(f'Quem Ganhava {func_salario:.2f}AOA por mês.'
              f'\nCom aumento de 15% o Funcionário passará ganhar {novo_func_salario:.2f}AOA por mês.')
    elif func_salario > 1250:
        novo_func_salario = func_salario + (func_salario * 10 / 100)
        print(f'Quem Ganhava {func_salario:.2f}AOA por mês.'
              f'\nCom aumento de 10% o Funcionário passará ganhar {novo_func_salario:.2f}AOA por mês.')
# -----------------------------------------------------------------------


# Programa Principal
AumentoSalarial()
