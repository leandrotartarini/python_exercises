from time import sleep
n1 = int(input('First value: '))
n2 = int(input('Second value: '))
option = 0
maxi = n1
while option != 5:
  print('''
  [1] Sum
  [2] Times
  [3] Greatest
  [4] New numbers
  [5] Exit''')
  option = int(input('Whats your option? '))
  if option == 1:
    print(f'Sum is {n1 + n2}')
  elif option == 2:
    print(f'Times is {n1 * n2}')
  elif option == 3:
    if n2 > maxi:
      maxi = n2
      print(f'The greatest is {maxi}')
    else:
      print(f'Greatest is {n1}')
  elif option == 4:
    n1 = int(input('First Value: '))
    n2 = int(input('Second value: '))
  elif option == 5:
    print('Exiting...')
  else:
    print('Invalid Option')
  sleep(0.5)