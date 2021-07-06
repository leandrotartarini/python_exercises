sum = 0
counter = 0
for c in range(1,7):
  n = int(input('Type an integer number: '))
  if n % 2 == 0:
    sum += n
    counter += 1
print(f'You informed {counter} even numbers and the total sum is {sum}')