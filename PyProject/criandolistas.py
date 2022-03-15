# Acessando os Dados da Listas
# ------------------------------------------------------------------------
frutas = ['Maçã', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
print(frutas[4])  # Indexação Positiva
print(frutas[-5])  # Indexação Negativa
print('-'*50)

# Listas de Listas
# ---------------------------------------------------------------------------
lista = ['HTML', ['Css3', 'Bootstrap'], 'JavaScript']
sublista = lista[1]
print(lista[2])  # Lista Principal
print(sublista[1])  # lista dentro da Lista (sublista)
print('-'*50)

# Fatiamento de Listas
# ---------------------------------------------------------------------------
numeros = [10, 20, 30, 40, 50, 60]
print(numeros)
for i, v in enumerate(numeros):
    print(f'Índice => {i} ||| Valor => {v}')
[print(num) for num in numeros]  # List Comprehension
