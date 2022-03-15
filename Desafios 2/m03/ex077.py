print('\033[32;1mDESAFIO 77 - Contando Vogais\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)

palavras = ('aprender', 'programar', 'línguagem', 'python', 'curso', 'grátis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aáàâãeéèêiíìîoóòôõuúùû':
            print(letra, end=' ')
