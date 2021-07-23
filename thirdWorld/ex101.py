def vote(year):
  from datetime import date
  age = date.today().year - year
  if age < 16:
    return f'With {age} years of age, you cannot vote'
  elif age < 18 or age > 65:
    return f'With {age} years of age, your vote is optional'
  else:
    return f'With {age} years of age, must vote'

yearBirth = int(input('When were you born: '))
print(vote(yearBirth))