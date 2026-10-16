import pytest
import project


def test_is_prime():
    assert project.is_prime(13) == True
    assert project.is_prime(57) == False
    assert project.is_prime(0) == False
    assert project.is_prime(2) == True


def test_prime_factorization():
    assert project.prime_factorization(3) == [3]
    assert project.prime_factorization(15) == [3, 5]
    assert project.prime_factorization(1) == []
    assert project.prime_factorization(50) == [2, 5, 5]
    assert project.prime_factorization(0) == []
    assert project.prime_factorization(-5) == []


def test_factor_count():
    assert project.factor_count([3, 3, 3, 5]) == {3: 3, 5: 1}
    assert project.factor_count([3, 3, 5]) == {3: 2, 5: 1}
    assert project.factor_count([5, 7, 3, 2, 3, 7, 5]) == {2: 1, 3: 2, 5: 2, 7: 2}
    assert project.factor_count([7, 5]) == {5: 1, 7: 1}
