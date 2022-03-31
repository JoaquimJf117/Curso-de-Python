print('\033[32;1mDESAFIO 08 - Conversor de Medidas\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
dist = float(input('Digite Uma Distância em Metros(m): '))
cm = dist * 100
mm = dist * 1000
print(f'A distância de {dist}m corresponde a {cm:.0f}cm e {mm:.0f}mm')
# -----------------------------------------------------------------------
