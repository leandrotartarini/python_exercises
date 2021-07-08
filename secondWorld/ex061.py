first = int(input('First Term: '))
rational = int(input('Rational: '))
term = first
cont = 1
while cont <= 10:
  print(f'{term}', end=' -> ')
  term += rational
  cont += 1
print('Done')