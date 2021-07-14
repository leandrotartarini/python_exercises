exp = str(input('Type an expression: '))
pile = []
for sim in exp:
  if sim == '(':
    pile.append('(')
  elif sim == ')':
    if len(pile) > 0:
      pile.pop()
    else:
      pile.append(')')
      break
if len(pile) == 0:
  print('Valid expression')
else:
  print('Invalid Expression')