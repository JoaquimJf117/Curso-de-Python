print('\033[32;1mDESAFIO 89 - Boletim com Lista Compostas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
alunos = []
# -----------------------------------------------------------------------
while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('1ª Nota do Aluno: '))
    nota2 = float(input('2ª Nota do Aluno: '))
    resp = str(input('Quer Continuar?[S/N] '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    if resp in 'Nn':
        break
print('-'*50)
print(f'{"Nº":<5} {"Nome":^15} {"MÉDIA":>15}')
print('-'*50)
for i, a in enumerate(alunos):
    print(f'{i:<5}{a[0]:^15}{a[2]:>15.1f}')
while True:
    print('-'*50)
    opc = int(input('Mostrar Notas de qual Aluno? (999 interrompe): '))
    if opc == 999:
        print('------------- FINALIZANDO -------------')
        break
    if opc <= len(alunos)-1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
