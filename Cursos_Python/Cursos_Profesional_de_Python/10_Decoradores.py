# Creación de decoradores, las cuales son closures pero más poderosos.


def decorador(func):
    def envoltura():
        print("Esto no estaba en la version inicial")
        func()
    return envoltura

# def saludo():
#     print("Hola mundo")
# saludo = decorador(saludo)

# Con azucar sintatica (@)-------------------:

@decorador
def saludo():
    print("Hola")
# --------------------------------------------

# EJEMPLO: DECORADOR QUE PONE EN MAYUSCULAS EL TEXTO DE UNA FUNCIÓN CON AZUCAR SINTACTICA

def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayuscula
def name(nombre):
    return(nombre)


def main(): 
    saludo()
    print(name("Felipe"))


if __name__ == "__main__":
    main()