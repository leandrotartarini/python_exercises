value = float(input('What is the price of the house? '))
wage = float(input('What is your salary? '))
years = int(input('How many years do you want to pay? '))
months = years * 12
mortgage = value/months
minimum = wage * (30/100)
print(f'House price of {value} in {years} years the monthly payment is {mortgage:.2f} ')
if mortgage <= minimum:
  print('Approved')
else:
  print('Denied')