import random
import math

def is_prime(n, iterations=1):
    for i in range(iterations):
        randomint = random.randint(0,n-1)
        if pow(randomint, n-1, n) != 1:
            return False

        

    return True

def main ():
    currNum = 600851475143
    lastPrime = 0
    i = 2
    while i <= currNum:
        if currNum % i == 0 and is_prime(i):
            while currNum % i == 0:
                currNum = currNum / i
                lastPrime = i
        i += 1   
    print lastPrime

main()
