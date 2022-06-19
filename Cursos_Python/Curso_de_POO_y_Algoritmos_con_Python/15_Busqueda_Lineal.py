import random

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ =="__main__":
    tamano_de_lista = int(input("De que tamano será la lista"))
    objetivo = int(input("Que numero quieres encontrar"))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]; #Crea una lista del tamaño del input y la llena con valores random
 
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no esta"} en la lista'); #Revisa directamente en un print una condición if