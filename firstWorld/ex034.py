wage = float(input('Type employee wage: '))
if wage <= 1250:
  inc = wage + (wage * 15/100)
else:
  inc = wage + (wage * 10/100)

print(f'Before the wage was {wage}, now employee makes {inc}')