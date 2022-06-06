menu = """
Bienvenido al conversor de monedas 💲

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Bolivarianos

Elige una opción: """
opcion = int(input(menu))

conversion_peso_colombiano = 3703.703
conversion_peso_mexicano = 19.607
conversion_peso_bolivariano = 5 
dolares = 0

if(opcion == 1):
    dolares = float(input("Por favor, ingrese la cantidad de Pesos Colombianos a convertir a Dolares: "))
    print("La cantidad de Dolares que usted tiene es de: " + "$" + str(round((dolares/conversion_peso_colombiano),3)))
elif(opcion == 2):
    dolares = float(input("Por favor, ingrese la cantidad de Pesos Mexicanos a convertir a Dolares: "))
    print("La cantidad de Dolares que usted tiene es de: " + "$" + str(round((dolares/conversion_peso_mexicano),3)))
elif(opcion == 3):
    dolares = float(input("Por favor, ingrese la cantidad de Pesos Bolivarianos a convertir a Dolares: "))
    print("La cantidad de Dolares que usted tiene es de: " + "$" + str(round((dolares/conversion_peso_bolivariano),3)))
else:
    print("No existe la opción seleccionada")

