
def num_primo(a: int) -> bool:
    aux: int =0
    for i in range(1, 101):
        if a%i ==0:
            aux = aux+1
    if aux<=2:
        return True
    else:
        return False
        
def run():
    if num_primo('4'):
        print("Es un numero primo")
    else:
        print("No es un numero primo")
        
if __name__=='__main__':
    run()