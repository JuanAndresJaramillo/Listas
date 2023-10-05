import os
import random
import listas

# La función menú principal que interactúa con el usuario
def menu(lista = []):
    os.system("cls")  # Limpia la pantalla de la consola
    print("*************** Parcial de programacion ***************\n\n")
    while True:
        try:
            # Se muestran las opciones y se recoge la elección del usuario
            opcion = int(input("***** Menu principal *****\n" 
                               + "1. Lista aleatoria\n"
                               + "2. Ingresar lista\n"
                               + "3. Cargar lista previamente creada\n"
                               + "4. Crear lista desde rango\n"
                               + "5. Ayuda\n"
                               + "6. Salir\n"
                               + "Seleccione una opcion: "))
            # Validación para asegurar que la opción seleccionada es válida
            if opcion < 1 or opcion > 6:
                raise ValueError  # Provoca una excepción si no es válida
            else:
                break
        except ValueError:
            os.system("cls")
            print("Favor digite un valor valido\n")
            
    # Ejecuta la función correspondiente a la opción seleccionada
    if opcion == 1:
        lista_aleatoria()
    elif opcion == 2:
        lista = instanciar(crear_lista())
        opciones_avanzadas(lista)
    elif opcion == 3:
        opciones_avanzadas(lista)
    elif opcion == 4: 
        lista_manual()
    elif opcion == 5: 
        ayuda()
        menu(lista)
    else:
        exit()  # Sale de la aplicación

# Función para crear una lista de manera manual
def crear_lista():
    os.system("cls")
    while True:
        print("******************** Crea tu lista ********************\n\n")
        try:
            lista = []
            tamano = int(input("Ingresa el tamaño de tu lista: "))  # Toma el tamaño de la lista
            for i in range(tamano):
                # Solicita al usuario ingresar cada elemento de la lista
                elemento = int(input(f"Ingresa el elemento {i} de tu lista: "))
                lista.append(elemento)
            break
        except ValueError:
            os.system("cls")
            print("Favor digite valores validos")
    return lista

# Función para instanciar un objeto de la clase ListaEstadistica con la lista dada
def instanciar(lista):
    mi_lista = listas.ListaEstadistica()  # Crea una nueva instancia de ListaEstadistica
    mi_lista.lista = lista  # Asigna la lista a la instancia
    # Muestra los primeros 10 elementos de la lista
    if len(mi_lista.lista)>10:
        print(f"\n Lista creada exitosamente (los diez primeros digitos son): {mi_lista.lista[:10]}")
    else:
        print(f"\n lista creada exitosamente: {mi_lista.lista}")
    input("\nPresione enter para continuar.")
    return mi_lista

# Función para mostrar la ayuda al usuario
def ayuda():
    os.system("cls")
    print("******************  Ayuda  ******************\n"
          + "* La busqueda lineal recorre la lista de principio a fin hasta encontrar el elemento.\n"
          + "* La busqueda binaria requiere que la lista este ordenada y encuentra el elemento dividiendo la lista en mitades.\n"
          + "* El ordenamiento por burbuja compara pares de elementos adyacentes y los intercambia si estan en orden incorrecto.\n"
          + "* ordenamiento rapido utiliza un elemento 'pivote' para dividir la lista y ordenarla de marena mas eficiente\n\n")
    input("Presione enter para continuar.")
    
# Función para crear una lista de manera aleatoria
def lista_aleatoria():
    os.system("cls")
    print("************ Lista aleatoria ************\n")
    while True:
        try:
            tamano = int(input("Ingrese el tamaño de la lista: "))  # Toma el tamaño de la lista
            break
        except ValueError:
            os.system("cls")
            print("Favor ingresar un valor valido")
    mi_lista = listas.ListaEstadistica()
    # Genera una lista de enteros aleatorios
    lista_aleatoria = [random.randint(0,100000) for _ in range(tamano)]
    mi_lista.lista = lista_aleatoria  # Asigna la lista generada a la instancia
    # Muestra los primeros 10 elementos de la lista
    if len(mi_lista.lista)>10:
        print(f"\n Lista creada exitosamente (los diez primeros digitos son): {mi_lista.lista[:10]}")
    else:
        print(f"\n lista creada exitosamente: {mi_lista.lista}")
    input("\nPresione enter para continuar.")
    opciones_avanzadas(mi_lista)
    
# Función para crear una lista manualmente a partir de un rango
def lista_manual():
    os.system("cls")
    print("************ Lista desde rango ************\n")
    while True:
        try:
            # Toma el rango inicial, el rango final y el tamaño de la lista
            rango_inicial = int(input("Ingrese el rango inicial de la lista: "))
            rango_final = int(input("Ingrese el rango final de la lista: "))
            tamano = int(input("Ingrese el tamaño de la lista: "))
            # Validación de la entrada
            if tamano < 0: 
                raise ValueError
            if rango_final <=  rango_inicial: 
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("Favor ingresar valores validos.")
    mi_lista = listas.ListaEstadistica()
    # Genera una lista de enteros aleatorios en el rango dado
    lista_aleatoria = [random.randint(rango_inicial,rango_final) for _ in range(tamano)]
    mi_lista.lista = lista_aleatoria  # Asigna la lista generada a la instancia
    # Muestra los primeros 10 elementos de la lista
    if len(mi_lista.lista)>10:
        print(f"\n Lista creada exitosamente (los diez primeros digitos son): {mi_lista.lista[:10]}")
    else:
        print(f"\n lista creada exitosamente: {mi_lista.lista}")
    input("\nPresione enter para continuar.")
    opciones_avanzadas(mi_lista)
    
# Función para manejar las opciones avanzadas del menú
def opciones_avanzadas(lista):
    os.system("cls")
    while True:
        try:
            # Se muestran las opciones avanzadas y se recoge la elección del usuario
            opcion=int(input("************** Opciones avanzadas **************\n\n"
                    + "1. Imprimir lista.\n"
                    + "2. Ordenar con burbuja.\n"
                    + "3. Ordenar con Rapido.\n"
                    + "4. Comparar con sorted()\n"
                    + "5. Buscar elemento (busqueda lineal)\n"
                    + "6. Buscar elemento (busqueda binaria)\n"
                    + "7. Sumar elementos\n"
                    + "8. Calcular promedio\n"
                    + "9. Calcular mediana\n"
                    + "10. Calcular varianza\n"
                    + "11. Encontrar el minimo\n"
                    + "12. Encontrar el maximo\n"
                    + "13. Mostrar longitud de la lista\n"
                    + "14. Comparar con otra lista\n"
                    + "15. volver al menu principal\n"
                    + "Seleccione una opcion: "))
            # Validación para asegurar que la opción seleccionada es válida
            if opcion < 1 or opcion > 15: 
                raise ValueError
            else: 
                break
        except ValueError:
            os.system("cls")
            print("Favor digite una opcion valida\n\n")
    
    # Ejecuta la opción seleccionada
    if opcion == 1: 
        os.system("cls")
        print(f"Tu lista es : {lista.lista}")  # Imprime la lista actual
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 2:
        os.system("cls")
        # Ordena la lista usando el método burbuja e imprime los primeros 10 elementos
        print(f"Tu lista ordenada es (primeros 10 elementos): {lista.ordenar_burbuja()[:10]}\nTiempo de ejecucion: {lista.tiempo_burbuja}")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 3:
        os.system("cls")
        # Ordena la lista usando el método pivote e imprime los primeros 10 elementos
        print(f"Tu lista ordenada es (primeros 10 elementos): {lista.ordenar_pivote(lista.lista)[:10]}\nTiempo de ejecucion: {lista.tiempo_pivote}")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 4:
        os.system("cls")
        # Ordena la lista usando diferentes métodos e imprime el tiempo de ejecución
        lista.ordenar_burbuja()[:10]
        lista.lista[:10]
        lista.ordenar_pivote(lista.lista)[:10]
        print(f"*************** Comparacion de metodos de ordenamiento con sorted ***************\nMetodo de burbuja:{lista.tiempo_burbuja}\nMetodo pivote: {lista.tiempo_pivote}\nMetodo sorted: {lista.tiempo_sorted}")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 5:
        os.system("cls")
        while True:
            print("************ Busqueda lineal ************")
            try: 
                # Obtiene el elemento a buscar y realiza la búsqueda lineal
                elemento_a_buscar = int(input("Favor Digite el elemento que decea buscar en la lista: "))
                break
            except ValueError:
                os.system("cls")
                print("Favor digite un elemento valido. \n\n")
        print(f"{lista.busqueda_lineal(elemento_a_buscar)}\n\nSu tiempo de ejecucion fue: {lista.tiempo_busqueda_lineal}")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 6:
        os.system("cls")
        while True:
            print("************ Busqueda lineal ************")
            try: 
                # Obtiene el elemento a buscar y realiza la búsqueda binaria
                elemento_a_buscar = int(input("Favor Digite el elemento que decea buscar en la lista: "))
                break
            except ValueError:
                os.system("cls")
                print("Favor digite un elemento valido. \n\n")
        print(f"{lista.busqueda_binaria(elemento_a_buscar)}\n\nSu tiempo de ejecucion fue: {lista.tiempo_busqueda_binaria}")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 7:
        os.system("cls")
        # Calcula y muestra la sumatoria de los elementos de la lista
        print(f"La sumatoria de la lista es: {lista.sumatoria()}\n\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 8:
        os.system("cls")
        # Calcula y muestra el promedio de los elementos de la lista
        print(f"El promedio de la lista es: {lista.promedio()}\n\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 9:
        os.system("cls")
        # Calcula y muestra la mediana de los elementos de la lista
        print(f"La mediana de tu lista es: {listas.Estadistica.mediana(lista.lista[:])}\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 10:
        os.system("cls")
        # Calcula y muestra la varianza de los elementos de la lista
        print(f"La varianza de tu lista es: {listas.Estadistica.varianza(lista.lista[:])}\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 11:
        os.system("cls")
        # Encuentra y muestra el valor mínimo de los elementos de la lista
        print(f"El valor minimo de tu lista es: {lista.minimo()}\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 12:
        os.system("cls")
        # Encuentra y muestra el valor máximo de los elementos de la lista
        print(f"El valor maximo de tu lista es: {lista.maximo()}\n")
        input("Presione enter para continuar")
        opciones_avanzadas(lista)
    elif opcion == 13:
        os.system("cls")
        # Muestra la longitud de la lista
        print(f"La longitud de tu lista es: {lista.longitud()}\n")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 14:
        os.system("cls")
        # Permite comparar la lista actual con otra lista
        lista_para_comparar = crear_lista()
        if lista_para_comparar == lista.lista[:]:
            print("Las listas son completamente iguales.")
        else:
            print("Las listas son diferentes")
        input("Presione enter para continuar.")
        opciones_avanzadas(lista)
    elif opcion == 15:
        menu(lista)  # Vuelve al menú principal

# Entrypoint
if __name__  == '__main__' :
    menu()
        