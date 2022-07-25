from datetime import datetime

# IMPORTANTE EN ESTA CLASE:
#
# Cuando tenemos funciones que reciben diferente numeros de paramentros, que podemos hacer para que el decorador sirva en cualquier función sin importar el numero de parametros?
#
# La respuesta es *args, **kwargs
#
# *args -> No importa la cantidad de argumentos posicionales que vengan de la función original. i.e def suma(a,b) 
# 
# **kwargs -> No importa la cantidad de argumentos nombrados que se le envíen. i.e def nombre (apellido = "camacho") 
#
# * -> Operador de destructuración de Python.

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " Segundos")
    return wrapper

@execution_time
def random_func():
    a = [ i for i in range(0, 1000000)]

@execution_time
def suma(a: int, b: int) -> int:
    return (a+b)

@execution_time
# Función con parametro nombrado!!!
def saludo (nombre = "Felipe"):
    print("Hola " + nombre)
    
if __name__ == "__main__":
    random_func()
    suma(4,5)
    saludo("Felipe Camacho")

