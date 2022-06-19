import random

def ordenamiento_por_insercion(lista):
    n = len(lista)
    
    for i in range(1,n):
        indice = i
        valor_actual = lista[indice]

        while indice > 0 and lista[indice - 1] > valor_actual:
            lista[indice] = lista[indice-1]
            lista[indice -1] = valor_actual
            indice -=1
            print(lista)



    print(lista)

if __name__ =="__main__":

    longitud_lista = int(input("Por favor, indique la longitud de la lista"))
    lista = [random.randint(0,100) for i in range(longitud_lista)]

    ordenamiento_por_insercion(lista)