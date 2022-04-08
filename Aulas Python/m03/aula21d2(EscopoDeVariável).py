# >>> Escopo de Variável <<<
# ---------------------------------------------------
def função():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')


# Programa Principal
n1 = 2
função()
print(f'N1 fora vale {n1}')

# n1 fora é global
# n1 dentro é local
