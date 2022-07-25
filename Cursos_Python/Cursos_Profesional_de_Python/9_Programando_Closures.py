# En esta clase vamos a crear un closure que retorne un string n veces.
# Platzi 4 -> PlatziPlatziPlatzi

# MI SOLUCIÓN PREVIA

def string_to_multiple(palabra: str):
    def times_multiplier(n):
        return palabra *n

    return times_multiplier

word = string_to_multiple("Felipe")

print(word(4))

# SOLUCIÓN FACUNDO

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Felipe"))

# RETO: Create a closure that returns a functions that returns the division of an x number by n

def divisor(n: int):
    def number(x: int) -> float:
        return x/n
    return number

def run2():
    division_by_3 = divisor(3)
    print(division_by_3(18))
    division_by_5 = divisor(5)
    print(division_by_5(100))
    division_by_18 = divisor(18)
    print(division_by_18(54))

if __name__ == "__main__":
    run()
    run2()



