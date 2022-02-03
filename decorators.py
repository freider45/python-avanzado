
from datetime import datetime
import os

def execution_time(func):
    '''*args y **kwargs son para decir que no importa la
    cantidad de argumentos que reciba'''
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass
    
@execution_time
def suma(a: int, b: int) -> int:
    return a + b

def run():
    os.system("cls")
    random_func()
    suma(5,23)

if __name__=='__main__':
    run()