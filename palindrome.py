
def isPalindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    if isPalindrome(1000):
        print("Es un puto palindromo")
    else:
        print("No es un puto palindromo")

if __name__=='__main__':
   run() 