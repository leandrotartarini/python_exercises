f = int(input('First term: '))
r = int(input('Rational: '))
d = f + 10 * r
for i in range(f,d,r):
  print(i, end= ' -> ')
print('Done')