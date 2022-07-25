import time

class FiboIter():
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux # Swapping
            self.counter += 1
            return self.aux

# RETO: SERIE DE FIBONACCI PERO HASTA UN NUMERO MAXIMO QUE EL USUARIO INDIQUE

class FiboIterMax():
    
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux # Swapping
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if __name__ =="__main__":

    # fibonacci = FiboIter()
    # for element in fibonacci:
    #     print(element)
    #     time.sleep(0.2)

    fibonacciMax = FiboIterMax(10)
    for element in fibonacciMax:
        print(element)
        time.sleep(0.2)

