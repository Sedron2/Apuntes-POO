def busqueda(lista, numero, comienzo, final):
    epsilon = (comienzo + final) // 2
    print(epsilon)

    if lista[numero] < epsilon:
        busqueda(lista, numero, comienzo, epsilon)

    elif lista[numero] > epsilon:
        busqueda(lista, numero, epsilon, final)

    return "termine"


lista = range(int(input("De que tamaño quieres que sea la lista?: ")))
numero = int(input("Que número quieres encontrar?: "))

print(busqueda(lista, numero, 0, len(lista)))