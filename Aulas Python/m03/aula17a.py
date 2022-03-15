print('=' * 15, '\033[1;35mAULA 17 - Listas[Testes]\033[m', '=' * 15)
num = [2, 5, 9, 1]  # Lista
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
# num.pop(2)
print(num)
print(f'Essa lista têm {len(num)} elementos')
