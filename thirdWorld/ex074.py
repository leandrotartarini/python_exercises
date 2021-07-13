import math
from random import randint, sample

i,f = 1,100
a,b,c,d,e = randint(i,f), randint(i,f), randint(i,f), randint(i,f), randint(i,f)
numbers = (a,b,c,d,e)

print(f'Numbers are: {numbers}')
print(f'Smallest: {min(numbers)}')
print(f'Greatest: {max(numbers)}')

print('*' * 30)

a = tuple(sample(range(100), 5))
print(a)
print(f'The greatest is: {max(a)} and the smallest is {min(a)}')

print('*' * 30)

numbers = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print('Values are: ', end='')
for n in numbers:
  print(f'{n} ', end='')
print(f'\nThe greatest is: {max(numbers)}')
print(f'The smallest is: {min(numbers)}')