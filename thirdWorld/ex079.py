lis = []
while True:
  n = int(input('Type a value: '))
  if n not in lis:
    lis.append(n)
    print('Valued added')
  else:
    print('Duplicated, not adding')
  r = str(input('Want to continue?[Y/N]')).strip().upper()
  if r in 'Nn':
    break
lis.sort()
print(f'Values typed were: {lis}')