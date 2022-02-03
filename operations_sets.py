
def run():
    #unión
    my_set_1 = {3,4,5}
    my_set_2 = {5,6,7}

    my_set_3 = my_set_1 | my_set_2
    print(my_set_3)

    #intersección
    my_set_4 = {3,4,5}
    my_set_5 = {5,6,7}

    my_set_6 = my_set_4 & my_set_5
    print(my_set_6)

    #Diferencia
    my_set_7 = {3,4,5}
    my_set_8 = {5,6,7}

    my_set_9 = my_set_7 - my_set_8
    print(my_set_9)

    my_set_10 = my_set_8 - my_set_7
    print(my_set_10)

    #Diferencia simétrica
    my_set_11 = {3,4,5}
    my_set_12 = {5,6,7}

    my_set_13 = my_set_11 ^ my_set_12
    print(my_set_13)

if __name__=='__main__':
    run()
