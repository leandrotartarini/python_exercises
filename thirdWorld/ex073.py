clubs = ('Newcastle','Sheffield','Liverpool','Manchester City','Tottenham','West Ham','Bournemouth','Crystal Palace')

print(f'Football Clubs list {clubs}')

for t in clubs:
  print(t)

print(f'Top 3 are: {clubs[:3]}')
print(f'Last 2 are: {clubs[-2:]}')
print(f'Alphabetic order: {sorted(clubs)}')
print(f'Liverpool is in position: {clubs.index("Liverpool") + 1}')