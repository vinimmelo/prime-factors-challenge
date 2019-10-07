""" Simple script to return Prime Factors of a given number """


def is_prime(number: int) -> bool:
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def is_prime_factor(factor, number) -> bool:
    return is_prime(factor) and (number % factor == 0 or factor == number)


def prime_factors(number: int) -> list:
    remainder = int(number)
    if remainder <= 3:
        return [remainder]

    prime_factors = []
    while remainder > 1:
        for i in range(2, remainder + 1):
            if is_prime_factor(i, remainder):
                prime_factors.append(i)
                remainder //= i

    return sorted(prime_factors)
