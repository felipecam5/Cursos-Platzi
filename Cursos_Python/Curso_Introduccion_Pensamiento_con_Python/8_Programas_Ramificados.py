def operacion():
    num_1 = int(input("Por favor, escoge un entero: "))
    num_2 = int(input("Por favor, escoge otro entero: "))

    if num_1 < num_2:
        print("El numero " + str(num_1) + " es menor que el numero " + str(num_2))
    elif num_1 > num_2:
        print("El numero " + str(num_1) + " es mayor que el numero " + str(num_2))
    else:
        print("Los numeros son iguales")



if __name__ == "__main__":
    operacion()