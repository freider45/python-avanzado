
import time
from typing import Counter

def fiboGen(maximo :int):
    num1, num2, counter = 0, 1, 0
    while True:
        if counter == 0:
            counter += 1
            yield num1
        elif counter == 1:
            counter += 1
            yield num2
        else:
            aux = num1 + num2
            if aux <= maximo:
                num1, num2 = num2, aux
                counter += 1
                yield aux
            else:
                break

#una forma más corta e óptima para la serie
def FiboGen(max: int = None):
    num1, num2 = 0, 1
    while not max or num1 <= max:
        yield num1
        num1, num2 = num2, num1+num2

def run():
    maximo = int(input("Digite un máximo para la serie fibonacci: "))
    fibonacci = FiboGen(maximo)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)

if __name__=='__main__':
   run()

   