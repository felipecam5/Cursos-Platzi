#Quiero agregar la funcionalidad a las funciones de suma y resta, de informar antes y despues de hacer el calculo. No puedo ponerme a hacer esto para cada función entonces creo un función decoradora.

def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #Acciones adicionales que decoran
        print(f'Vamos a realizar un calculo: ')

        funcion_parametro()

        print(f'Se ha terminado el calculo: ')

    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()


