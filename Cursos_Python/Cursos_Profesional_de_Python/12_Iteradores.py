my_list = [i for i in range(0,30)]
my_iter = iter(my_list)

def iterable_example():
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

# Como utilizamos next() para una lista muy larga?

def iterable_example2():
    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

if __name__ == "__main__":
    iterable_example()
    iterable_example2()