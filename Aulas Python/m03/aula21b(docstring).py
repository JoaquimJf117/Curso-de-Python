# >>> docstrings <<<
# ---------------------------------------------------
# Docstring é basicamente uma String de Documentação [Manual]
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da Contagem
    :param f: Fim da Contagem
    :param p: Passo da Contagem
    :return: Sem Retorno
    Função criada por Gustavo Guanabara do canal do CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)
