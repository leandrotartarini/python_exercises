d = int(input('How many kms are you going to drive? '))
if d <= 200:
  price = d * 0.50
else:
  price = d * 0.45
print(f'Trip of {d}kms')
print(f'Ticket price {price}')