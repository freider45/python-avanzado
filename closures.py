
import os

def main(cadena: str):
    def nested(num:int):
        assert type(num) == int, "debe ingresar un numero para hacer la multiplicacion" 
        print(cadena*num)
    return nested

def make_divison(n:int):
    def division(x:int) -> float:
        assert n != 0, "ZeroDivisionError, you cannot divide by zero puto"
        return x//n
    return division

def run():
    os.system("cls")
    a = main("Freider")
    b = main("Escobar")
    
    division_by_3 = make_divison(4)
    print(division_by_3(18))
    
    division_by_5 = make_divison(5)
    print(division_by_5(100))

    division_by_18 = make_divison(18)
    print(division_by_18(54))


if __name__=='__main__':
    run()