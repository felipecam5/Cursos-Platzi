from operator import index, indexOf
import random
import sys
sys.setrecursionlimit(10000000)

def ordenamiento_burbuja(lista,longitud):
    # len = longitud
    # print(lista)

    # for elemento in lista:
    #     for arreglo in lista:10
    #         if elemento == arreglo:
    #             print(elemento, arreglo, "Es igual")
    #         elif elemento < arreglo:
    #             print(elemento, arreglo, "Es menor")
    #         else:
    #             if indexOf(lista,elemento)<=len or indexOf(lista,elemento)==0  :
    #                 print(elemento, arreglo, "Es mayor xds")
    #                 lista[indexOf(lista,elemento)] = arreglo
    #                 lista[indexOf(lista,arreglo)] = elemento       
                                
    # print(lista)
    print(lista)
    variable_temporal = 0
    
    for elemento in lista:
        if indexOf(lista, elemento) < len(lista) - 1 and lista != sorted(lista): 
            if elemento >= lista[indexOf(lista, elemento) + 1] and lista != sorted(lista):
                variable_temporal = lista[indexOf(lista, elemento) + 1]
                lista[indexOf(lista, elemento) + 1] = elemento
                lista[indexOf(lista, elemento)] = variable_temporal
                ordenamiento_burbuja(lista, longitud)                               
                        
    print(lista)
    
if __name__ == "__main__":
    
    longitud = int(input("Por favor, indique la longitud de la lista"))
    lista = [random.randint(0,100) for i in range(longitud)]

    ordenamiento_burbuja(lista, longitud)