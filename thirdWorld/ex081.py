values = []
while True:
  values.append(int(input('Type a value: ')))
  res = str(input('Want to continue? [Y/N]: '))
  if res in 'Nn':
    break
print('-=' * 30)
print(f'You typed {len(values)} values')
values.sort(reverse=True)
print(f'The reverse list is {values}')
if 5 in values:
  print('five is on the list')
else:
  print('five is not on the list')