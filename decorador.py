
import os

def func_decorator(func):
    def envoltura():
        print("Esto es una decoracion")
        func()
    return envoltura

@func_decorator
def saludo():
    print("Hola")

def mayusculas(funci):
    def funcion(texto: str) -> str:
        return funci(texto).upper()
    return funcion

@mayusculas
def mensaje(nombre):
    return f"{nombre} recibiste un mensaje"
   
def run():
    os.system("cls")
    print(mensaje("freider"))
    
if __name__=='__main__':
    run()