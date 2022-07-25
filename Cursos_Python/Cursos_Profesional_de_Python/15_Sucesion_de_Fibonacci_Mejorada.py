import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1,n2 = n2, aux
            counter += 1
            yield aux


# RETO: GENERADOR PERO HASTA UN MAXIMO DE NUMEROS

def fibo_gen_max(max):
    n1 = 0
    n2 = 1
    counter = 0
    
    while True:
        if counter < max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1,n2 = n2, aux
                counter += 1
                yield aux
        else:
            raise StopIteration

if __name__ =="__main__":

    # fibonacci = fibo_gen()

    # for i in fibonacci:
    #     print(i)
    #     time.sleep(1)

    fibonacci_max = fibo_gen_max(10)

    for i in fibonacci_max:
        print(i)
        time.sleep(0.3)