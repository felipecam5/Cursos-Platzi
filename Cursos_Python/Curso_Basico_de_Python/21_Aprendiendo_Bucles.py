# numero = 2
# contador =0 

# while contador <= 10:
#     print(numero **contador)
#     contador += 1


def potencias():
    numero = int(input("Por favor, ingrese el numero: "))
    potencia = int(input("Por favor, ingrese hasta que potencia quiere calcular: "))
    contador = 0
    while contador <= potencia:
        print("La potencia " + str(contador) + " del numero " + str(numero) + " es " + str(numero**contador))
        contador +=1


if __name__ == "__main__":
    potencias()

#Solución Platzi

# def potencia(numero):
    
#     potencia = 1

#     while (potencia <= 10):
        
#         result = numero ** potencia
#         print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
#         potencia += 1
        

# def run():
#     numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
#     potencia(numero)


# if __name__ == "__main__":
#     run()

