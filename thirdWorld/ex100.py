from random import randint

def draw(list):
  print('Drawing 5 values: ', end='')
  for cont in range(0,5):
    n = randint(1,10)
    list.append(n)
    print(f'{n} ', end='')
  print(' DONE')

def sumEven(list):
  sumNumber = 0
  for value in list:
    if value % 2 == 0:
      sumNumber += value
  print(f'The sum of even numbers is equals to: {sumNumber}')

number = []
draw(number)
sumEven(number)
