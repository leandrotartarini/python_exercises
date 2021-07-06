from datetime import date
less18 = 0
over18 = 0
for c in range(1,8):
  birth = int(input(f'What year person {c} was born? '))
  actual = date.today().year
  age = actual - birth
  if age >= 18:
    over18 += 1
  else:
    less18 += 1
print(f'\n{over18} are over 18 and {less18} less than 18 year old')