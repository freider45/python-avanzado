
import os

def run():
    os.system("cls")

    #Cración e impresión de sets
    my_set = {1,4,5}
    print("my_set = ", my_set)

    my_set_2 = {"Hola", 23.3, True, False}
    print("my_set_2 = ",my_set_2)

    my_set_3 = {3,2,3}
    print("my_set_3 = ", my_set_3)

    #Creación e impresión de sets vacios
    empty_set = {}     #No es un set vacio
    print(type(empty_set))

    empty_set_ = set()  #Es un set vacio
    print(type(empty_set_))

    #Casting con los set, osea convertirlos a otra ED
    my_list = [1,1,2,3,4,4,5]
    my_set_4 = set(my_list)
    print(my_set_4)

    my_tuple = ("Hola", "Hola", "Hola", 1)
    my_set_5 = set(my_tuple)
    print(my_set_5)

    #Añadir elementos a un set
    my_set_6 = {1,2,3}
    my_set_6.add(4)     #Añadir un elemento
    print(my_set_6)

    my_set_6.update([1,2,5])  #Añadir elementos multiples
    print(my_set_6)

    my_set_6.update([1,7,2], {6,8})  #Añadir elementos multiples
    print(my_set_6)

    #Borrar elementos a un set
    my_set_7 = {1,2,3,4,5,6,7}
    print(my_set_7)

    my_set_7.discard(1)  #Borrar un elemento existente
    print(my_set_7)

    my_set_7.remove(2)  #Borrar un elemento existente
    print(my_set_7)

    my_set_7.discard(16)  #Borrar un elemento inexistente
    print(my_set_7)

    my_set_7.remove(12)  #Borrar un elemento inexistente
    print(my_set_7)

    my_set_7.pop()  #Borrar un elemento aleatorio
    print(my_set_7)

    my_set_7.clear()  #limpiar o borrar todo el set
    print(my_set_7)
    
    #Creación e impresión de un set erroneo
    my_set_error = {[1,2,3],4}
    print("my_set_4 = ", my_set_error)

if __name__=='__main__':
    run()