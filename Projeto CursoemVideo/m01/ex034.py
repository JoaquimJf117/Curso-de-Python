print('\033[32;1mDESAFIO 34 - Aumentos Múltiplos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
sal = float(input('Qual é o Salário do Funcionário? R$ '))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print(f'Para Funcionários que Ganhavam R${sal:.2f}, Passaram a Ganhar R${nsal:.2f}')
