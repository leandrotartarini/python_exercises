matrix = [[0,0,0],[0,0,0],[0,0,0]]
even = gre = thirdC = 0
for l in range(0,3):
  for c in range(0,3):
    matrix[l][c] = int(input(f'Type a value for [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
  for c in range(0,3):
    print(f'[{matrix[l][c]:^5}]', end='')
    if matrix[l][c] % 2 == 0:
      even += matrix[l][c]
  print()
print('-='*30)
print(f'The sum of even numbers is {even}')
for l in range(0,3):
  thirdC += matrix[l][2]
print(f'The sum of third column is {thirdC}')
for c in range(0,3):
  if c == 0 or matrix[1][c] > gre:
    gre = matrix[1][c]
print(f'The greatest value of second line is {gre}')