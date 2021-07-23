def write(msg):
  leng = len(msg) + 4
  print('~' * leng)
  print(f'  {msg}')
  print('~' * leng)

write('Leandro Tartarini')
write('Hello')
write('United Kingdom')