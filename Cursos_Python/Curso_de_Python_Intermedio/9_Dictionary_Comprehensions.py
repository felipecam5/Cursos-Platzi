#Genera diccionarios sin ciclos.

# RETO: Diccionario con llaves de los 100 primeros valores naturales y sus valores, estos valores al cubo.
import math

def main():
    my_dictionary = {}

    for i in range(0,101):
        if i % 3 != 0:
           my_dictionary[i] = i ** 3
    print(my_dictionary) 

# Dictionary Comprehension
def comprehension_dict():
    my_dictionary = {i: i ** 3 for i in range(0, 101) if i % 3 != 0}
    print(my_dictionary)

# RETO FINAL: Crear, con un dictionary comprehension, un diccionario cuyas llaves sean los 1000 primeros numero naturales con sus raices cuadradas como valores

def dict_reto():
    my_dict = {i: math.sqrt(i) for i in range(0,1001) }
    print(my_dict)
    


if __name__ =="__main__":
    main()
    comprehension_dict()
    dict_reto()
    