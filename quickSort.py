import random

def particao(array, inicio, fim):
    pivo_index = random.randint(inicio, fim) 
    swap(array, pivo_index, fim)
    q = inicio
    pivo = array[fim]

    for i in range(inicio, fim):
        if array[i] < pivo:  
            swap(array, i, q)
            q += 1

    swap(array, fim, q)
    return q

def swap(array, inicio, fim):
    temp = array[fim]
    array[fim] = array[inicio]
    array[inicio] = temp

def quick_sort(array, inicio,fim):
    if inicio< fim:
        q = particao(array, inicio,fim)
        quick_sort(array, inicio,q-1)
        quick_sort(array, q+1,fim)
def sort(array):
    quick_sort(array,0,len(array)-1)
array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6]
sort(array)
print(array)
 