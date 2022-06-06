a = "Felipe Camacho Hurtado"
for i in range(len(a)):
    print(a[i])

def run():
    nombre = input("Escribe tu nombre: ")
    for letra in nombre:
        print(letra.upper())
    print (len(nombre))

if __name__ == "__main__":
    run()