def merge_sort(lista):
 
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return fusionar(izquierda, derecha)


def fusionar(izquierda, derecha):

    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def busqueda_binaria(lista, objetivo):
   
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  


def solicitar_entero(mensaje):
  
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente de nuevo.")


def main():
    print(" SISTEMA DE GESTIÓN DE CÓDIGOS DE PRODUCTOS ")


    n = 0
    while n <= 0:
        n = solicitar_entero("Ingrese la cantidad de productos: ")
        if n <= 0:
            print("La cantidad debe ser mayor a 0.")

    codigos = []

   
    for i in range(1, n + 1):
        codigo = solicitar_entero(f"Ingrese el código del producto {i}: ")
        codigos.append(codigo)

    print(f"La lista original sería:\{codigos}")

    # 2. Ordenar los productos con Merge Sort
    codigos_ordenados = merge_sort(codigos)
    print(f"\nPunto 1. Resultados ordenados con Merge Sort:\n{codigos_ordenados}")

 
    print("\ Punto 2. Búsqueda de Productos")
    buscar = solicitar_entero("Ingrese el código que desea buscar: ")

    posicion = busqueda_binaria(codigos_ordenados, buscar)

    if posicion != -1:
        print(f"El producto con código {buscar} fue encontrado.")
    else:
        print(f"El producto con código {buscar} no se encuentra registrado.")


if __name__ == "__main__":
    main()
