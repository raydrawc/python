def prime_list(step=1):
    n = 1
    while True:
        n += step
        yield n


def is_primes(n):
    return lambda x: x % n


def prime():
    ls = prime_list()
    while True:
        n = next(ls)
        yield n
        ls = filter(is_primes(n), ls)


def is_prime(num):
    for i, x in enumerate(prime()):
        if x > num:
            break
        else:
            print(x)


if __name__ == '__main__':
    is_prime(100)
