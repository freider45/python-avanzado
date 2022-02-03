
import time

class fiboIter():

    """En esta clase vamos a hacer la sucesión fibonacci
    la cual consta de que cada término es la suma de los 
    dos anteriores  0 1 1 2 3 5 8 13 21 ...."""

    def __init__(self, max=None):
        self.max = max

    #Creación e inicialización de variables a usar
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    #Extracción de los números con la lógica fibonacci 
    def __next__(self):
        
        if self.counter == 0:
            self.counter += 1
            return self.num1
        elif self.counter == 1:
            self.counter += 1
            return self.num2
        else:
            self.aux = self.num1 + self.num2
            if self.aux <= self.max:
                #self.num1 = self.num2
                #self.num2 = self.aux
                #Las dos lineas de arriba, las podemos acortar así
                self.num1, self.num2 = self.num2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration
        

if __name__=='__main__':
    maximo = int(input("Digite un máximo para la serie fibonacci: "))
    fibonacci = fiboIter(maximo)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)



