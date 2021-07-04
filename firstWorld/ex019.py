from random import choice
f = str(input('First student: '))
s = str(input('Second student: '))
t = str(input('Third student: '))
fo = str(input('Fourth Student: '))
c = [f,s,t,fo]
print('The student chosen was {}'.format((choice(c))))