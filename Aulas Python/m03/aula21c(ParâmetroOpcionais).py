# >>> Parâmetros Opcional <<<
# ---------------------------------------------------
#
def somar(a=0, b=0, c=0):
    """
    -> Faz a Soma de Três Valores e mostra na Tela.
    :param a: O primeiro Valor
    :param b: O segundo Valor
    :param c: O terceiro Valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(a=4, b=7, c=9)  # Informando Directamente
somar(3, 2, 5)  # Informando todos os valores
somar(8, 4)  # Informando metade dos valores
somar()  # Nenhum valor Informado
