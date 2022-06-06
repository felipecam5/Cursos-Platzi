pesos = input("Ingrese la cantidad de dinero en pesos colombianos ")
conversion = float(pesos)
valor_dolar =  3976.51
dolares = conversion/valor_dolar
dolares = round(dolares,2)
print ("Usted tiene $" + str(dolares) + " dolares")