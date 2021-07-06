from random import randint
from time import sleep
item = ('Paper', 'Scissor', 'Rock')
computer = randint(0,2)
print(''''Your options
[0] PAPER
[1] SCISSOR
[2] ROCK''')
player = int(input('Type your option: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('-=' * 12)
print(f'Computer: {item[computer]}')
print(f'Player: {item[player]}')
print('-=' * 12)

if computer == 0:
  if player == 0:
    print('Draw')
  elif player == 1:
    print('Player WINS')
  elif player == 2:
    print('Computer WINS')
  else:
    print('Invalid')

elif computer == 1:
  if player == 1:
    print('Draw')
  elif player == 0:
    print('Computer WINS')
  elif player == 2:
    print('Player WINS')
  else:
    print('Invalid')

elif computer == 2:
  if player == 2:
    print('Draw')
  elif player == 0:
    print('Player WINS')
  elif player == 1:
    print('Computer WINS')
  else:
    print('Invalid')
