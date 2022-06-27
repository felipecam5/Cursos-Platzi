def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Felipe",
        "lastname" : "Camacho"
    }

    super_list = [
        {"firstname": "Felipe","lastname" : "Camacho"},
        {"firstname": "Julian","lastname" : "Camacho"},
        {"firstname": "Romulo","lastname" : "Camacho"},
        {"firstname": "Nery","lastname" : "Hurtado"},
        {"firstname": "Lolita","lastname" : "Camacho"}   
    ]

    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5 ],
        "integer_nums" : [-1, -2, 0 ,1, 2],
        "floatin_nums" : [1.1, 4.5, 6.43 ]
    }
    
    # Imprimir las listas dentro de un diccionario
    for key, value in super_dict.items():
        print(key,"-", value)

    # Imprimir los diccionarios dentro de la lista.
    for i in super_list:
        dict_element = i
        keys, values = dict_element.items()
        print(f'* {keys} - {values}')

    # Imprimir los diccionarios dentro de las listas.
    for i in super_list:
        for key, value in i.items():
            print(f'* {key} - {value}')

if __name__ == "__main__":
    run()