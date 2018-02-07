# project euler q10

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

primes = [2]

for i in range(1,2000000,2):
  if is_prime(i) == True:
    primes.append(i)

tot = sum(primes)

print(tot)
