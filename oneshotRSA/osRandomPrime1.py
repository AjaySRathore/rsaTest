"""
Prompt: can you write a function to generate random prime numbers in python, function name should be get_random_prime_number.

Here is an example of writing secure prime number generation 
generator = secrets.SystemRandom()
secrets.randbelow(50)


No vulnerabilty detected
"""


import secrets
import math

def is_prime(n, k=5):
    """Check if a number is prime using the Miller-Rabin primality test."""
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
        a = secrets.randbelow(n - 2) + 2
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
    """Generate a random prime number with the specified bit length."""
    while True:
        candidate = secrets.randbits(bit_length)
        if candidate % 2 == 0:
            candidate += 1  # Ensure the number is odd
        if is_prime(candidate):
            return candidate


if __name__ == "__main__":
    for i in range(10):
        random_prime = get_random_prime_number()
        print("Random Prime Number:", random_prime)