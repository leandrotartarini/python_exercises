from time import sleep
def counter(i,f,p):
  if p < 0:
    p *= -1
  if p == 0:
    p = 1
  print(f'Counting from {i} to {f} skipping {p}')
  if i < f:
    cont = i
    while cont <= f:
      print(f'{cont} ', end='', flush=True)
      sleep(0.2)
      cont += p
  else:
    cont = i
    while cont >= f:
      print(f'{cont} ', end='', flush=True)
      sleep(0.2)
      cont -= p
  print('DONE')

counter(1,10,2)
counter(10,0,2)
beg = int(input('Begging: '))
end = int(input('End: '))
ski = int(input('Skip: '))
counter(beg,end,ski)
