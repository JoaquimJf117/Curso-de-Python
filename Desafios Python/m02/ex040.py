# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 040 - Média do Aluno[v1]\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------


def MediaAluno():
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    print(f'A sua Média é de {media}')
    if 9 > media >= 5:
        print('O Aluno está em RECUPERAÇÃO .')
    elif media < 5:
        print('O Aluno está REPROVADO')
    elif media >= 9:
        print('O Aluno está APROVADO')
# -----------------------------------------------------------------------


# Programa Principal
MediaAluno()
# 7
# 8 e 9
# 10
