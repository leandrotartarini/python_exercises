s = c = 0
while True:
  n = int(input('Type a number: '))
  if n == 999:
    break
  c += 1
  s += n
print(f'Sum {s} and {c} numbers typed')