menu = """
    Bienvenidos a la selección de algoritmos de raiz cuadradas.

    A continuación encontrará los diferentes tipos de algoritmos que podrá seleccionar. Por favor, ingrese el numero correspondiente:

    1 - Enumeración Exhaustiva
    2 - Aproximación de Soluciones
    3 - Busqueda Binaria

"""

eleccion = int(input(menu))

print(eleccion)

def raiz_cuadrada():
    if eleccion == 1:

        objetivo = int(input("Seleccionaste el algoritmo: Enumeración Exhaustiva. Por favor, escoge un entero: "))
        respuesta = 0

        while respuesta**2 < objetivo:
            respuesta+=1
            print(respuesta)

        if respuesta**2 == objetivo:
            print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        else:
            print(f'El {objetivo} no tiene una raiz cuadrada exacta')
    elif eleccion == 2:
        #Numero al que se le calculará la raiz cuadrada
        objetivo = int(input("Seleccionaste el algoritmo: Aproximación de soluciones. Por favor, escoge un entero: "))

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
    elif eleccion == 3:
        # numero al que se le calculará la raiz cuadrada
        objetivo = int(input("Seleccionaste el algoritmo: Busqueda Binaria. Por favor, escoge un entero: "))

        # margen de error para encontrar esa raiz cuadrada
        epsilon = 0.001

        # valor minimo para calcular largo del conjunto
        bajo = 0.0

        # valor maximo para calcular largo de conjunto. Función max() >> elegirá el valor máximo de los parámetros que le demos; colocamos 1.0 como valor mínimo aceptado (así nos cubrimos de que, por ejemplo, el usuario coloque un valor negativo), y objetivo (valor que nos dará el usuario)
        alto = max(1.0, objetivo)

        # aqui generamos el valor medio de nuestro conjunto, a lo cual se puede genera el condicional (if) para elegir la mitad menor o la mitad mayor.
        respuesta = (alto+bajo) / 2


        # para entender esto, lo más fácil es imaginar que el while saltará de un grupo de mitades a otro, dependiendo de la situación, hasta que el grupo se divida lo suficiente como para dar con el objetivo.

        # el while comienza diciendo que, hasta que la respuesta de con el resultado (con un margen de error de 0.01, es decir epsilon), se hará la iteración del paso 2 de este algoritmo. 
        while abs(respuesta**2 - objetivo) >= epsilon:
            print(f'{bajo} bajo, {alto} alto, {respuesta} respuesta')
            # si respuesta**2 no es mayor que objetivo, quiere decir que respuesta debe ser mayor (de respuesta para abajo, no nos sirve; nos sirve el rango de respuesta para arriba). 
            # RECORDAR: respuesta es el valor medio del conjunto que estamos analizando (mirar más arriba)
            if respuesta**2 < objetivo:
                # como sabemos que de respuesta para abajo no tenemos un valor que nos sirva, actualizamos el piso (bajo) de nuestro conjunto a el valor actual de respuesta.
                bajo = respuesta
                # si respuesta**2 es mayor que objetivo, quiere decir que respuesta debe ser menor (de respuesta para arriba, no nos sirve; nos sirve el rango de respuesta para abajo)
            else:
                # como sabemos que respuesta para arriba no tenemos un valor que nos sirva, actualizamos el techo (alto) de nuestro conjunto a el valor actual de respuesta
                alto = respuesta

        # Saliendo del else, ejecutamos el código para que respuesta (punto medio de nuestro conjunto) se actualice al nuevo conjunto.
            
            respuesta = (alto+bajo) / 2


        ##################################
        # Repitiendo este loop, llegará un punto en el que el conjunto sea muy pequeño, y hallaremos la raiz cuadrada.
        # Los loops necesarios serán mucho menos que si usamos busqueda exhaustiva o aproximacion
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print (f'Por favor, escoga una opción correcta')

if __name__ == "__main__":
    raiz_cuadrada()