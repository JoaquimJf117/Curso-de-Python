print('\033[32;1mDESAFIO 92 - Cadastro de Trabalhador com Python\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
from datetime import datetime
# -----------------------------------------------------------------------
pessoa = dict()
# -----------------------------------------------------------------------
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não têm): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: A0A'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - datetime.now().year)
elif pessoa['CTPS'] == 0:
    pessoa['CTPS'] = 'Não Possui um Emprego!!'
print('-' * 15, 'Dados Pessoais', '-' * 15)
for k, v in pessoa.items():
    print(f' - {k}: {v}')
