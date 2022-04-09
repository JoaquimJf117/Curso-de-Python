print('\033[32;1mDESAFIO 101 - Função para Votar\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)


def votar(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if ano > atual:
        return'[ERRO!]Por favor Insira a Data correcta do seu Nascimento!'
    elif idade < 17:
        return f'Com {idade} Anos: Você NÃO PODE VOTAR!'
    elif 17 <= idade < 18 or idade > 60:
        return f'Com {idade} Anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} Anos: VOTO OBRIGATÓRIO!'


# Programa Principal
nasc = int(input('Em que Ano você Nasceu: '))
print(votar(nasc))
