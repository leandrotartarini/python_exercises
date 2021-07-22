player = {}
matches = []
player['name'] = str(input('Name of the player: '))
total = int(input(f'How many matches did {player["name"]} play?: '))
for c in range(0, total):
  matches.append(int(input(f'How many goals in match {c + 1}?: ')))
player['goals'] = matches[:]
player['tot'] = sum(matches)
print('-='*30)
print(player)
print('-='*30)
for k,v in player.items():
  print(f'Field {k} has value {v}')
print('-=' *30)
print(f'Player {player["name"]} played {len(player["goals"])} matches')
for i,v in enumerate(player['goals']):
  print(f' in match {i+1}, scored {v} goals')
print(f'Scored a total of {player["tot"]} goals')
