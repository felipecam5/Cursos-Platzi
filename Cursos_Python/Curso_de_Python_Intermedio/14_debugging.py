# Función que retorna en una lista los divisores enteros de un numero.

def divisors_pipe(numero):
    divisores = []
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
    print(divisores)
        
# Función que retorna en una lista los divisores enteros de un numero, utilizando LIST COMPREHENSIONS

def divisores_list(numero):
    divisores = list(i for i in range(1, numero + 1) if numero % i == 0)
    print(divisores)

#Función de la clase

def divisors(num):
    divisores = []
    for i in range(1,num+1):
        if num % i == 1: #EL "1" está puesto mal a proposito
            divisores.append(i)
    return(divisores)



def run():
    numero = int(input("Por favor, indique el numero al cual quiere conocer sus divisores enteros: "))
    print(divisors(numero))
    print("Terminó mi programa")

if __name__ == "__main__":
    run()