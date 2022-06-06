def primalidad():
    contador = 0
    numero = int(input("Por favor, introduzca el numero del cual quiere saber si es primo o no"))
    for i in range(1,numero+1):
        if (numero == 1):
            print("El numero 1 no es primo")
            break
        elif(numero % i == 0):
            contador +=1
            print(contador)
            if(i == numero):

                if(contador >=3):
                    print("El numero " + str(numero) + " no es primo ")
                else:
                    print("El numero " + str(numero) + " es primo ")
                      
      

if __name__ == "__main__":
    primalidad()