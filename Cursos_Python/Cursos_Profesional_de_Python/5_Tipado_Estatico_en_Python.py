# Static Typing >> Convirtiendo a Python en un lenguaje de tipado estatico.

#Link: https://www.section.io/engineering-education/python-static-typing/

import random
from typing import Dict

a: int = 5

b: str = "Hola Mundo"

c: bool = True

print(f'Las opciones que usted tiene son: {a}, {b}, {c}')

# Static Typing en funciones

def suma(a: int, b: int) -> int:
    return a+b

print(suma(2,5))
print(suma("2", "5")) ##Aún no funciona, deberia tirar error pero python los concadena.

# Static Typing en listas:
# numbers: List[int] = [] informs the type checker that numbers is a list if integers. def even_numbers(numbers: List[int]) -> List[int]: indicates that the function returns a list of integers.

numbers: list[int] = []

def even_numbers(numbers: list[int]) -> list[int]:
    numbers = [number for number in numbers if number % 2 == 0]
    return numbers

print(even_numbers(range(0,100)))

# Static Typing en Diccionarios:

users: Dict[str, int] = {
    "Argentina": 2001,
    "Colombia" : 2004
}

# Static Typing en Listas de Diccionarios:

countries: list[Dict[str, str]] = [
    {
        "name" : "Felipe"
    },
    {
        "name" : "Mapss"
    }

]

# Ejemplo Complejo:

CoordinatesType = list[Dict[str, tuple[int, int]]]
Coordinates: CoordinatesType = [

    {
        "coor1" : (4,5),
        "coor2" : (10,5)
    }
]

for i in Coordinates:
    for key,value in i.items():
        print(key,value)
