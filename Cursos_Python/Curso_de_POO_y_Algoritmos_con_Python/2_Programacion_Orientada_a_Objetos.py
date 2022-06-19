#Definir la Clase
class Hotel: 
    #Utilizamos __init__ para inicializar la instancia, se utiliza como primer parametro self 
    def __init__(self, camas, parqueaderos):
        self.camas = camas
        self.parqueaderos = parqueaderos
        self.huespedes = 0
    #Agrega los metodos de la instancia, siempre tienen como primer parametro self.  
    def añadir_huesped(self, cantidad_huespedes):
        self.huespedes += cantidad_huespedes

    def camas_disponibles(self):
        return(self.camas - self.huespedes)


#Creación de la instancia        
hotel = Hotel(camas=50, parqueaderos=20)

hotel.añadir_huesped(20)

print(hotel.camas, hotel.parqueaderos, hotel.huespedes, hotel.camas_disponibles())