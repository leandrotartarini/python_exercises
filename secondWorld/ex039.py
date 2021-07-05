import datetime
year = int(input('Year of birth: '))
ay = datetime.date.today().year
age = ay - year
#f = ay - (year + age)
print(f'Who was born in {year} is {age} years old in {ay}')

if age == 18:
  print('Serve army')
elif age < 18:
  s = 18 - age
  print(f'{s} years to serve the army')
  yeararmy = ay + s
  print(f'You will have to serve the army in {yeararmy}')
else:
  s = age - 18
  print(f'You should have served {s} years ago')
  yeararmy = ay - s
  print(f'You should have served in {yeararmy}')