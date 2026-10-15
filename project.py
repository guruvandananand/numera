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
    primes_list = generate_primes(n)  
    factors_list = []
    break_outer = False
    while n > 1 and break_outer == False:
        for prime in primes_list:
            if prime > math.sqrt(n):
                factors_list.append(n)
                break_outer = True
                break
            while True:
                if n % prime == 0:
                    n //= prime
                    factors_list.append(prime)
                else:
                    break
            
    
    return factors_list
    

def factor_count(factors: list[int]) -> dict[int, int]:
    counts = Counter(factors)
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
            
            




def main():
    pass
    # terminal selection here, do this LAST

if __name__ == "__main__":
    main()
   