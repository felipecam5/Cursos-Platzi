from functools import reduce
from typing import List


def is_palindrome(palabra: str) -> bool:
    print()
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def run():
    print(is_palindrome(1000))

# RETO: Crear un programa que verifique si un número es primo o no, pero hazlo con tipado estatico.

def is_primo(numero: int) -> bool:
    contador = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
            if contador > 2:
                return False
    return True

def is_primo2(numero: int) -> bool:
    contador_list: list[int] = []
    contador_list = [1 for x in range(1, numero + 1) if numero % x ==0]
    contador_list = reduce(lambda x,y: x+y, contador_list)
    if contador_list > 2:
        return False
    else:
        return True
    
        
def run2():
    # print(is_primo(18))
    print(is_primo2(19))

if __name__ == "__main__":
    # run()
    run2()
