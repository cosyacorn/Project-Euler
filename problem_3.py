# project euler q3

from math import sqrt

def is_prime(x):
  lim = int(sqrt(x)) + 1
  if x == 1:
    return False
  elif x == 2:
    return True
  else:
    for i in range(2,lim):
      if x%i == 0:
        return False
    return True

def prime_factors(x):
  other = 0
  factors = []
  if x%2 == 0:
    factors.append(2)
  lim = int(sqrt(x)) + 1
  for i in range(3,lim,2):
    if x%i == 0:
      other = x/i
      if is_prime(i) == True:
        factors.append(i)
      if is_prime(other) == True:
        factors.append(other)
  return factors

print(prime_factors(600851475143))
