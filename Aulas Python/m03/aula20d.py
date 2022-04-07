def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
valores = [7, 2, 5, 0, 4]
print(valores, ' <-- Antes')
dobra(valores)
print(valores, '<-- Depois')
