import pytest

import project

# Test Data Definitions; CONSTANT!
PRIME_DATA: list = [(13, True), (57, False), (0, False), (2,True)]
PRIME_FACTORIZATION_DATA: list = [(3, [3]), (15,[3,5]), (1, []), (50, [2,5,5]), (0, [])]
FACTOR_COUNT_DATA: list = [([3,3,3,5], {3: 3, 5:1}),([3,3,5], {3: 2, 5:1}),([5,7,3,2,3,7,5], {2:1, 3: 2, 5 : 2, 7: 2}),([7,5], {5: 1, 7:1})]
FORMAT_FACTOR_DATA: list = [({3: 3, 5:1}, "3^3 * 5" ), ({3:1, 5:1}, "3 * 5"), ({6: 2, 5:1, 3:8}, "6^2 * 5 * 3^8")]
GCD_DATA: list = [(3, 5, 1), (5, 10, 5), (0, 1, 1)]
LCM_DATA: list = [(3, 5, 15), (2, 2, 2), (0, 1, 0), (13, 17, 221)]
GENERATE_PRIMES_DATA: list = [(5, [2,3,5]), (0, []), (15, [2,3,5,7,11,13])]
COPRIME_DATA: list = [(3,5,True),(2,4,False),(0,1,True)]
EULERS_TOTIENT_DATA: list = [(5, 4),(1,1), (2, 1), (9, 6), (15,8)]
MODULO_DATA: list = [(5, 3, 2),(9, 2, 1),(0, 1, 0), (2, 2, 0)]
MODULO_EXPONENT_DATA: list = [("2^3", 2, 0),("5^5", 3, 2),("0^8", 1, 0)]

@pytest.mark.parametrize("number, expected", PRIME_DATA)
def test_is_prime(number: int, expected: bool):
    assert project.is_prime(number) == expected


@pytest.mark.parametrize("number, expected", PRIME_FACTORIZATION_DATA)
def test_prime_factorization(number: int, expected: list[int]):
    assert project.prime_factorization(number) == expected
    with pytest.raises(ValueError):
            project.prime_factorization(-4)

@pytest.mark.parametrize("givenlist, expected", FACTOR_COUNT_DATA)
def test_factor_count(givenlist: list[int], expected: dict[int, int]):
    assert project.factor_count(givenlist) == expected

@pytest.mark.parametrize("givendict, expected", FORMAT_FACTOR_DATA)
def test_format_factors(givendict: dict[int,int], expected: str):
    assert project.format_factors(givendict) == expected

@pytest.mark.parametrize("num1, num2, expected", GCD_DATA)
def test_gcd(num1: int, num2: int, expected: int):
    assert project.gcd(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", LCM_DATA)
def test_lcm(num1: int, num2: int, expected: int):
    assert project.lcm(num1, num2) == expected

@pytest.mark.parametrize("limit, expected", GENERATE_PRIMES_DATA)
def test_generate_primes(limit: int, expected: list[int]):
    assert project.generate_primes(limit) == expected
    with pytest.raises(ValueError):
        project.generate_primes(-4)

@pytest.mark.parametrize("num1, num2, expected", COPRIME_DATA)
def test_coprime(num1: int, num2: int, expected: bool):
    assert project.coprime(num1, num2) == expected 
    with pytest.raises(ValueError):
            project.coprime(0,0)

@pytest.mark.parametrize("number, expected", EULERS_TOTIENT_DATA)
def test_eulers_totient(number: int, expected: int):
    assert project.eulers_totient(number) == expected
    with pytest.raises(ValueError):
         project.eulers_totient(0)

@pytest.mark.parametrize("number, modulus, expected", MODULO_DATA)
def test_modulo(number: int, modulus: int, expected: int):
    assert project.modulo(number, modulus) == expected
    with pytest.raises(ValueError):
        project.modulo(5,0)
        project.modulo(0,0)
        project.modulo(10,-5)



@pytest.mark.parametrize("number, modulus, expected", MODULO_EXPONENT_DATA)
def test_modulo_exponent(number: str, modulus: int, expected: int):
    assert project.modulo_exponent(number, modulus) == expected
    with pytest.raises(ValueError):
        project.modulo_exponent("5^5", 0)
        project.modulo_exponent("3^3", -5)


