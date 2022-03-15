print('\033[32;1mDESAFIO 59 - Tuplas com Time de Futebol\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
print('-' * 80)

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmeio',
         'Cruzeiros', 'Flamengo', 'Vasco', 'Chapacoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'Avaí',
         'EC Vitória', 'Coritiba', 'Ponte Preta', 'Atlético-GO')
print(f'{"Tabela de Times do Brasileirão":^70}')
print('-'*80)
print(f'Lista Completa dos Times: {times}')
print('-'*280)
print(f'Os Primeiros 5 Times são: {times[:5]}')
print('-'*90)
print(f'Os Últimos 4 Colocados são: {times[-4:]}')
print('-'*90)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-'*280)
print(f"O Chapacoense está na {times.index('Chapacoense')+1}ª Posição")
print('-'*35)
