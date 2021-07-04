sp = float(input('What is the current car speed? '))
if sp <= 80:
  print('Have a nice day')
else:
  print(f'You have to pay a fine of {(sp - 80) * 7}')