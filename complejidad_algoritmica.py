import time
from functools import reduce


def factorial(numero):
    start = time.time()
    answer = reduce(lambda x, y: x*y, [i for i in range(1, numero + 1)])
    end = time.time()
    return answer, end-start


print(factorial(10000))

# El punto es que las funciones en la programación también tienen un crecimiento exponencial y mientras
# más hacia arriba en la recta (como es el caso de la cuadrática o la factorial), peor es el algoritmo