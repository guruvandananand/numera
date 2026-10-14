import math
import sys

def is_prime(n:int) -> bool:
    # uses sqrt(n) method for primality testing
     
    if n <= 1:
        return False
    elif n % 2 == 0:
        if n != 2: 
            return False
        else:
            return True
    else:
        root = int(math.sqrt(n))
        for i in range(2, root + 1):
            if n % i == 0:
                return False
        return True

def prime_factorization(n: int):
    pass
    #do later


def gcd(a: int, b:int) -> int:
    # Uses Euclidean Algorithm

    try:
        a, b = abs(a), abs(b)
    except ValueError:
        sys.exit("Don't use negative integers!") #perhaps
        '''I'm thinking of just calling main or even calling the function where this input is given because this
        should be straitifed into multiple functions'''
        # do a call for main here instead, THIS IS A PLACEHOLDER
    
    while True:
        a, b = b, a % b
        if b == 0:
            return a

def lcm(a:int, b: int) -> str:
    # uses LCM formula --> lcm(a,b) == (a*b)/gcd(a,b)

    try:
        a,b = abs(a), abs(b)
    except ValueError:
        sys.exit("Don't use negative integers!") #perhaps
    return f"{(a*b)/gcd(a,b):.0f}"

def generate_primes(limit):
    # uses Sieve of Eratosthenes
    if limit < 1:
        sys.exit()
    flags = [True] * (limit+1)
    flags[0], flags[1] = False, False
    for i in range(2,limit+1):
        if not flags[i]:
            continue
        if i*i > limit:
            break
        for n in range(i*i, limit + 1, i):
            flags[n] = False
    primes_list = []
    for value in range(2, limit+1):
         if flags[value]:
            primes_list.append(value)
    return primes_list
            
            

        





def main():
    pass
    # terminal selection here, do this LAST

if __name__ == "__main__":
    limit = generate_primes(int(input("whats the limit for gen primes? ")))
    print(limit)
