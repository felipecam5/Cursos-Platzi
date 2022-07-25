my_set1 = {3,4,5}
my_set2 = {5,6,7}

# UNION: Se utiliza el operador ( " | " )
my_set3 = my_set1 | my_set2
print(my_set3)

# INTERSECCIÓN: Se utiliza el operador ( " & " )
my_set3 = my_set1 & my_set2
print(my_set3)

# DIFERENCIA: Se utiliza el operador ( " - " )
my_set3 = my_set1 - my_set2 #Elementos que están exclusivamente en el set 1
print(my_set3)

my_set3 = my_set2 - my_set1 #Elementos que están exclusivamente en el set 2
print(my_set3)

# DIFERENCIA SIMETRICA: Se utiliza el operador ( " ^ " )
my_set3 = my_set1 ^ my_set2
print(my_set3)
