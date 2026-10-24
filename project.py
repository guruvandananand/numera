from collections import Counter
from math import isqrt, prod  # called with just isqrt(), math. not needed
from rich.console import Console
from rich.table import Table
from rich import print


def is_prime(n: int) -> bool:
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
    counts = dict(Counter(factors))
    return counts


def format_factors(factors: dict[int, int]) -> str | None:
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
    # Uses Euclidean Algorithm
    a, b = abs(a), abs(b)

    while True:
        a, b = b, a % b
        if b == 0:
            return a


def lcm(a: int, b: int) -> int:
    # uses LCM formula --> lcm(a,b) == (a*b)/gcd(a,b)
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)


def generate_primes(limit:int) -> list[int]:
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
    """Uses the gcd tp calculate if 2 ints are coprime.

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


def eulers_totient(n: int) -> int | None:
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

    if modulus <= 0:
        raise ValueError
    else:
        return n % modulus


def modulo_exponent(n: str, modulus: int) -> int:
    if modulus <= 0:
        raise ValueError
    else:
        if "^" in n:
            base, power = n.split("^")
            return pow(int(base), int(power), modulus)
        else:
            raise ValueError("Wrong function call, use modulo")


def divisor_count(n: int) -> int:
    if n <= 0:
        raise ValueError("Input cannot be negative!")
    factor_powers = factor_count(prime_factorization(n)).values() # n (int) becomes list, then a dict
    result = 1 
    for number in factor_powers:
        result *= number+1
    return result

def is_perfect_square(n: int) -> bool:
    if n < 0:
        raise ValueError
    return (isqrt(n))**2 == n

def digit_sum(n: int) -> int:
    accumulator = []
    for digit in str(n):
        accumulator.append(int(digit))
    return sum(accumulator)

def divisor_sum(n: int) -> int:
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
                        print(*prime_factorization(*x), sep=", ")
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
                first = int(input("Enter number 1: "))
                second = int(input("Enter number 2: "))
                print(lcm(first, second))
            case "5":
                print("[red]GENERATE PRIMES[/red]")
                number = int(input("Enter number: "))
                print(generate_primes(number))
            case "6":
                print("[red]COPRIME CHECKER[/red]")
                first = int(input("Enter number 1: "))
                second = int(input("Enter number 2: "))
                print(coprime(first, second))
            case "7":
                print("[red]EULER'S TOTIENT[/red]")
                number = int(input("Enter number: "))
                print(eulers_totient(number))
            case "8":
                print("[red]MODULAR ARITHMETIC[/red]")
                number = int(input("What's the dividend?: "))
                modulus = int(input("What's the divisor/modulus?: "))
                print(modulo(number, modulus))
            case "9":
                print("[red]MOD ARITHMETIC W/ EXPONENT[/red]")
                number = input("What's the dividend? (must include ^): ") # must be str
                modulus = int(input("What's the divisor/modulus?: "))
                print(modulo_exponent(number, modulus))
            case "10":
                print("[red]DIVISOR COUNT[/red]")
                number = int(input("Enter number: "))
                print(divisor_count(number))
            case "11":
                print("[red]SQUARE TESTING[/red]")
                number = int(input("Perfect Square to check: "))
                print(is_perfect_square(number))
            case "12":
                print("[red]DIGIT SUM[/red]")
                number = int(input("Enter number: "))
                print(digit_sum(number))
            case "13":
                print("[red]DIVISOR SUM[/red]")
                number = int(input("Enter number: "))
                print(divisor_sum(number))
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
