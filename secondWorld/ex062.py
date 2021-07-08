first = int(input('First Term: '))
rational = int(input('Rational: '))
term = first
cont = 1
total = 0
plus = 10
while plus != 0:
  total = total + plus
  while cont <= total:
    print(f'{term}', end=' -> ')
    term += rational
    cont += 1
  print('Pause')
  plus = int(input('How many more? '))
print(f'You calculate {total} terms')