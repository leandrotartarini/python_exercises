products = ('Pencil', 1.75,
'eraser', 2.00,
'notebook', 15.10,
'Backpack', 50.30,
'book', 30.85)

for pos in range(0, len(products)):
  if pos % 2 == 0:
    print(f'{products[pos]:.<30}', end='')
  else:
    print(f'R${products[pos]:>7.2f}')
print('-'*30)

i,f = 0,1
leng = len(products)
print(f'List of price')
while f < leng:
  print(f'{products[i]:.<31}$ {products[f]:>6.2f}', end='\n')
  i += 2
  f += 2