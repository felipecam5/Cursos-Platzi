from functools import reduce
import random
# Estructura FILTER
# filter(<función filtro (anonima)>, <lista iterable>)


def funcion_filter():
    my_list = list(random.randint(0,100) for i in range(0,20))
    print(my_list)

    odd = list(filter(lambda x: x %2 != 0, my_list))
    print(odd)

# RETO: Simular la función Map pero con list comprehensions

def elevado_cuadrado():
    my_list = list(random.randint(0,100) for i in range(0,5))
    print(my_list)

    squares = list(i**2 for i in my_list)
    print(squares)

# Estructura MAP
# map(<función Mapeadora (anonima)>, <lista iterable>)

def funcion_map():
    my_list = list(random.randint(0,100) for i in range(0,5))
    print(my_list)

    squares = list(map(lambda x: x**2, my_list))
    print(squares)

# Estructura Reduce
# reduce (<funcion filtro>, <iterable>)

def funcion_reduce():
    my_list = list(random.randint(0,100) for i in range(0,5))
    print(my_list)

    sumatoria = reduce(lambda x,y:x+y, my_list)
    print(sumatoria)

if __name__ == "__main__":
    funcion_filter()
    elevado_cuadrado()
    funcion_map()
    funcion_reduce()