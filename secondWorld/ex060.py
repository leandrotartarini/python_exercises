n = int(input('Type a number to check its factorial: '))
c = n 
f = 1
print(f'Calculating {n}! = ', end='')
while c > 0:
  print(f'{c}', end='')
  print(' x ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print(f'{f}')