def suma(a,b):
    total = a+b
    print(total)

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        print (f'{apellido} {nombre}')
    else:
        print( f'{nombre} {apellido}')

if __name__ == "__main__":
    suma(5,6)
    nombre_completo("Felipe","Camacho", inverso=False)
    nombre_completo(apellido="Camacho", nombre="Felipe")