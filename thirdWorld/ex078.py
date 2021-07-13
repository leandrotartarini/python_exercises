lis = list()
for n in range(0, 5):
  lis.append(int(input(f'Type a value for position {n}: ')))
gre = max(lis)
sma = min(lis)
print(f'You typed the values {lis}')

print(f'The greatest value typed was {gre} in position ', end='')
for i, v in enumerate(lis):
  if v == gre:
    print(f'{i}... ', end='')

print(f'\nThe smallest value types was {sma} in position ', end='')
for i, v in enumerate(lis):
  if v == sma:
    print(f'{i}... ', end='')

print('')