from random import randint
from time import sleep
lis = []
games = []
cont = 0
ammo = int(input('How many games would you like to play?: '))
tot = 1
while tot <= ammo:
  cont = 0
  while True:
    num = randint(1,60)
    if num not in lis:
      lis.append(num)
      cont += 1
    if cont >= 6:
      break
  lis.sort()
  games.append(lis[:])
  lis.clear()
  tot += 1
for i,l in enumerate(games):
  print(f'Game {i+1}: {l}')
  sleep(0.5)