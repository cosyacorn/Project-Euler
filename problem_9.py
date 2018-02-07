# project euler q9

def is_triple(x,y,z):
  oa = x**2 + y**2
  hyp = z**2
  if oa == hyp:
    return True
  else:
    return False

triples = []

for i in range(3,1000):
  for j in range(i+1,1000):
    for k in range(j+1,1000):
      if is_triple(i,j,k) == True:
        triples.append([i,j,k])

for a in range(len(triples)):
  if triples[a][0]+triples[a][1]+triples[a][2]==1000:
    a1 = triples[a][0]
    a2 = triples[a][1]
    a3 = triples[a][2]

prod = a1*a2*a3
print(prod)
