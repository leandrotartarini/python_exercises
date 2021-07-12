var = tuple(int(input('Type values: '))for c in range(0,5))
print(f'Number 9 appear {var.count(9)} times')
print(f'3 is in position {var.index(3)+1}' if 3 in var else '3 not typed')
print(f'Even values were: ', end='')
print({n for n in var if n % 2 == 0})

print('-=' * 30)

#other solution
num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')) )
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
  print(f'O valor 3 apareceu na {num.index(3) + 1} posição')
else:
  print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
  if n % 2 == 0:
    print(f'{n}', end=' ')