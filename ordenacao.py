def quicksort(vetor):
    if len(vetor) < 2: return vetor
    pivot = vetor[0]
    menores, maiores = [], []
    for elemento in vetor[1:]:
        if elemento <= pivot:
            menores.append(elemento)
        else:
            maiores.append(elemento)
    return quicksort(menores) + [pivot] + quicksort(maiores)