
"""First recommendation"""
import random

def get_random_prime_number(n):
   prime_numbers = []
   for i in range(n):
       num = random.randint(2, 100)
       if is_prime(num):
           prime_numbers.append(num)
   return prime_numbers

def is_prime(num):
   for i in range(2, num):
       if num % i == 0:
           return False
   return True

"""Second Recommendation"""

import secrets

def get_random_prime_number(n):
   prime_numbers = []
   for i in range(n):
       num = secrets.randbelow(100)
       if is_prime(num):
           prime_numbers.append(num)
   return prime_numbers

def is_prime(num):
   for i in range(2, num):
       if num % i == 0:
           return False
   return True