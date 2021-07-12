total = totHun = smallest = cont = 0
cheap = ''
while True:
  product = str(input('Type the name of the product: '))
  price = float(input('Price $: '))
  cont += 1
  if cont == 1 or price < smallest:
    smallest = price
    cheap = product
  total += price
  if price > 1000:
    totHun += 1
  resp = ' '
  while resp not in 'YN':
    resp = str(input('Want to continue [Y/N]: ')).strip().upper()[0]
  if resp == 'N':
    break
print(f'Done')
print(f'Final price ${total:.2f}')
print(f'There is {totHun} products over $1000')
print(f'The cheapeast product was {cheap} which cost {smallest:.2f}')