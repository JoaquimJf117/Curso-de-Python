print('\033[32;1mDESAFIO 29 - Radar Electrônico\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
vel = float(input('Qual é a Velocidade atual do Veiculo? '))
if vel > 80:
    print(f'\033[31;1mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    multa = (vel - 80) * 7
    print(f'\033[31;1mVocê deve pagar uma multa de R${multa:.2f}\033[m')
print('Tenha um Bom Dia! Dirija com Segurança')
