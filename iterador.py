
def run():
    #Creando un iterador
    my_list = [1,2,3,4,5]
    #La lista o iterable, la convertimos a iterador
    my_iter = iter(my_list)

    #iterando un iterador
    #La funcion next me trae el siguiente dato
    '''print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))'''
    #Cuando ya no quedan mas datos, se eleva la excepcion StopIteration
    #print(next(my_iter))

    #ahora hagamoslo para que se itere sin estar haciendolo manual
    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            break

    

if __name__=='__main__':
    run()
