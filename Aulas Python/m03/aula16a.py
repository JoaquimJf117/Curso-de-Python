print('=' * 15, '\033[1;35mAULA 16 - Tuplas[Testes]\033[m', '=' * 15)
# TUPLAS SÃO IMUTÁVEIS
# (TUPLAS) [LISTAS] {DICIONÁRIO}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou Comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Vou Comer {lanche[cont]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou Comer {comida} na Posição {pos}')
print('Comi pra Caramba')
print('-' * 80)
print(sorted(lanche))
