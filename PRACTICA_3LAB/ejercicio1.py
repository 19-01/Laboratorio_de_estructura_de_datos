listacompras = []

while True:
    print("Elija una opción:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista de compras")
    print("4. Salir")

    opcion = input("Opción elegida: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        listacompras.append(producto)
        print(f"{producto} ha sido agregado a la lista.")

    elif opcion == "2":
        if len(listacompras) == 0:
            print("La lista de compras está vacía.")
        else:
            eliminado = listacompras.pop(0)
            print(f"{eliminado} la lista fue eliminada.")

    elif opcion == "3":
        if len(listacompras) == 0:
            print("lista de compras vacía.")
        else:
            print("Lista de compras:")
            for i, producto in enumerate(listacompras):
                print(f"{i + 1}. {producto}")

    elif opcion == "4":
        print("¡Que tenga un buen día!")
        break

    else:
        print("La opción que a elejido es invalida. escoja un numero:")