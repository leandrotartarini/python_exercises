team = []
player = {}
matches = []
while True:
  player.clear()
  player['name'] = str(input('Name of the player: '))
  total = int(input(f'How many matches did {player["name"]} play? '))
  matches.clear()
  for c in range(0, total):
    matches.append(int(input(f'How many goals in match {c + 1}?: ')))
  player['goals'] = matches[:]
  player['tot'] = sum(matches)
  team.append(player.copy())
  while True:
    res = str(input('Wanna continue [Y/N]? ')).upper()[0]
    if res in 'YN':
      break
    print('Error! type N or Y')
  if res == 'N':
    break
print('-='*30)
print('cod ',end='')
print()
for k,v in enumerate(team):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-' * 30)
while True:
  search = int(input('Which player do you want to check? (999 to stop): '))
  if search == 999:
    break
  if search >= len(player):
    print(f'Error, there is no player with this code {search}')
  else:
    print(f'Player {team[search]["name"]}: ')
    for i,g in enumerate(team[search]['goals']):
      print(f'In match {i+1}, scored {g} goals')
  print('-'*30)
print()
