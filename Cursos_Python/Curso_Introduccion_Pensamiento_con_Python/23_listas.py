my_list = [1,2,3]
my_list[0:2:1] #Recorrerla

my_list.pop()

#Clonar listas

a = [1,2,3]
b = list(a)
# ó
b = a[::]

#List Comprehension

double = [i * 2 for i in my_list]
pares = [i * 2 for i in my_list if i%2 == 0]