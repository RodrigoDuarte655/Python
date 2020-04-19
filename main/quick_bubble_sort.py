import timeit
import time
from random import seed
from random import randint

""" # Implementação do Bubble Sort """


def bubble_sort(array):
    # Passar pela lista enquanto houver elementos
    for _ in range(len(array)):
        # O objetivo é que o último par de elementos adjacentes seja (n-2, n-1)
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                # Faz a troca (swap)
                array[j], array[j+1] = array[j+1], array[j]


"""
Implementação do Quick Sort """


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Se o valor corrente é maior que o pivô, ele está no lugar certo, basta
        # mover o ponteiro high à esquerda. Senão, ele está na posição errada e o laço deve
        # ser interrompido
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Mesmo raciocício se aplica com low
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Nesse ponto, ou achamos dois valores que precisam ser trocados, ou então
        # low > high e não há troca a fazer
        if low <= high:
            # Executando a troca
            array[low], array[high] = array[high], array[low]
        else:
            # Saindo do loop
            break
    # Colocando o pivô na posição correta
    # (Todos à esquerda do pivô são menores e todas à direita são maiores)
    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


""" Escreva um programa que gere uma lista com 10.000 números
inteiros (gerados randomicamente no intervalo entre 1 e
10.000) """

array = []


def gerarListaAleatoria():
    seed(1)

    for _ in range(10000):
        value = randint(1, 10000)
        array.append(value)


""" Computar o tempo gasto para ordenar a lista usando o
Quicksort """

gerarListaAleatoria()
inicio_quick = timeit.default_timer()
quick_sort(array, 0, len(array) - 1)
fim_quick = timeit.default_timer()

""" Computar o tempo gasto para ordenar a lista usando o
Bubble sort """

array = []
gerarListaAleatoria()
inicio_bubble = timeit.default_timer()
bubble_sort(array)
fim_bubble = timeit.default_timer()


""" Imprimir os resultados obtidos, em milisegundos """

print(
    f'Duracao do Quick Sort: {(fim_quick - inicio_quick) * 1000} milisegundos')

print(
    f'Duracao do Bubble Sort: {(fim_bubble - inicio_bubble) * 1000} milisegundos')
