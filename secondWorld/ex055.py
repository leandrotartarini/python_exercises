maxx = 0
minn = 0
for p in range(1,6):
  weight = float(input(f'Weight of {p} person: '))
  if p == 1:
    maxx = weight
    minn = weight
  else:
    if weight > maxx:
      maxx = weight
    if weight < minn:
      minn = weight
print(f'The havier weight is {maxx} and the lightest is {minn}')