values = []
listEven = []
listOdd = []
while True:
  values.append(int(input('Type a number: ')))
  res = str(input('Want to continue?[Y/N]: '))
  if res in 'Nn':
    break
for i,v in enumerate(values):
  if v % 2 == 0:
    listEven.append(v)
  else:
    if v % 2 == 1:
      listOdd.append(v)

print(f'List {values}')
print(f'Even numbers {listEven}')
print(f'Odd numbers {listOdd}')