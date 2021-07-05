n1 = float(input('First note: '))
n2 = float(input('Second note: '))

av = (n1 + n2) / 2
print(f'With {n1:.1f} and {n2:.1f}, the avarage is {av:.1f}')
if av < 5.0:
  print('Failed')
elif av <= 6.9:
  print('recovery')
else:
  print('Passed')