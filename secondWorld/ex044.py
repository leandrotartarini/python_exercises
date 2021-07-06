price = float(input('Type the price of the product: '))

print('''Payment
[1] cash
[2] credit
[3] 2x credit
[4] 3x plues credit''')

option = int(input('What is your option: '))
if option == 1:
  total = price - (price * 10/100)
elif option == 2:
  total = price - (price * 5/100)
elif option == 3:
  total = price
  ins = total / 2
  print(f'2 installments of {ins:.2f} no interest')
elif option == 4:
  total = price + (price * 20/100)
  totins = int(input('How many installments? '))
  ins = total / totins
  print(f'Your purchase has {totins} installments of {ins} with interest')
else:
  total = price
  print('Invalid option')

print(f'your purchase of ${price:.2f} will cost ${total:.2f} at the end')