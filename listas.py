# Importando las bibliotecas necesarias
import time
import statistics
import numpy as np

# Definición de la clase Lista
class Lista:
    # Método constructor de la clase
    def __init__(self):
        # Inicializamos la lista interna como una lista vacía
        self.__lista_ = [] 
    
    @property
    def lista(self):
        # Método getter para obtener la lista interna
        return self.__lista_
    
    @lista.setter
    def lista(self, nueva_lista):
        # Método setter para establecer la lista interna
        self.__lista_ = nueva_lista
        
    def __str__(self):
        # Método para representar la lista como una cadena de texto
        return str(self.lista)
        
# Definición de la clase ListaTiempos que hereda de Lista
class ListaTiempos(Lista):
    def __init__(self):
        # Método constructor de la clase
        # Inicializamos las variables de tiempo para diferentes operaciones
        self._tiempo_burbuja = 0
        self._tiempo_pivote = 0
        self._tiempo_sorted = 0
        self._tiempo_lineal = 0
        self._tiempo_binario = 0
        
    @property
    def tiempo_busqueda_lineal(self):
        # Método getter para obtener el tiempo de búsqueda lineal
        return self._tiempo_lineal
    
    @tiempo_busqueda_lineal.setter
    def tiempo_busqueda_lineal(self, tiempo):
        # Método setter para establecer el tiempo de búsqueda lineal
        self._tiempo_lineal = tiempo
        
    @property
    def tiempo_busqueda_binaria(self):
        # Método getter para obtener el tiempo de búsqueda binaria
        return self._tiempo_binario
    
    @tiempo_busqueda_lineal.setter
    def tiempo_busqueda_binario(self, tiempo):
        # Método setter para establecer el tiempo de búsqueda binaria
        self._tiempo_binario = tiempo
        
    @property
    def tiempo_pivote(self):
        # Método getter para obtener el tiempo de ordenamiento por pivote
        return self._tiempo_pivote 
    
    @tiempo_pivote.setter
    def tiempo_pivote(self, tiempo):
        # Método setter para establecer el tiempo de ordenamiento por pivote
        self._tiempo_pivote = tiempo
    
    @property
    def tiempo_burbuja(self):
        # Método getter para obtener el tiempo de ordenamiento de burbuja
        return self._tiempo_burbuja
    
    @tiempo_burbuja.setter
    def tiempo_burbuja(self, tiempo):
        # Método setter para establecer el tiempo de ordenamiento de burbuja
        self._tiempo_burbuja = tiempo
    
    @property
    def tiempo_sorted(self):
        # Propiedad calculada que devuelve el tiempo que tarda en ordenar la lista con la función sorted
        inicial = time.time()
        sorted(self.lista[:])
        final = time.time()
        return final - inicial
    
    def ordenar_burbuja(self):
        # Método para ordenar la lista usando el algoritmo de burbuja
        # Hacemos una copia de la lista original para no modificarla
        lista = self.lista[:]
        inicio = time.time()  # Marcamos el tiempo de inicio
        tamano = len(lista)
        for i in range(tamano):
            for j in range(0, tamano - i - 1):
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        final = time.time()  # Marcamos el tiempo de finalización
        self._tiempo_burbuja = final - inicio  # Calculamos el tiempo total
        return lista  # Devolvemos la lista ordenada
        
    def ordenar_pivote(self, lista=None):
        # Método para ordenar la lista usando el algoritmo de quicksort (ordenamiento por pivote)
        # Si no se proporciona una lista, usamos la lista interna
        if lista is None:
            lista = self.lista[:]
        # Si la lista es de tamaño 1 o menor, ya está ordenada
        if len(lista) <= 1:
            return lista
        inicio = time.time()  # Marcamos el tiempo de inicio
        # Elegimos un elemento pivote (en este caso, el elemento del medio)
        pivote = lista[len(lista) // 2]
        menores, iguales, mayores = [], [], []

        # Dividimos la lista en tres partes: menores que el pivote, iguales al pivote y mayores que el pivote
        for elemento in lista:
            if elemento < pivote:
                menores.append(elemento)
            elif elemento == pivote:
                iguales.append(elemento)
            else:
                mayores.append(elemento)
        # Recursivamente ordenamos las partes menores y mayores y concatenamos las tres partes
        lista_ordenada = self.ordenar_pivote(menores) + iguales + self.ordenar_pivote(mayores)
        final = time.time()  # Marcamos el tiempo de finalización
        self.tiempo_pivote = final - inicio  # Calculamos el tiempo total
        return lista_ordenada  # Devolvemos la lista ordenada
    
    def busqueda_lineal(self, elemento_a_buscar):
        # Método para buscar un elemento en la lista usando búsqueda lineal
        inicial = time.time()  # Marcamos el tiempo de inicio
        indice = None  # Inicializamos el índice del elemento encontrado como None
        for i in range(len(self.lista[:])):
            if self.lista[i] == elemento_a_buscar:
                # Si encontramos el elemento, guardamos su índice y salimos del bucle
                indice = i
                break
        final = time.time()  # Marcamos el tiempo de finalización
        self.tiempo_busqueda_lineal = final - inicial  # Calculamos el tiempo total
        # Si encontramos el elemento, devolvemos su índice, de lo contrario, indicamos que no se encontró
        if indice is not None:
            return f"El elemento se encuentra en el índice: {indice}"
        else:
            return f"El elemento {elemento_a_buscar} no se encuentra en la lista"
        
    def busqueda_binaria(self, elemento_a_buscar):
        # Método para buscar un elemento en la lista usando búsqueda binaria
        inicial = time.time()  # Marcamos el tiempo de inicio
        lista = sorted(self.lista[:])  # Ordenamos la lista antes de buscar
        izquierda, derecha = 0, len(lista) - 1  # Inicializamos los punteros izquierdo y derecho
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if lista[medio] == elemento_a_buscar:
                # Si encontramos el elemento, salimos del bucle
                final = time.time()
                self._tiempo_binario = final - inicial  # Calculamos el tiempo total
                return f"El elemento se encuentra en el índice: {medio}"
            elif lista[medio] > elemento_a_buscar:
                # Si el elemento del medio es mayor que el elemento a buscar,
                # ajustamos el puntero derecho para buscar en la mitad izquierda
                derecha = medio - 1
            else:
                # Si el elemento del medio es menor que el elemento a buscar,
                # ajustamos el puntero izquierdo para buscar en la mitad derecha
                izquierda = medio + 1
        final = time.time()
        self._tiempo_binario = final - inicial  # Calculamos el tiempo total
        # Si no encontramos el elemento, indicamos que no se encontró
        return f"El elemento {elemento_a_buscar} no se encuentra en la lista"
    
# Definición de la clase Estadistica
class Estadistica:
    
    @classmethod
    def mediana(cls, lista):
        # Método de clase para calcular la mediana de una lista
        return statistics.median(lista)
    
    @classmethod
    def varianza(cls, lista):
        # Método de clase para calcular la varianza de una lista
        return np.var(lista)

# Definición de la clase ListaEstadistica que hereda de Estadistica y ListaTiempos
class ListaEstadistica(Estadistica, ListaTiempos):
    def sumatoria(self):
        # Método para calcular la sumatoria de los elementos de la lista
        sumatoria = 0
        for i in self.lista:
            sumatoria += i
        return sumatoria
    
    def promedio(self):
        # Método para calcular el promedio de los elementos de la lista
        return statistics.mean(self.lista[:])
    
    def minimo(self):
        # Método para encontrar el valor mínimo de la lista
        valor_minimo = float('inf')  # Inicializamos el valor mínimo como infinito
        for i in self.lista:
            if i < valor_minimo:
                valor_minimo = i
        return valor_minimo

    def maximo(self):
        # Método para encontrar el valor máximo de la lista
        valor_maximo = float('-inf')  # Inicializamos el valor máximo como menos infinito
        for i in self.lista:
            if i > valor_maximo:
                valor_maximo = i
        return valor_maximo
    
    def longitud(self):
        # Método para calcular la longitud de la lista
        contador = 0
        for i in self.lista:
            contador += 1
        return contador
    

    