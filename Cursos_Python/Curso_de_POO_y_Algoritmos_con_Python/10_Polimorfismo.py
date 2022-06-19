class Persona:
    
    def __init__(self,  nombre):
        self.nombre = nombre

    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    #Basicamente, en el polimorfismo, se redifen algunos metodos para las subclases.
     
    def avanza(self):
        print("Ando moviendome en mi bicicleta")

#Clases con varias extensiones que tienen metodos con el mismo nombre
class Terrestre:

    def desplazar(self):
        print('El animal anda')


class Acuatico:

    def desplazar(self):
        print('El animal nada')


class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """

def main():
    persona1 = Persona("Felipe")
    persona1.avanza()
    
    ciclista1 = Ciclista("Maria Paula")
    ciclista1.avanza()
if __name__ == "__main__":
    main()

