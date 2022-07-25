# """
# Un pequeño resumen:

# Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

# Los sets son inmutables

# Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento

# los sets guardan los elementos en desorden

# Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}

# Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:

# add(): nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara

# update(): nos permite agregar múltiples elementos al set

# remove(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error

# discard(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.

# pop(): permite eliminar un elemento del set, pero lo hará de forma aleatoria.

# clear(): Limpia completamente el set, dejándolo vació.

# Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set

# """

# SET DE ENTEROS
my_Set = {1,2,3,4,5}
print(f'Este es un set de enteros: {my_Set} \n')

# SET DE DIFERENTES TIPOS DE DATOS
my_Set = {1.0, "hi", (1,4,7)}
print(f'Este es un set de diferentes tipos de datos: {my_Set} \n')

# EJEMPLOS DE OPERACIONES SOBRE SETS
my_set = {1,2,3}
print(f'Este es mi set original: {my_set} \n')

# AÑADIENDO UN ELEMENTO AL SET
my_set.add(4)
print(f'Este es el set despues de utilizar .add() {my_set}')

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set pero no tira error si no lo encuentra
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# Elimina el elemento, pero si no lo encuentra tira error.
my_set.remove(2)
print(my_set) 

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 

#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple = ("hola", "hola", 1, 2)
my_set2 = set(my_tuple)
print(my_set2) #Output {'hola', 1}
