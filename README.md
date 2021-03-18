Mario map-John_Torrico
========

## Planteamiento del problema

Encontrar la manera en la que Mario pueda llegar a uno de sus objetivos, el cual es entrar en una de las 2 tuberias que se plantean en el enunciado.

Figure 1: Mapa de Mario (Practica 2-Sistemas Inteligentes.pdf)


## Formulacion del objetivo

Usar una estructura de control adecuada para resolver la problemática de Mario de manera eficiente con un camino óptimo.


## Formulacion del problema

**Estado Inicial**       
    -Mario en cualquier casilla disponible

**Acciones**
    *Mover a la derecha
    *Mover a la izquierda
    *Mover hacia abajo
    *Mover hacia arriba
    
**Modelo de transición**
    *Intercambio de la posición de Mario con una casilla vacia
    
**Test del objetivo**

    (Segunda figura [Practica 2-Sistemas Inteligentes.pdf])

**Costo**

    ==BFS==

    - Solución óptima en este codigo.
        *3 pasos
        *9 iteraciones

    - Solución no óptima en este codigo.
        *5 pasos
        *31 iteraciones


## Como hacer funcionar el codigo

**Instalaciones**

- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [Visual code](https://code.visualstudio.com/download)

Nota: Visual Code no es completamente necesario, si se quiere se puede utilizar otro editor de codigo que usted elija.

**Pasos para hacer correr el codigo**

Una vez conseguido el codigo hacer lo siguiente:

    *Abrir una terminal con la siguiente ruta como ejemplo: "C:\Users\PC\Desktop\Sistemas Inteligentes\mario-map-john" (Sin las comillas)
    *En la terminal escribir la siguiente linea: "py main.py" (Sin las comillas)
    


