class EvenNumbers:

    """ Clase que implementa un iterador de todos los numeros pares, o los números pares hasta un maximo 
    """
    # Constructor, con primer parametro "self", y segundo "max" que es hasta que numero quiero imprimir los numeros pares.

    def __init__(self, max = None):
        self.max = max

    # Metodo iter: Tener el atributo de cada uno de los numeros de la iteración. Se retorna al final el objeto. Convierte un iterable en un iterador.

    def __iter__(self):
        self.num = 0
        return self

    # Metodo next: Permite extraer cada uno de los elementos del iterador.

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2 
            return result
        else:
            raise StopIteration

if __name__ =="__main__":
    Pares = EvenNumbers(100)
    print([i for i in Pares])