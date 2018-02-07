#project euler q6

def sum_squares(x):
  lst = [a**2 for a in range(x)]
  return sum(lst)


def square_sum(x):
  lst = [a for a in range(x)]
  return (sum(lst))**2

ans = square_sum(100) - sum_squares(100)

print(ans)

