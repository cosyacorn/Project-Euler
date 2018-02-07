# project euler q25
def fibonacci(x):
  i=2
  first=1
  second=2
  fib=[]
  fib.append(first)
  fib.append(second)
  while True:
    nxt = fib[i-1] + fib[i-2]
    if nxt >= x-1:
      break
    fib.append(nxt)
    i+=1    
  return fib

length = 0
n=3
prev2=1
prev=1

while True:
  nxt = prev + prev2
  length = len(str(nxt))
  if length == 1000:
    break
  prev2 = prev
  prev = nxt
  n += 1
print(n)
