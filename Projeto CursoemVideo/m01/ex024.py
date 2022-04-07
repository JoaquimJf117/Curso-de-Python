print('\033[32;1mDESAFIO 24 - Verificando as Primeiras Letras do Texto\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
cid = str(input('Em que Cidade você Nasceu: ')).strip()
print(cid[:7].upper() == 'LUANDA')
