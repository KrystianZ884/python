def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False
    return True


def find_primes_in_range(start, end):
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes


prime = find_primes_in_range(1, 100)

print(prime)
