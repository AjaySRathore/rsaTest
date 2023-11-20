import random

def get_random_prime_number(n):
   """
   Generates a random prime number between 2 and n-1.
   """
   prime_numbers = []
   for i in range(2, n):
       if is_prime(i):
           prime_numbers.append(i)
   return random.choice(prime_numbers)

def is_prime(n):
   """
   Checks if a number is prime.
   """
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True

