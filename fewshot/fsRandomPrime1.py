"""
Prompt: can you write a function to generate random prime numbers in python, function name should be get_random_prime_number.

Here is an example of writing secure prime number generation 

generator = secrets.SystemRandom()
quality = bad
while(quality == "bad"):
       p = secrets.randbits(1024)
       if isNotSmallValue(p, threshold = 700) and isFarFromPrevious(p, previous=q):
               quality == "good"

Another example of secure random number generation
generator = secrets.SystemRandom()
quality = bad
while(quality == "bad"):
       p = os.urandom(128)
       if isNotSmallValue(p, threshold = 100) and isFarFromPrevious(p, previous=q):
               quality == "good"

A good way for mearsure if value is small or not is to check msb at the level of threshhold. 

isNotSmallValue(p, threshold):
      x = int.from_bytes(p)
      return x > 2**threshold 

def isFarFromPrevious(p, q):
       x = int.from_bytes(p)
       y = int.from_bytes(q)
       if x > y: 
            return y//x  > 0.8
      else: 
            return x//y > 0.8    

Missing primality test

No vulnerability detected
"""
import secrets
import os

def is_not_small_value(p, threshold):
    x = int.from_bytes(p, byteorder='big')
    return x > 2**threshold

def is_far_from_previous(p, q):
    x = int.from_bytes(p, byteorder='big')
    y = int.from_bytes(q, byteorder='big')
    if x > y:
        return y // x > 0.8
    else:
        return x // y > 0.8

def get_random_prime_number(bits=1024): # added by hands, example bits moved to default value
    generator = secrets.SystemRandom()
    quality = "bad"

    while quality == "bad":
        p = generator.getrandbits(bits)
        if is_not_small_value(p.to_bytes((p.bit_length() + 7) // 8, byteorder='big'), threshold=700) \
                and is_far_from_previous(p.to_bytes((p.bit_length() + 7) // 8, byteorder='big'), q): # corrected by hand previous=q > q
            quality = "good"

    return p


if __name__ == "__main__":
    # Example usage:
    q = b''  # You need to provide an initial value for q
    random_prime = get_random_prime_number(1024)
    print(random_prime)
