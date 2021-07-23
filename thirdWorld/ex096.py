def area(larg,comp):
  a = larg * comp
  print(f'A area de um terreno de {larg}x{comp} é de {a}m2')

print('Controle de terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)