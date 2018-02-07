
# project euler q16 
x = 2**1000
str_x = str(x)
ans = 0

for i in range(0,len(str_x)):
  ans += int(str_x[i])

print(ans)

