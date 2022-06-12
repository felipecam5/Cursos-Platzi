#Numero al que se le calculará la raiz cuadrada
objetivo = int(input("Escoge un numero: "))

#Margen de error para econtrar esa raiz cuadrada
epsilon = 0.1

#valor que se irá sumando secuencialmente hasta encontrar la raiz cuadrada
paso = epsilon**2

# Se comenzará a buscar a la raiz cuadrada desde 0.0 en adelante.
respuesta = 0.0

#Mientras que respuesta al cuadrado no sea igual al objetivo (con un margen de error de 0.01, es decir epsilom), este while se seguirá ejecutando
#Respuesta >= objetivo: codigo defensivo; si respuesta es mayor a objetivo, el while seguirá infinitamente, y nunca encontrará a la raiz cuadrada (la raiz cuadrada nunca sería mas grande que el objetivo)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo),respuesta)
    respuesta+=paso

if abs((respuesta**2 -objetivo) >=epsilon):
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')