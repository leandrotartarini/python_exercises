from random import randint
v = 0
while True:
  player = int(input('Type a value: '))
  comp = randint(0,10)
  total = player + comp
  type = ' '
  while type not in 'EO':
    type = str(input('Even or odd [E/O]: ')).strip().upper()
  print(f'You played {player} and the computer played {comp}. Total of {total}', end='')
  print(f'Even: ' if total % 2 == 0 else 'Odd')
  if type == 'E':
    if total % 2 == 0:
      print('You won')
      v += 1
    else:
      print('You lost')
      break
  elif type == 'O':
    if type % 2 == 1:
      print('You won')
      v += 1
    else:
      print('You lost')
  print('Lets play again')
print(f'Game over. You won {v} times')