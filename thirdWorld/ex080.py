lis = []
for c in range(0,5):
  n = int(input('Type a value: '))
  if c == 0 or n > lis[-1]:
    lis.append(n)
    print('Added to the end')
  else:
    pos = 0
    while pos < len(lis):
      if n <= lis[pos]:
        lis.insert(pos, n)
        print(f'Added to position {pos}')
        break
      pos += 1
print(f'Typed values in order were {lis}')