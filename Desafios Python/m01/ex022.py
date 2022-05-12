import time
print('\033[32;1mDESAFIO 022 - Analisador de Textos\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 50)

# -----------------------------------------------------------------------
nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisando seu Nome...')
time.sleep(1)
print(f'Seu Nome em Maiúsculas é {nome.upper()}')
time.sleep(1)
print(f'Seu Nome em Minúsculas é {nome.lower()}')
time.sleep(1)
print(f'Seu Nome tem ao todo {len(nome) - nome.count(" ")}')
time.sleep(1)
separa = nome.split()
print(f'Seu Primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
# -----------------------------------------------------------------------
