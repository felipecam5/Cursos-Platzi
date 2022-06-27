# import random

# def list_comprenhesion():
#     lista = [random.randint(-100,100) for i in range(10)]
#     print(lista)
#     print([i*2 for i in lista])

# if __name__ == "__main__":
#     list_comprenhesion()
import time

def run():
    squares = []
    for i in range(1,101):
        if i % 3 != 0:
           squares.append(i**2)
    
    print(squares)

    # List comprenhesions que lo resuelve en una linea
    print([i**2 for i in range(0,100) if i % 3 != 0])

    #Reto
    a = time.time()
    print([i for i in range(0,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 and len(str(i)) < 6])
    b = time.time()
    print(b-a)
        


if __name__ =="__main__":
    run()
    