from datetime import datetime
data = {}
data['name'] = str(input('Name: '))
birth = int(input('Year of birth: '))
data['age'] = datetime.now().year - birth
data['contract'] = int(input('Number of contract (0 not working): '))
if data['contract'] != 0:
  data['contract'] = int(input('Year started working: '))
  data['salary'] = float(input('Salary: '))
  data['retirement'] = data['age'] + ((data['contract'] + 35) - datetime.now().year)
print('-='*30)
for k, v in data.items():
  print(f' - {k} has value {v}')