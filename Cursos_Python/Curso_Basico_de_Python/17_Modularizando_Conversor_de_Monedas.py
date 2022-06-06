def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💲

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Bolivarianos

Elige una opción: """
opcion = int(input(menu))

if(opcion == 1):
    conversor("Colombianos", 3703.703)
elif(opcion == 2):
    conversor("Mexicanos", 19.607)
elif(opcion == 3):
    conversor("Bolivarianos", 5)
else:
    print("No existe la opción seleccionada")