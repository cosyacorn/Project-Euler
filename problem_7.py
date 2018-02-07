# project euler q7
from math import sqrt
def is_prime(x):
  lim = int(sqrt(x)) + 1
  if x == 0:
    return False
  if x == 1:
    return False
  elif x == 2:
    return True
  else:
    for i in range(2,lim):
      if x%i == 0:
        return False
    return True

primes = []
i=0

while len(primes) < 10001:
  if is_prime(i) == True:
    primes.append(i)
  i+=1

print(primes[10000])
