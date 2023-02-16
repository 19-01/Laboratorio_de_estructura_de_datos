tareas_pend = []

while True:
    print("¿Qué acción quieres realizar?")
    print("1: Agregar tarea al inicio de la lista")
    print("2: Eliminar tarea del final de la lista")
    print("3: Mostrar las tareas en orden inverso al que se agregaron")
    print("4: Mostrar cantidad total de tareas")
    print("5: Salir, gracias ")

    opcion = input("Ingresa el número de la opción deseada realizar: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea por agregar")
        tareas_pend.insert(0, tarea)
        print("Tarea ingresada al inicio de la lista.")

    elif opcion == "2":
        if len(tareas_pend) == 0:
            print("La lista de tareas está vacía.")
        else:
            eliminar_tarea = tareas_pend.pop()
            print("Tarea eliminada del final de la lista:", eliminar_tarea)

    elif opcion == "3":
        if len(tareas_pend) == 0:
            print("La lista de tareas está vacía.")
        else:
            print("Todas las tareas en orden inverso al que se agregaron:")
            for tarea in reversed(tareas_pend):
                print(tarea)

    elif opcion == "4":
        print("Cantidad total de tareas en la lista:", len(tareas_pend))

    elif opcion == "5":
        print("¡Gracias por la lista de tareas !")
        break

    else:
        print("Opción inválida,Por favor ingresa un número del 1 al 5")