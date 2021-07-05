num = int(input('Type an integer number: '))
print('''Choose an option:
[1] convert to Binary 
[2] convert to Octal
[3] convert to Hexadecimal''')
option = int(input('Your option: '))

if option == 1:
  print(f'{num} converted to binary is equals to {bin(num)[2:]}')
elif option == 2:
  print(f'{num} converted to Octal is equals to {oct(num)[2:]}')
elif option == 3:
  print(f'{num} converted to Hexadecimal is equals to {hex(num)[2:]}')
else:
  print('Invalid Option')