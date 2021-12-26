def morral(tamaño_morral, pesos, valores, n):
    if n == 0 or tamaño_morral == 0:
        return 0

    if pesos[n - 1] > tamaño_morral: #:/
        return morral(tamaño_morral, pesos, valores, n-1)

    return max(valores[n - 1] + morral(tamaño_morral - pesos[n - 1], pesos, valores, n-1), morral(tamaño_morral, pesos, valores, n - 1))
    


valores = [60, 100, 120]
pesos = [10, 20, 30]
tamaño = 50

resultado = morral(tamaño, pesos, valores, n=len(valores))
print(resultado)