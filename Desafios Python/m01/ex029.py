
# -----------------------------------------------------------------------
print('\033[32;1mDESAFIO 029 - Radar Eletrônico\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)
# -----------------------------------------------------------------------
vel = int(input('Qual é a Velocidade atual do carro: [km]'))
if vel > 80:
    print(f'Multado! você excedeu o limite permitido que é de 80Km/h')
    multa = vel * 7
    print(f'Você deve pagar uma Multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com Segurança!')
# -----------------------------------------------------------------------
