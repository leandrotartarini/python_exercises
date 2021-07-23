def record(name='unknown', goals=0):
  print(f'Player {name} scored {goals} goals')

n = str(input('Name of the player: '))
g = str(input('How many goals: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  record(goals = g)
else:
  record(n,g)