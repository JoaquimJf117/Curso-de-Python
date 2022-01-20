print('\033[32;1mDESAFIO 40 - Media do Aluno\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-'*40)
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a sua Média é de {media:.1f}')
if 7 > media >= 5:
    print('Aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('Aluno está REPROVADO!')
elif media >= 7:
    print('O Aluno está APROVADO!')
