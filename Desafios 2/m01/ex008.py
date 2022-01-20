print('\033[32;1mDESAFIO 8 - Conversor de Medidas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
medida = float(input('Uma Distância em Metros: '))
cm = medida * 100  # Centrimentro
mm = medida * 1000  # Milimetro
print(f'A media de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')
