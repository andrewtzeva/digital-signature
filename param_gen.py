from random import randint
from gmpy2 import is_prime


def get_random_prime(prime_size):
    x = randint(1 << (prime_size - 1), (1 << prime_size) - 1)
    while not (is_prime(x)):
        x = randint(1 << (prime_size - 1), (1 << prime_size) - 1)
    return x


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = randint(1, n - 1)
        if is_composite(a, n):
            return False
    return True


def is_composite(a, n):
    t, d = decompose(n - 1)
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True

    return False


def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i


def get_random_primes(prime_size):
    x = randint(1 << (prime_size - 1), (1 << prime_size) - 1)
    y = 2*x + 1
    while not (is_prime(x)) or not is_prime(y):
        x = randint(1 << (prime_size - 1), (1 << prime_size) - 1)
        y = 2*x + 1
    return x,y


print(get_random_primes(512))


