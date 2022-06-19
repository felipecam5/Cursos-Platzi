class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "En Resposo"
        self._motor = Motor(cilindros = 4)
        self._serial = Serial(serial=1234)

    def acelerar(self, tipo="Despacio"):

        if tipo == "Rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = "En movimiento"


class Motor:

    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Serial:

    def __init__(self, serial, estado = "Confirmado"):
        self.serial = serial
        self.estado = estado
        self._buscado = None

ferrari = Automovil("GTO 228", "FERRARI", "ROJO")
print(ferrari._serial.serial, ferrari._serial.estado)