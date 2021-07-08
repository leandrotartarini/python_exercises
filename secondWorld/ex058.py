from random import randint
computer = randint(0,10)
print('Will think a number from 0 to 10')
c = 0
guess = ''
while guess != computer:
  guess = int(input('Guess the number: '))
  if guess < computer:
    print('More... Try again')
  if guess > computer:
    print('Less... Try again')
  c += 1
print(f'You got the number after {c} tries')