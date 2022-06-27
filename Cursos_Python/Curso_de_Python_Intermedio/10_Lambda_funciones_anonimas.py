# lambda argumentos: expresion

muliplicador = lambda mul : print(mul * 4)

palindromo = lambda string : string == string[::-1]

if __name__ == "__main__":
    muliplicador(10)
    print(palindromo("ana"))
    