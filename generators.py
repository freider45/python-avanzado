
def my_gen():
    """Este es un ejemplo de generadores"""

    """Yield funciona igual que un return, pero
    este lo que hace es que guarda el estado hasta
    donde quedo el último yield"""

    print("Hello world!")
    n = 0
    yield n 


    print("Hello heaven!")
    n = 1
    yield n 

    print("Hello hell!")
    n = 2
    yield n 

a = my_gen()

print(next(a)) #Hello world
print(next(a)) #Hello heaven
print(next(a)) #Hello hell
print(next(a)) #aqui eleva la excepción StopIteration

