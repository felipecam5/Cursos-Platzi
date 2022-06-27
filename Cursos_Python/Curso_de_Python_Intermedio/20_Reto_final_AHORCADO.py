# -----Instrucciones----- :

# La pantalla se limpia cada vez que se corre el script

# El script muestra la palabra con ("_") y le pide al usuario que ingrese una palabra

# Retorna las palabras en mayusculas

# -----REGLAS-----

# Incorpora comprehensions, manejo de errores y manejo de archivos

#Utiliza el archivo data.txt léelo para obterner las palabras

# -----AYUDAS Y PISTAS-----

# Investiga la función enumerate

# El metodo "get" de los diccionarios puede servirte

# La sentecia os.system("cls") sirve para limpiar la pantalla

# ------------------------------------------------------ FIN ------------------------------------------#

from operator import index, indexOf
import random
import os
FILE_PATH=os.path.dirname(__file__)
import re


diccionario_palabras = {}

with open("./lista_ahorcado/data.txt", "r", encoding="utf-8") as archivo_palabras:
    diccionario_palabras = {key:value for key, value in enumerate(archivo_palabras,0)}

random_word_key = random.randint(0,170)


def ahorcado():
    os.system("cls") 
    word = diccionario_palabras.get(random_word_key)
    print("!Adivine la palabra!", word)
    word_hidden = "_ " * (len(word) - 1)
    word_hidden = word_hidden.strip() 
    print(word_hidden)
    
    while word_hidden.count("_") > 0:  
        letra = input("\n" + "Ingresa una letra: ")
        assert len(letra) <= 1, "No se admite mas de una letra por intento"
        assert letra != "" and letra != " ", "No se admiten caracteres vacios o espacios"
        for character in word:
            if letra == character:
                word_hidden = word_hidden[:word.index(character)*2] + letra.upper() + word_hidden[(word.index(character) *2 + 1):]
                print(letra) 
                if word.count(letra) >1:
                    word_hidden = word_hidden[:word.rindex(character)*2] + letra.upper() + word_hidden[(word.rindex(character) *2 + 1):]
                print(letra) 
        print(word_hidden)
    
    print("Felicidades, ganó")            

def run():
    ahorcado()

if __name__ == "__main__":
    run()