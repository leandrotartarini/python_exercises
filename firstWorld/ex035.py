r1 = float(input('First: '))
r2 = float(input('Second: '))
r3 = float(input('Third: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Could be a triangle')
else:
  print('Cant be a triangle')