print('\033[32;1mDESAFIO 31 - Custo de Viagem\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
distancia = float(input('Qual é a Distância da sua Viagem: '))
print(f'Você está prestes a começar uma Viagem de {distancia}Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o Preço da sua Passagem será de R${preco:.2f}')
