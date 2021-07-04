import math
a = float(input('Type an angle: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'An angle of {a} has a sine of {s:.2f}')
print(f'An angle of {a} has a cosine of {c:.2f}')
print(f'An angle of {a} has a tangent of {t:.2f}')