student = {}
student['name'] = str(input('Type the name: '))
student['avarage'] = float(input(f'Avarage of {student["name"]}: '))
if student['avarage'] >= 7:
  student['score'] = 'approved'
elif student['avarage'] >= 5:
  student['score'] = 'need to take a second test'
else:
  student['score'] = 'unapproved'
print('-='*30)
for k,v in student.items():
  print(f'{k} is equal to {v}')