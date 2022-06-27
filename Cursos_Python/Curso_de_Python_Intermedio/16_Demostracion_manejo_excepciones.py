# Resolviendo la excepción en la clase

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Solo se admiten valores de tipo numerico")

# RETO: Utilizar las palabras clave "TRY", "EXCEPT" Y "RAISE" para elevar un error si el usuario ingresa un número negativo en nuestro programa de divisores.

def run2():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise TypeError("Solo se admiten numeros positivos")
        print(divisors(num))
        print("Terminó mi programa")
    except TypeError as ve:
        print(ve)
    except ValueError:
        print("Solo se admiten valores de tipo numerico")


if __name__ == "__main__":
    run(), run2()