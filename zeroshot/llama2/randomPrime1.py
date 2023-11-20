import random

def get_random_prime_number(n):
   prime_numbers = []
   for i in range(n):
       num = random.randint(1, 1000000000)
       if is_prime(num):
           prime_numbers.append(num)
   return prime_numbers

def is_prime(num):
   if num < 2:
       return False
   for i in range(2, num):
       if num % i == 0:
           return False
   return True

