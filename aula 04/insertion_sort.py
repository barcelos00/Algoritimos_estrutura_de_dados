def insertion_sort(lista):
    n = len(lista)
    deslocamentos = 0
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            deslocamentos += 1
            j -= 1
        lista[j + 1] = chave
    print("deslocamentos=" + str(deslocamentos))
    return lista