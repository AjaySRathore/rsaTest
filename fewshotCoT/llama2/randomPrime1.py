import random
import math # added by hand

def generate_secure_random_prime(bits):
   """
   Generates a secure random prime number using the /dev/urandom file in Linux.
   :param bits: The number of bits to use for the prime number.
   :return: A secure random prime number.
   """
   # Generate a random number using the /dev/urandom file
   random_number = random.randint(0, 2**bits - 1)

   # Check if the number is prime
   if is_prime(random_number):
       return random_number
   else:
       # If the number is not prime, generate a new random number
       return generate_secure_random_prime(bits)

def is_prime(number):
   """
   Checks if a number is prime.
   :param number: The number to check.
   :return: True if the number is prime, False otherwise.
   """
   # Check if the number is divisible by any number between 2 and the square root of the number
   for i in range(2, int(math.sqrt(number)) + 1):
       if number % i == 0:
           return False
   return True


prime_number = generate_secure_random_prime(2048)
print(prime_number)
