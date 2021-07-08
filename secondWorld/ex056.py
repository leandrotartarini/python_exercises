sumage = 0
olderman = 0
oldername = ''
woman20 = 0
for p in range(1,5):
  print(f'----- {p} PERSON')
  name = str(input('Name: ')).strip()
  age = int(input('Age: '))
  sex = str(input('M/F: ')).strip()
  sumage += age
  if p == 1 and sex in 'Mm':
    olderman = age
    oldername = name
  if sex in 'Mm' and age > olderman:
    oldername = age
    oldername = name
  if sex in 'Ff' and age < 20:
    woman20 = woman20 + 1
average = sumage / 4
print(f'Age avarage is {average}')
print(f'The oldest man is {oldername} and he is {olderman} years old')
print(f'There is {woman20} women under 20 yo')