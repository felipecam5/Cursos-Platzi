#Función sin manejo de excepción:

# def palindromo(string):
#     return string == string[::-1]

#Función con manejo de expeción con: TRY - EXCEPT

def palindromo_exc(string):
    try:
        return string == string[::-1]
    except TypeError:
        print("La función solo admite strings")


#Función con manejo de excepción con: RAISE
def palindromo_exc_2(string):
    try:
        if len(string) == 0:
            raise ValueError("No se admiten cadenas de texto vacias")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False 


#Función con manejo de expeción con: FINALLY

if __name__ =="__main__":
    # palindromo(1), 
    palindromo_exc(1)
    print(palindromo_exc_2(""))