from solution import prime_factors


def test_prime_factor_5():
    result = prime_factors(5)
    assert result == [5]


def test_prime_factor_100():
    result = prime_factors(100)
    assert result == [2, 2, 5, 5]


def test_prime_factor_198():
    result = prime_factors(198)
    assert result == [2, 3, 3, 11]


def test_prime_factor_276():
    result = prime_factors(276)
    assert result == [2, 2, 3, 23]
