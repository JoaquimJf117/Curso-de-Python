print('\033[32;1mDESAFIO 11 - Pintando Parede \033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
print(f'Sua Parede têm a Dimensão de {largura}x{altura} e sua Área é de {area}m')
tinta = area / 2
print(f'Para Pintar essa Parede, Você precisará de {tinta}l de Tinta')
