s = 0
count = 0
for num in range(1, 501, 2):
  if num % 3 == 0:
    count += 1
    s += num
print(f'The total sum is {s} and {count} numbers were counted')