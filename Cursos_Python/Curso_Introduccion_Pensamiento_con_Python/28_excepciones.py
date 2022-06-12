lista = list(range(10))
divisor = 0

def divide_elementos_de_lista(lista, divisor):
    try:
        resultado = [i/divisor for i in lista]
        return(resultado)
    except ZeroDivisionError as e:
        print(e)
        return lista
    #ó
    # for i in lista:
    #     print(i/divisor)

    

if __name__ == "__main__":
    print(divide_elementos_de_lista(lista, divisor))