import math

def merge(array, inicio, fim, divisao):
    k = 0
    j = 0
    p = inicio
    direita = []
    esquerda = []
    for i in range(inicio, divisao):
        direita.append(array[i])
    for i in range(divisao, fim):
        esquerda.append(array[i])

    while j < len(direita) and k < len(esquerda):
        if direita[j] < esquerda[k]:
            array[p] = direita[j]
            j += 1
        else:
            array[p] = esquerda[k]
            k += 1
        p += 1

    while j < len(direita):
        array[p] = direita[j]
        j += 1
        p += 1

    while k < len(esquerda):
        array[p] = esquerda[k]
        k += 1
        p += 1

def merge_sort(array, inicio, fim):
    if inicio < fim:
        q = math.floor((inicio + fim) / 2)
        merge_sort(array, inicio, q)
        merge_sort(array, q+1, fim)
        merge(array, inicio, fim, q)

def sort(array):
    merge_sort(array, 0, len(array))


