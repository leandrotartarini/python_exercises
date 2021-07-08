cont = 0
sum = 0
n = int(input('Type a number [999 to stop]: '))
while n != 999:
  sum += n
  cont += 1
  n = int(input('Type a number [999 to stop]: '))
print(f'You typed {cont} numbers and the sum is {sum}')