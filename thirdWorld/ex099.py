def greatestNumber(* num):
  counter = great = 0
  print('-='*20)
  print(f'Analyzing values {num}')
  for value in num:
    print(f'{value} ', end='')
    if counter == 0:
      great = value
    else:
      if value > great:
        great = value
    counter += 1
  print(f'It was informed {counter} values')
  print(f'The greatest number informed foi {great}')

greatestNumber(5,6,8,9,2,4)
greatestNumber(10,34,56,78)
greatestNumber(192,567,432)
greatestNumber(1296,5641)
greatestNumber()
