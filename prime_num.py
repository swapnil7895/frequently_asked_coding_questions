

def check_prime():
    num = 8

    for i in range( 2, num ):
        if num % i == 0:
            print(f"Prime number")
            return
    print(f"Not prime")

check_prime()