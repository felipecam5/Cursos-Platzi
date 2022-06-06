def ahorcado():
    intentos = 0
    letra = "k"
    
    while intentos < 5:
        letrausuario = input("Por favor, escriba una letra: ")
        if letrausuario == letra:
            print("Felicidades, esa era la letra")
            break
        else:
            if letrausuario == "":
                print("Introduzca una letra valida ")
                continue
            intentos +=1
            print ("Falló, ha gastado " + str(intentos) + " intentos")
            if intentos == 5:
                print("Lo siento, vuelva a empezar")

        






if __name__ == "__main__":
    ahorcado()