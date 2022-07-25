
def my_gen():
    
    print("Hola Papá")
    n = 0
    yield n

    print("Hola Mamá")
    n = 1
    yield n

    print("Hola Hermano")
    n = 2
    yield n

saludo = my_gen()
print(next(saludo))
print(next(saludo))
print(next(saludo))

# Generator Expression

my_list = [1,2,3,4,5]
my_second_gen = (x**2 for x in my_list)


print(my_list)
print (my_second_gen) # No se puede imprimir, tiene que ser casteado a lista.
for i in my_second_gen:
    print(i)