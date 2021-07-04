d = float(input('How many days would you like to rent the car? '))
k = float(input('How many km would you like to ride? '))
n = (d*60) + (k*0.15)
print(f'The total to pay is R${n}')