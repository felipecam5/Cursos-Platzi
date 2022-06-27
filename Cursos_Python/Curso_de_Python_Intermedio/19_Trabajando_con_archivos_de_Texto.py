def read():
    numbers = []
    with open("./19_archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
 
def write():
    names = ["facundo", "Miguel", "Pepe"]
    with open("./19_archivos/lista_nombres.txt", "w+", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()
    read()


if __name__ =="__main__":
    run()
    
