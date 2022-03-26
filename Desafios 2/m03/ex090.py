print('\033[32;1mDESAFIO 90 - Dicionário em Python v0.1\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
aluno = dict()
# -----------------------------------------------------------------------
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 10:
    aluno['Situação'] = 'APROVADO'
elif 7 <= aluno['Média'] < 10:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-'*50)
for k, v in aluno.items():
    print(f' - {k}: {v}')
