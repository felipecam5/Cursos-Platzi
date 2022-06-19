#CREACIÓN DE LA CLASE

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    #CREACIÓN DEL METODO QUE CALCULA EL AREA

    def area(self):
        return self.base * self.altura

#CREACION DE LA CLASE "Cuadrado" extendida a la clase "Rectangulo". De manera, que Cuadrado hereda la definición y metodos de rectangulo.

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        #super()> permite obtener una referencia directa de la superclase, para llamar a su constructor.
        super().__init__(lado, lado)

if __name__ =="__main__":
    
    rectangulo1 = Rectangulo(40,25)
    print(rectangulo1.area())

    cuadrado1 = Cuadrado(5)
    print(cuadrado1.area())


#EJEMPLO DE PLATZI:

class PasapalosVenezolanos:

    def __init__(self, precio_unidad, numero_racion, relleno):
        self.precio_unidad = precio_unidad
        self.numero_racion = numero_racion
        self.relleno = relleno
    
    def precio_plato(self):
        return self.precio_unidad * self.numero_racion

class Arepa(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_de_preparacion, tipo_hmaiz):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_de_preparacion = tipo_de_preparacion # horno, frita, asada
        self.tipo_hmaiz = tipo_hmaiz # harina de maiz blanco / amarilla

class Tequeno(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_masa):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_masa = tipo_masa # masa tradicional, masa cachapa

class Pastelito(PasapalosVenezolanos):

    def __init__(self, precio_unidad, numero_racion, relleno, tipo_salsa):
        super().__init__(precio_unidad, numero_racion, relleno)
        self.tipo_salsa = tipo_salsa # de ajo, rosada, picante, tartara