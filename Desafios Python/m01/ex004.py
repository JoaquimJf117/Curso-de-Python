print('\033[32;1mDESAFIO 04 - Dissecando uma Variável\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
palavra = input('Digite Algo: ')
print(f'O tipo Primitivo desse valor é {type(palavra)}')
print(f'Só têm Espaços? {palavra.isspace()}')
print(f'É Númerico? {palavra.isnumeric()}')
print(f'É Alfabético? {palavra.isalpha()}')
print(f'É Alfanúmerico? {palavra.isalnum()}')
print(f'Está em Maiúscula? {palavra.isupper()}')
print(f'Está em Minúscula? {palavra.islower()}')
print(f'Está Capitalizada? {palavra.istitle()}')
# -----------------------------------------------------------------------
