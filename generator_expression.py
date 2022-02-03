

def run():
    #Generator Expresion

    #lista
    my_list = [0,1,4,7,9,10]
    
    my_second_list = [x*2 for x in my_list]   #list comprenhension
    my_second_generator = (x*2 for x in my_list) #Generator expresion

    for i in my_second_list:
        print(i)

    input()

    for i in my_second_generator:
        print(i)


if __name__=='__main__':
    run()

