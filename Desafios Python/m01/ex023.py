import time
# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 023 - Separando dígitos de um número\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
numero = int(input('Informe um número: '))
print(f'Analisando o número {numero}')
time.sleep(1)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
# -----------------------------------------------------------------------
