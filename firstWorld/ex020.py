import random
f = str(input('First student: '))
s = str(input('Second student: '))
t = str(input('Third student: '))
fo = str(input('Fourth Student: '))
c = [f,s,t,fo]
random.shuffle(c)
print('The presentation order is')
print(c)