palabra_input = input("Por favor, introduzca la palabra a confirmar si es palindroma o no: ")
palabra_input_sinespacios = palabra_input.replace(" ", "")
palabra_final = palabra_input_sinespacios.lower()

def confirmacion():
    if(palabra_input == ""):
        print("Por favor, ingresar una palabra")
    elif (palabra_input == palabra_input[::-1]):
        print("La palabra " + palabra_input + " es palindroma")
    elif (palabra_final == palabra_final[::-1]):
        print("La palabra " + palabra_input + " es palindroma")        
    
    else:
        print("La palabra " + palabra_input + " no es palindroma") 

confirmacion()