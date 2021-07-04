from random import randint
from time import sleep
comp = randint(0,5)
print('I will think a number between 0 and 5, guess it...')
num = int(input('What number did I think? '))
print('processing.....')
sleep(1)
if num == comp:
  print('You won')
else:
  print(f'You lost. I though the number {comp}, not {num}')