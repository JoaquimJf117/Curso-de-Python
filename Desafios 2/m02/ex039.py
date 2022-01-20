print('\033[32;1mDESAFIO 39 - Alistamento Militar\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
from datetime import date
atual = date.today().year
nome = str(input('Nome Completo: ')).strip()
n = nome.split()
sexo = str(input('Sexo[F/M]: ')).upper()
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'\033[36;1m{n[0]} você Nasceu em {nasc} e tens {idade} anos\033[m.')
if sexo == 'F':
    print(f'{n[0]} você não Precisa fazer Alistamento Militar Obrigatório!')
else:
    if idade == 18:
        print('Você têm que se Alistar Imediatamente ao Serviço Militar!\033[m')
    elif idade < 18:
        saldo = 18 - idade
        print(f'\033[32;1mAinda Faltam {saldo} anos para você se Alistar ao Serviço Militar!\033[m')
        ano = atual + saldo
        print(f'Seu Alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        print(f'\033[31;1mVocê ja Deveria se Alistar ao Serviço Militar há {saldo} anos!\33[m')
        ano = atual - saldo
        print(f'Seu Alistamento foi em {ano}')
