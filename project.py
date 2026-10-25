from collections import Counter
from math import isqrt, prod  # called with just isqrt(), math. not needed
from rich.console import Console
from rich.table import Table
from rich import print


def is_prime(n: int) -> bool:
    '''Returns a bool signifying whether an integer is prime or not.

    Args:
        n: Int provided by the user.

    Returns:
        bool: Whether the given int is prime.

    '''
    # uses sqrt(n) method for primality testing

    if n <= 1:
        return False
    elif n % 2 == 0:
        return n == 2
    else:
        for i in range(3, isqrt(n)+1, 2):
            if n % i == 0:
                return False
        return True


def prime_factorization(n: int) -> list[int]:
    '''Creates and returns a list of integers which contain the prime factors of a given int.

    Args:
        n: Int provided by the user.

    Returns:
        An list which is the prime factors of n.

    Raises:
        ValueError: If n is negative'''
    
    if 0 <= n <= 1:
        return []
    if n < 0:
        raise ValueError("Negative inputs not allowed!")
    primes_list = generate_primes(isqrt(n))
    factors_list = []
    append = factors_list.append
    for prime in primes_list:
        if n == 1 or prime**2 > n:
            break
        while n % prime == 0:
            n //= prime
            append(prime)
    if n > 1:
        append(n)

    return factors_list


def factor_count(factors: list[int]) -> dict[int, int]:
    '''Takes a list from prime_factorization() and formats it into a dict with a key-value pair of 'prime: power'.

    Args:
        factors: List provided from prime_factorization().

    Returns:
        A dict with a key-value pair of 'prime:power'.
o

    '''
    counts = dict(Counter(factors))
    return counts


def format_factors(factors: dict[int, int]) -> str | None:
    '''Takes a dict from factor_count and formats the factors into a str.

    Args:
        factors: A dict from factor_count().

    Returns:
        A str formatting the factors.

    '''
    formatted = []
    for prime, power in factors.items():
        if power == 0:
            continue
        elif power == 1:
            formatted.append(str(prime))
        else:
            formatted.append(f"{prime}^{power}")
    if not formatted: # checks for falsiness
        return None
    return " * ".join(formatted)


def gcd(a: int, b: int) -> int:
    '''Returns the greatest common divisor (GCD) of two integers.

    Args:
        a: Int provided by the user.
        b: Int provided by the user.

    Returns:
        An int which is the gcd of a and b.
    '''
    # Uses Euclidean Algorithm
    a, b = abs(a), abs(b)

    while True:
        a, b = b, a % b
        if b == 0:
            return a


def lcm(a: int, b: int) -> int:
    '''Returns the least common multiple (LCM) of two integers.

    Args:
        a: Int provided by the user.
        b: Int provided by the user.
    Returns:
        An int which is the lcm of a and b.

    '''
    # uses LCM formula --> lcm(a,b) == (a*b)/gcd(a,b)
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)


def generate_primes(limit:int) -> list[int]:
    '''Uses the Sieve of Eratosthenes to calculuate the list of primes up to a given limit.

    Args:
        limit: Int provided by the user.

    Returns:
        A list of ints which are the primes up to the given limit.

    Raises:
        ValueError: If n is negative
    '''
    # uses Sieve of Eratosthenes
    if 0 <= limit <= 1:
        return []
    if limit < 0:
        raise ValueError("Negative input not allowed!")
    flags = [True] * (limit + 1)
    flags[0], flags[1] = False, False
    for i in range(2, limit + 1):
        if not flags[i]:
            continue
        if i * i > limit:
            break
        for n in range(i * i, limit + 1, i):
            flags[n] = False
    primes_list = []
    for value in range(2, limit + 1):
        if flags[value]:
            primes_list.append(value)
    return primes_list


def coprime(a: int, b: int) -> bool:
    """Uses the gcd to calculate if 2 ints are coprime.

    Args:
        a: int provided by the user.
        b: int provided by the user.

    Returns:
        bool: If the 2 ints are coprime or not.
    """
    if b != 0:
        return gcd(a,b) == 1
    else:
        raise ValueError("b cannot be 0")


def eulers_totient(n: int) -> int:
    """In tandem with the coprime function, returns the totient (number of coprime
        integers from 1 to n) of a given int.

    Args:
        n: Int provided by the user.

    Returns:
        An int which is the count of coprimes between 1 and n.

    Raises:
        ValueError: If n is negative or zero"""

    # two formulas: one for prime numbers, one for composite numbers

    if n == 1:
        return 1
    if n < 1:
        raise ValueError
    if is_prime(n) is True:
        return n - 1
    else:
        result: int = n
        for prime in set(prime_factorization(n)):
            result = result - result//prime
        return result

def modulo(n: int, modulus: int) -> int:
    '''Uses the built in modulus operator ('%') to calculate a modular operation between a dividend and modulus.

    Args:
        n: Int provided by the user.
        modulus: Int provided by the user.

    Returns:
        An int which is the remainder when n is divided by modulus.

    Raises:
        ValueError: If modulus is negative or zero
    '''

    if modulus <= 0:
        raise ValueError
    else:
        return n % modulus


def modulo_exponent(n: str, modulus: int) -> int:
    '''Highly similar to modulo(); instead of taking n as an int, it takes n as a str, and n must contain '^'.

    Args:
        n: Str provided by the user, must contain '^'
        modulus: Int provided by the user.

    Returns:
        An int which is the remainder when n is divided by modulus.

    Raises:
        ValueError: If modulus is negative or zero
    '''
    if modulus <= 0:
        raise ValueError
    else:
        if "^" in n:
            base, power = n.split("^")
            return pow(int(base), int(power), modulus)
        else:
            raise ValueError("First integer must contain '^'.")


def divisor_count(n: int) -> int:
    '''Returns the number of divisors a given int has.

    Args:
        n: Int provided by the user.

    Returns:
        An int which is the count of divisors of n.

    Raises:
        ValueError: If n is negative or zero
    '''
    if n <= 0:
        raise ValueError("Input cannot be negative!")
    factor_powers = factor_count(prime_factorization(n)).values() # n (int) becomes list, then a dict
    result = 1 
    for number in factor_powers:
        result *= number+1
    return result

def is_perfect_square(n: int) -> bool:
    '''Checks whether a given int is a perfect square.

    Args:
        n: Int provided by the user.

    Returns:
        bool: Whether n is a perfect square or not.

    Raises:
        ValueError: If n is negative.
    '''
    if n < 0:
        raise ValueError
    return (isqrt(n))**2 == n

def digit_sum(n: int) -> int:
    '''Returns the sum of all the digits of a given int.

    Args:
        n: Int provided by the user.

    Returns:
        An int which is the sum of all digits within an int.
    '''
    accumulator = []
    for digit in str(n):
        accumulator.append(int(digit))
    return sum(accumulator)

def divisor_sum(n: int) -> int:
    '''Returns the sum of all the divisors of a given int.

    Args:
        n: Int provided by the user.

    Returns:
        An int which is the sum of all the divisors of n.

    Raises:
        ValueError: If n is negative or zero
    '''
    if n <= 0:
        raise ValueError("N must be a positive integer!")
    accumulator = []
    if is_prime(n):
        return n + 1
    for prime, power in factor_count(prime_factorization(n)).items():
        accumulator.append(sum(prime**number for number in range(power+1)))
    return prod(accumulator)

def main():
    console = Console()
    print()
    table = Table(title="Welcome to Numera! Select your operation from the list below.", show_lines=True)
    # 1. Add Columns (with optional styles)
    table.add_column("Number", style="green", header_style="red")
    table.add_column("Operation", style="blue", header_style="red")
    table.add_row("1.", "Prime Testing")
    table.add_row("2.", "Prime Factorization")
    table.add_row("3.", "GCD")
    table.add_row("4.", "LCM")
    table.add_row("5.", "Generate Primes")
    table.add_row("6.", "Coprime")
    table.add_row("7.", "Euler's Totient")
    table.add_row("8", "Modular Arithmetic")
    table.add_row("9", "Modular Arithmetic with Exponent")
    table.add_row("10.", "Divisor Count")
    table.add_row("11.", "Square Testing")
    table.add_row("12.", "Digit Sum")
    table.add_row("13.", "Divisor Sum")
    table.add_row("0.", "Exit")
    console.print(table)
    while True:
        choice = input("Select operation here, enter 0 to exit: ").strip().replace(".","")
        match choice:
            case "1":
                print("[red]PRIME TESTING[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(is_prime(*x))
                        break
                    else:
                        print("Invalid number, please use an integer(s)!")
            case "2":
                print("[red]PRIME FACTORIZATION[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print("Prime factors: ", end="")
                        prime_factorization_list = prime_factorization(x[0])
                        print((prime_factorization_list), sep=", ")
                        user = input("Do you want these numbers in a string? ")
                        if user.casefold() in ("yes", "y"):
                            print(format_factors(factor_count(prime_factorization_list)))
                        break
                    else:
                        print("Invalid number, please use an integer(s)!")
            case "3":
                print("[red]GCD[/red]")
                while True:
                    if x := checker(input("Enter number 1: ")):
                        if y := checker(input("Enter number 2: ")):
                            print(gcd(x[0], y[0]))
                            break
                        else:
                            print("Invalid number, please use an integer!")
                    else:
                        print("Invalid number, please use an integer!")
                       
            case "4":
                print("[red]LCM[/red]")
                while True:
                    if x := checker(input("Enter number 1: ")):
                        if y := checker(input("Enter number 2: ")):
                            print(lcm(x[0], y[0]))
                            break
                        else:
                            print("Invalid numbers, please use integers!")
                    else:
                        print("Invalid numbers, please use integers!")
            case "5":
                print("[red]GENERATE PRIMES[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(generate_primes(*x))
                        break
                    else:
                        print("Invalid number, please use an integer!")
    
            case "6":
                print("[red]COPRIME CHECKER[/red]")
                while True:
                    if x := checker(input("Enter number 1: ")):
                        if y := checker(input("Enter number 2: ")):
                            print(coprime(x[0], y[0]))
                            break
                        else:
                            print("Invalid numbers, please use integers!")
                    else:
                        print("Invalid numbers, please use integers!")
            case "7":
                print("[red]EULER'S TOTIENT[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(eulers_totient(*x))
                        break
                    else:
                        print("Invalid number, please use an integer!")
            case "8":
                print("[red]MODULAR ARITHMETIC[/red]")
                while True:
                    if x := checker(input("What's the dividend?: ")):
                        if y := checker(input("What's the modulus?: ")):
                            if y[0] != 0:
                                print(modulo(x[0], y[0]))    
                            else:
                                print("Modulus cannot be 0!") 
                            break
                        else:
                            print("Invalid numbers, please use integers!")
                    else:
                        print("Invalid numbers, please use integers!")
            case "9":
                print("[red]MOD ARITHMETIC W/ EXPONENT[/red]")
                while True:
                    if x := input("What's the dividend? (must include '^''): "):
                        if y := checker(input("What's the modulus?: ")):
                            if y[0] != 0:
                                print(modulo_exponent(x, y[0]))
                            else:
                                print("Modulus cannot be 0!") 
                            break
                        else:
                            print("Invalid numbers, please use integers!")
                    else:
                        print("Invalid numbers, please use integer containing '^'!")
            case "10":
                print("[red]DIVISOR COUNT[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(divisor_count(*x))
                        break
                    else:
                        print("Invalid number, please use an integer!")
            case "11":
                print("[red]SQUARE TESTING[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(is_perfect_square(*x))
                        break
                    else:
                        print("Invalid number, please use an integer!")
            case "12":
                print("[red]DIGIT SUM[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(digit_sum(abs(x[0])))
                        break
                    else:
                        print("Invalid number, please use an integer!")
            case "13":
                print("[red]DIVISOR SUM[/red]")
                while True:
                    if x:= checker(input("Enter number: ")):
                        print(divisor_sum(*x))
                        break
                    else:
                        print("Invalid number, please use an integer!")
            case "0":
                print("[orange]EXIT[/orange]")
                break
            case _:
                print("[yellow]Sorry, input not recognized[/yellow]")

def checker(*numbers: str):
    try: 
        intnumbers = [int(number) for number in numbers]
        return intnumbers
    except (ValueError, TypeError):
        return False
    #WIP, use all() and isinstance()

if __name__ == "__main__":
    main()
