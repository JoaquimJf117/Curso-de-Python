# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 031 - Preço da Passagem\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
distancia = float(input('Qual é a distancia da Viagem:[km] '))
print(f'Você está prestes a começar uma viagem de {distancia}Km')
if distancia <= 200:
    preço = distancia * 0.50
    print(f'E o preço da sua Passagem será de R${preço:.2f}')
else:
    preço = distancia * 0.45
    print(f'E o preço da sua Passagem será de R${preço:.2f}')
# -----------------------------------------------------------------------
