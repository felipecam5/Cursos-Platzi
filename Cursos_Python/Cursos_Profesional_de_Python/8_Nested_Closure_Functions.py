# 1. Ejemplo de la estructura.

def main_function():
    a: int = 1
    def nested_function():
        print(a)
    return nested_function

saved_value = main_function()
saved_value()
del(main_function)
saved_value()

# 2. Ejemplo de su utilidad.

def multiplierOne(x):
    def multiplierTwo(n):
        return x*n
    return multiplierTwo

times10 = multiplierOne(10)
print(times10(5))
