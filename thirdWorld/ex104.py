def readInt(msg):
  ok = False
  value = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      value = int(n)
      ok = True
    else:
      print('Error, type an integer number please')
    if ok:
      break
  return value

n = readInt('Type a number: ')
print(f'You typed the number {n}')