import math
from collections import Counter

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

def prime_factorization(n: int) -> list[int]:
    if n <= 1:
        return []
    primes_list = generate_primes(math.isqrt(n))  
    factors_list = []
    append = factors_list.append
    for prime in primes_list:
        if n == 1: 
            break
        elif prime ** 2 > n:
            break
        while n % prime == 0:
            n //= prime
            append(prime)
    if n > 1:
        append(n)
            
    return factors_list
    
def factor_count(factors: list[int]) -> dict[int, int]:
    counts = dict(Counter(sorted(factors)))
    return counts

def format_factors(factors: dict[int, int]) -> str|None:
    factor_length = len(factors)
    formatted = ""
    for index, (prime, power) in enumerate(factors.items()):
        if index == factor_length - 1:
            formatted = formatted + str(prime)
            if power != 1:
                formatted = formatted + "^" + str(power)
        else:
            if power == 1:
                formatted = formatted + str(prime) + " x "
            else:
                formatted = formatted + str(prime) + "^" + str(power) + " x "
    if formatted == "":
        return None
    return formatted



def gcd(a: int, b:int) -> int:
    # Uses Euclidean Algorithm
    a, b = abs(a), abs(b)
  
    while True:
        a, b = b, a % b
        if b == 0:
            return a

def lcm(a:int, b: int) -> int:
    # uses LCM formula --> lcm(a,b) == (a*b)/gcd(a,b)
    a,b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return (a*b)//gcd(a,b)
    
def generate_primes(limit):
    # uses Sieve of Eratosthenes
    if limit == 0 or limit == 1:
        return []
    if limit < 0:
        raise ValueError
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

def coprime(a:int, b:int) -> bool:
    '''Uses the gcd tp calculate if 2 ints are coprime.
    
    Args:
        a: int provided by the user.
        b: int provided by the user.
        
    Returns:
        bool: If the 2 ints are coprime or not.
    '''

    if gcd(a,b) == 1:
        return True
    else:   
        return False

    def eulers_totient(n:int) -> int:
        '''In tandem with the coprime function, returns the totient *(list of coprime
        integers from 1 to n) of a given int.
        
        Args:
            n: Int provided by the user.
            
        Returns:
            An int which is the count of coprimes between 1 and n.
            
        Raises:
            ValueError: If n is negative'''

        # two formulas: one for prime numbers, one for composite numbers

        if n < 0:
            raise ValueError
        coprimes_list=[]
        if is_prime(n) == True:
            coprimes_list.extend(range(2,n)) # n acts like n-1 in the usual formula because of the range cutoff
        else:
            for i in range(2,n): # 1 is not coprime, n acts like n-1
                if coprime(i, n) == True:
                    coprimes_list.append(i)
            return len(coprimes_list)

        def modulo(n: int, modulus: int) -> int:

            if modulus < 0:
                raise ValueError
            else:
                return n % modulus

        def modulus_exponent(n: str, modulus: int) -> int:
            if modulus < 0:
                raise ValueError
            else:
                if "^" in n:
                    base, power = n.split("^")
                    return pow(int(base),int(power),modulus)
                else:
                    raise ValueError
            
            




def main():
    pass
    # terminal selection here, do this LAST

if __name__ == "__main__":
    main()
   