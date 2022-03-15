print('\033[32;1mDESAFIO 72 - Números por Extenso\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 40)

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezasete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num <= num <= 20:
        break
    print('Tente novamente. Um número entre 0 e 20')
print(f'Você Digitou o Número: \033[1;35m{cont[num]}\033[m')
