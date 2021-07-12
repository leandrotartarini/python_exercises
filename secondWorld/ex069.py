totM = tot18 = totW20 = 0
while True:
  gender = ' '
  age = int(input('Age: '))
  while gender not in 'MF':
    gender = str(input('Gender: [M/F]: ')).strip().upper()[0]
  if age >= 18:
    tot18 += 1
  if gender == 'M':
    totM += 1
  if gender == 'F' and age < 20:
    totW20 += 1
  resp = ' '
  while resp not in 'YN':
    resp = str(input('Want to continue [Y/N]: ')).strip().upper()[0]
  if resp == 'N':
    break
print(f'Total people over 18: {tot18}')
print(f'Total men: {totM}')
print(f'Total women under 20 yo: {totW20}')
