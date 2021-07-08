res = 'Y'
avarage = sum = qu = maxi = mini = 0
while res in 'Yy':
  num = int(input('Type a number: '))
  sum += num
  qu += 1
  if qu == 1:
    maxi = num
    mini = num
  else:
    if num > maxi:
      maxi = num
    if num < mini:
      mini = num
  res = str(input('Want to continue? [Y/N]: ')).strip()[0].upper()
avarage = sum / qu
print(f'You types {qu} numbers. The sum is {sum} and the avarage is {avarage}, the max number is {maxi} and the min number is {mini}')