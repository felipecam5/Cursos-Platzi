def edad():
    nombre_usuario1 = input("Por favor, indicame cual es tu nombre: ")
    edad_usuario1 = int(input("Por favor, indicame cual es tu edad: "))
    nombre_usuario2 = input("Por favor, indicame cual es el nombre de tu compañero: ")
    edad_usuario2 = int(input("Por favor, indicame cual es la edad de tu compañero: "))

    if (edad_usuario1 < edad_usuario2):
        print(f'{nombre_usuario2} es mayor con {str(edad_usuario2)} años')
    elif (edad_usuario1 > edad_usuario2):
        print(f'{nombre_usuario1} es mayor con {str(edad_usuario1)} años')
    else:
        print(f'{nombre_usuario1} y {nombre_usuario2} tiene la misma edad ({edad_usuario1} años)')


if __name__ == "__main__":
    edad()