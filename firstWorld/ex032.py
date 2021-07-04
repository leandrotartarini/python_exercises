from datetime import date
year = int(input('Type an year: '))
if year == 0:
  year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print(f'year {year} is leap')
else:
  print(f'Year {year} is not leap')