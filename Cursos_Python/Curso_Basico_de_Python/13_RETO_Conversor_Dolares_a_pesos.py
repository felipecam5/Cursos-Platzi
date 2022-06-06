dolares = input("Indique cuantos dolares tiene en la cuenta ")
dolares = float(dolares)
valor_dolar =  3976.51
pesos = valor_dolar*dolares
pesos = round(pesos,2)
print("Usted tiene en su cuenta $" + str(pesos) + " pesos colombianos")
