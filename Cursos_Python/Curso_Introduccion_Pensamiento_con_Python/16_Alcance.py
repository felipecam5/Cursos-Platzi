from re import X


def funcion1():
    mensaje = "Hola"
    def funcion2(mensaje):
        mensaje += "Mundo"
        return print(mensaje)
    funcion2(mensaje)
    return print(mensaje)
funcion1()  

#Scope global

x ='Esta es una variable Global'
def funcion():
    x = 'Esta es una variable local'
    print(x)

funcion()
print(x)

##Scope Local
def funcion4():
    x = 'Esta es una variable local'
    def funcion_interior():
        print(x)
    funcion_interior()
funcion4()

##KeyWord Global

def funcion5():
    global y
    y = 'Esta es una variable global'
funcion5()
print(y)

