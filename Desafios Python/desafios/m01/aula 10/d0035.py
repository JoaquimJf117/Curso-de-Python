print('='*20, 'DESAFIO 35', '='*20)
print('-=-'*20)
print(' '*16, 'Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um Triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo.')
