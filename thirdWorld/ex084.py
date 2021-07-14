temp = []
princ = []
gre = sma = 0
while True:
  temp.append(str(input('Name: ')))
  temp.append(float(input('Weight: ')))
  if len(princ) == 0:
    gre = sma = temp[1]
  else:
    if temp[1] > gre:
      gre = temp[1]
    if temp[1] < sma:
      sma = temp[1]
  princ.append(temp[:])
  temp.clear()
  res = str(input('Want to continue[Y/N]: '))
  if res in 'Nn':
    break
print(f'Data: {princ}')
print(f'You typed {len(princ)} people')
print(f'The haviest was {gre}kgs ', end='')

for p in princ:
  if p[1] == gre:
    print(f'[{p[0]}]', end='')
print()
print(f'The lightest was {sma}kgs ', end='')
for p in princ:
  if p[1] == sma:
    print(f'[{p[0]}]', end='')
print()