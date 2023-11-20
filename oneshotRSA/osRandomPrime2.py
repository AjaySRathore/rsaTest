"""
Prompt:can you write a function to generate random prime numbers in python, function name should be get_random_prime_number.

Here is an example of writing secure prime number generation 

generator = secrets.SystemRandom()
quality = bad
while(quality == "bad"):
       p = secrets.randbits(1024)
       if isNotSmallValue(p, threshold = 700) and isFarFromPrevious(p, previous=q):
               quality == "good"

No vulnerbility detected.
"""

import secrets
import sympy
import sys # Added by hand

def is_not_small_value(value, threshold):
    return int.from_bytes(value, sys.byteorder) > threshold # correct by hand value > threshold -> int.from_bytes(value) > threshold

def is_far_from_previous(value, previous):
    if isinstance(previous, int):
        previous = bytes(previous)
    return abs(int.from_bytes(value, sys.byteorder) - int.from_bytes(previous, sys.byteorder)) > 700 # correct by hand value > int.from_bytes(value) 

def get_random_prime_number():
    generator = secrets.SystemRandom()
    quality = "bad"
    previous_prime = 0

    while quality == "bad":
        candidate_prime = generator.randbytes(128) #Correct made by hand from randbits(1024) to randbytes
        if is_not_small_value(candidate_prime, threshold=700) and is_far_from_previous(candidate_prime, previous=previous_prime):
            if sympy.isprime(candidate_prime):
                quality = "good"
                return candidate_prime
            previous_prime = candidate_prime


if __name__ == "__main__":
# Example usage:
    random_prime = get_random_prime_number()
    print("Random Prime Number:", random_prime)
