print('\033[32;1mDESAFIO 25 - Procurando uma String dentro de Outra \033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
nome = str(input('Qual é o seu Nome Completo: ')).strip()
print('Seu Nome têm Fernando? {}'.format('fernando' in nome.lower()))
