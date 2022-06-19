#Modulo necesario para hacer mediciones de tiempo

import time

#Modulo necesario para revisar y reasignar el limite de recursividad
import sys

#Asignación del limite de recursividad
sys.setrecursionlimit(1000000)


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n-1)

if __name__ == "__main__":

    #Imprime el limite de recursividad actual
    print(sys.getrecursionlimit())

    n = 2000

    #Crea una variable de tiempo (Comienzo), llamando el metodo time del modulo time.
    comienzo = time.time()
    factorial(n)
    #Crea una variable de tiempo (Final)
    final = time.time()
    #Returna el tiempo requerido en el proceso
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)

