#project euler q12

def tri(n):
  return n*(n+1)/2

maxnum = 0
maxtri = 0
maxi = 0
for i in range(1,100000):
  num = tri(i)
  test = divisors(num)
  if test > maxnum:
    maxnum = test
    maxtri = num
    maxi = i
    if maxnum >500:
      break

print(maxnum)
print(maxtri)
print(maxi)
