def seleccion_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Pedimos al usuario que ingrese 10 números en desorden
numeros = []
print("Ingresa 10 números del 1 al 10 en desorden:")
for _ in range(10):
    num = int(input("Número: "))
    numeros.append(num)

# Ordenamos la lista con el algoritmo de selección
seleccion_sort(numeros)
print("Lista ordenada:", numeros)
