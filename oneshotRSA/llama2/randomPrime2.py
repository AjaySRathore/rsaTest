import random

def get_random_prime_number():
   while True:
       num = random.randint(1000000000, 9999999999)
       if is_prime(num):
           return num

def is_prime(num):
   for i in range(2, num):
       if num % i == 0:
           return False
   return True
