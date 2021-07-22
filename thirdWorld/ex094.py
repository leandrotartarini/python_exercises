people = []
person = {}
sum = 0
average = 0
while True:
  person.clear()
  person['name'] = str(input('Name: '))
  while True:
    person['gender'] = str(input('Gender [M/F]: ')).upper()[0]
    if person['gender'] in 'MF':
      break
    print('Error! Please, type M or F')
  person['age'] = int(input('Age: '))
  sum += person['age']
  people.append(person.copy())
  while True:
    res = str(input('Wanna continue? [Y/N]: ')).upper()[0]
    if res in 'YN':
      break
    print('Error! Type N or Y')
  if res == 'N':
    break
print('-=' * 30)
print(f'There is {len(people)} people registered')
print(f'The sum of age is {sum}')
average = sum / len(people)
print(f'The average of age is {average:.2f}')
print('Women registered were ', end='')
for p in people:
  if p['gender'] == 'F':
    print(f'{p["name"]} ', end='')
print()
for p in people:
  if p['age'] > average:
    print(' ', end='')
    for k, v in p.items():
      print(f'{k} = {v}: ', end='')
    print()
print('DONE')

