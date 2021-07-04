n1 = int(input('First value: '))
n2 = int(input('Second value: '))
n3 = int(input('Third value: '))
sm = n1
if n2 < n1 and n2 < n3:
  sm = n2
if n3 < n1 and n3 < n2:
  sm = n3

big = n1
if n2 > n1 and n2 > n3:
  big = n2
if n3 > n1 and n3 > n2:
  big = n3

print(f'Biggest number {big}')
print(f'Smallest numer {sm}')