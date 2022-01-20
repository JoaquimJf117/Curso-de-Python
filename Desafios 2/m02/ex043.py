print('\033[32;1mDESAFIO 43 - Índice de Massa Corporal\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)
peso = float(input('Qual é o seu PESO (Kg)? '))
altura = float(input('Qual é sua Altura (M)? '))
imc = peso / (altura ** 2)
print(f'O IMC dessa Pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você esta em OBESIDADE MÓRBIDA, Cuidado!')
