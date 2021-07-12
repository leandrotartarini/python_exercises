number = ('zero','one','two','three','four','five')

while True:
  n = int(input('Type a number between 0 and 5: '))
  if 0 <= n <= 5:
    break
  print('Try again ', end='')
print(f'You typed the number {number[n]}')