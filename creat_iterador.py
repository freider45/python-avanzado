
class EvenNumbers:

    """Clase que implementa un iterador de todos
    los números pares, o los números pares hasta un máximo"""

    #Constructor para darle un máximo al iterador
    def __init__(self, max=None):
        self.max = max

    #Tiene los elementos que se necesitan, como cada número
    def __iter__(self):
        self.num = 0
        return self

    #Extrae los elementos del iterador
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


if __name__=='__main__':
    pares = EvenNumbers(1000)
    for element in pares:
        print(element)