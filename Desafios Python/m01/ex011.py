print('\033[32;1mDESAFIO 011 - Pintando Parede\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt
print(f'A sua Parede tem a dimensão de {larg}x{alt} e sua área é de {area}m')
tinta = area / 2
print(f'Para pintar essa Parede, você precisará de {tinta}l de tinta')
# -----------------------------------------------------------------------
