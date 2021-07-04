num = int(input('type a number: '))
u = num // 1 % 100
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analyzing the number {num}')
print(f'Unit: {u}')
print(f'Ten: {d}')
print(f'Hundred: {c}')
print(f'Thousand: {m}')