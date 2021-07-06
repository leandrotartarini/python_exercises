from datetime import date
actual = date.today().year
db = int(input('Year of birth: '))

age = actual - db
print(f'The athlete is {age} year old')

if age <= 9:
  print('Child')
elif age <= 14:
  print('Young')
elif age <= 19:
  print('Teen')
elif age <= 25:
  print('Adult')
else:
  print('Master')