import pytest
import project

# Test Data Definitions
PRIME_DATA = [(13, True), (57, False), (0, False), (2,True)]
PRIME_FACTORIZATION_DATA = [(3, [3]), (15,[3,5]), (1, []), (50, [2,5,5]), (0, []), (-5, [])]
FACTOR_COUNT_DATA = [([3,3,3,5], {3: 3, 5:1}),([3,3,5], {3: 2, 5:1}),([5,7,3,2,3,7,5], {2:1, 3: 2, 5 : 2, 7: 2}),([7,5], {5: 1, 7:1})]
FORMAT_FACTOR_DATA = [({3: 3, 5:1}, "3^3 * 5" ), ({3:1, 5:1}, "3 * 5"), ({6: 2, 5:1, 3:8}, "6^2 * 5 * 3^8")]


@pytest.mark.parametrize("number, expected", PRIME_DATA)
def test_is_prime(number, expected):
    assert project.is_prime(number) == expected


@pytest.mark.parametrize("number, expected", PRIME_FACTORIZATION_DATA)
def test_prime_factorization(number, expected):
    assert project.prime_factorization(number) == expected

@pytest.mark.parametrize("givenlist, expected", FACTOR_COUNT_DATA)
def test_factor_count(givenlist, expected):
    assert project.factor_count(givenlist) == expected

@pytest.mark.parametrize("givendict, expected", FORMAT_FACTOR_DATA)
def test_format_factors(givendict, expected):
    assert project.format_factors(givendict) == expected
