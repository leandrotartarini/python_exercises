print('Leandros Bank')
value = int(input('How much do you want to withdraw: '))
tot = value
ced = 100
totced = 0
while True:
  if tot >= ced:
    tot -= ced
    totced += 1
  else:
    if totced > 0:
      print(f'Total of {totced} bank notes of ${ced}')
    if ced == 100:
      ced = 50
    elif ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 5
    elif ced == 5:
      ced = 1
    totced = 0
    if tot == 0:
      break
print('Cheers')