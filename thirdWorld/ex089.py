record = list()
while True:
  name = str(input('Name: '))
  firstScore = float(input('First Score: '))
  secondScore = float(input('Second Score: '))
  average = (firstScore + secondScore)/2
  record.append([name, [firstScore, secondScore], average])
  res = str(input('Want to continue? [Y/N]: '))
  if res in 'Nn':
    break
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-='*20)
for i,a in enumerate(record):
  print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
  print('-'*30)
  opt = int(input('Show which students grades? (999 to stop): '))  
  if opt == 999:
    break
  if opt <= len(record) - 1:
    print(f'Grades of {record[opt][0]} are {record[opt][1]}')
