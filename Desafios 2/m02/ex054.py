print('\033[32;1mDESAFIO 54 - Grupo de Maioridade\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
from datetime import date
atual = date.today().year
totmenor = totmaior = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas Maiores de Idade')
print(f'E também tivemos {totmenor} pessoas Menores de Idade')
