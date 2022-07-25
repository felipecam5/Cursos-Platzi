# [1, 1, 2, 2, 4] -> [1, 2, 4]

from random import randint, random


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = list(input("Ingrese la lista"))
    print(f' La lista original es {random_list} \n')
    print(f' La lista sin duplicados es {remove_duplicates(random_list)}')

# RETO: Crear un programa que elimine los elementos repetidos de una lista pero en lugar de utilizar un ciclo for, utiliza sets.

def remove_duplicates_sets(list):
    set_without_duplicate = set(list)
    return set_without_duplicate

def run2():
    lista = [randint(0, 10) for i in range(0, 10)]
    print(f' La lista original es: {lista} \n')
    print(f' El set resultante es: {remove_duplicates_sets(lista)}')



if __name__ == "__main__":
    # run()
    run2()
