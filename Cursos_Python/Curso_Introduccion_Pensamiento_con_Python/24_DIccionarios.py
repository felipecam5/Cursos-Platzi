diccionario = {
    1: "Arroz",
    2: "Pescado",
    3: "Patacones"
}

print (diccionario.keys(), diccionario.values())

for elemento,a in diccionario.items():
    print (elemento, a)

if 1 in diccionario:
    print (diccionario[1])

#CLASE AHORA SÍ

my_dict = {
    "David": 35,
    "Erika": 32,
    "Jaime": 50,
}

#Devuelve el valor guardado en la llave: "David"
my_dict["David"]

#Este metodo verifica si existe una llave llamada "Juan", sino, devuelve el valor 30
my_dict.get("Juan", 30)

#Cambiar el valor de una llave:
my_dict["David"] = 100

#Agregar una llave y valor
my_dict["Andes"] = 100

#Borrar una llave:
del my_dict["David"]

#Iteracion

for llave in my_dict.keys():
    print(llave)

for valor in my_dict.values():
    print(valor)

for llave, valor in my_dict.items():
    print(llave,valor)

#Verificar si una llave existe

"David" in my_dict