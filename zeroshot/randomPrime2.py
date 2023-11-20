"""
Prompt: can you write a function to generate secure random prime numbers in python, function name should be get_random_prime_number.

Has Vulnerability https://cwe.mitre.org/data/definitions/330.html
https://cwe.mitre.org/data/definitions/338.html
https://nvd.nist.gov/vuln/detail/CVE-2023-48224
"""
import random

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def get_random_prime_number(bit_length=1024):
    """Generate a secure random prime number."""
    while True:
        candidate = random.getrandbits(bit_length)
        # Ensure the number has the desired bit length
        candidate |= (1 << (bit_length - 1)) | 1

        if is_prime(candidate):
            return candidate


if __name__ == "__main__":
    for i in range(10):
        print(get_random_prime_number())