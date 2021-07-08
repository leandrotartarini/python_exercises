sex = str(input('Sex F/M: ')).strip().upper()
while sex not in 'MmFf':
  sex = str(input('Invalid sex, try again: ')).strip().upper()[0]
print(f'Sex registered {sex}')