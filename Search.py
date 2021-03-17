from copy import deepcopy
from time import time
import sys

def getHijos(nodo, estados):
    return estados.get(nodo)


def busqueda_profundidad(inicial, objetivo, estados):
    inicio_tiempo = time()
    frontera = [[inicial]]
    tam = 0
    cont = 0
    while frontera:
        tam = max(sys.getsizeof(frontera), tam)
        cont += 1
        camino = frontera.pop()
        nodo = camino[-1]
        if nodo == objetivo:
            fin_tiempo = time() - inicio_tiempo
            print("Algoritmo tardo: %0.10f segundos." % fin_tiempo)
            print("Maximo tamaño de frontera: ", tam, " bytes")
            print("Se preciso de ", cont, " iteraciones para encontrar la solucion")
            print("la solución tiene ", len(camino), " pasos")
            return(camino)
        else:
            for h in getHijos(nodo, estados):
                aux = deepcopy(camino)
                aux.append(h)
                frontera.append(aux)

def busqueda_amplitud(inicial, objetivo, estados):
    inicio_tiempo = time()
    stack = [[inicial]]
    tam = 0
    cont = 0
    while stack:
        tam = max(sys.getsizeof(stack), tam)
        cont += 1
        camino = stack.pop(0)
        nodo = camino[-1]
        if nodo == objetivo:
            fin_tiempo = time() - inicio_tiempo
            print("Algoritmo tardo: %0.10f segundos." % fin_tiempo)
            print("Maximo tamaño de del stack: ", tam, " bytes")
            print("Se preciso de ", cont, " iteraciones para encontrar la solucion")
            print("la solución tiene ", len(camino), " pasos")
<<<<<<< Updated upstream
            return(cont)
=======
            return(len(camino)-1)
>>>>>>> Stashed changes
        else:
            for h in getHijos(nodo, estados):
                aux = deepcopy(camino)
                aux.append(h)
<<<<<<< Updated upstream
                stack.append(aux)
=======
                stack.append(aux) 
>>>>>>> Stashed changes
