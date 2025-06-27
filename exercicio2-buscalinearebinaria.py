def h_index_linear(citacoes):
    for i in range(len(citacoes)):
        h = i + 1
        if citacoes[i] < h:
            return i
    return len(citacoes)


def h_index_binaria(citacoes):
    inicio = 0
    fim = len(citacoes) - 1

    while inicio <= fim:
        meio = (inicio+fim) // 2 
        h = meio + 1

        if citacoes[meio] >= h:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio

citacoes = [10, 8, 5, 4, 3] 
print("Índice-h linear:", h_index_linear(citacoes))
print("Índice-h binaria:", h_index_binaria(citacoes))