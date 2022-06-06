def run():
    LIMITE = 1000

    contador = 0 
    potencia = 2**contador
    while potencia <= LIMITE:
        print(potencia)
        contador +=1
        potencia = 2**contador

if __name__ == "__main__":
    
    run()