def helpPlease(com):
  title(f'Accessing manual command {com}')
  help(com)

def title(msg):
  tam = len(msg) + 4
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)

command = ''
while True:
  title('Helper system python')
  command = str(input('Function or Library > '))
  if command.upper() == 'DONE':
    break
  else:
    helpPlease(command)
title('See you later!')