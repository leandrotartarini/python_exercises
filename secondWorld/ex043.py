weight = float(input('What is your weight? (kg) '))
height = float(input('What is you heght? (m) '))
imc = weight / (height**2)

if imc < 18.5:
  print(f'{imc:.1f} under weight')
elif imc >= 18.5 and imc < 25:
  print(f'{imc:.1f} ideal weight')
elif imc >= 25 and imc < 30:
  print(f'{imc:.1f} overweight')
elif 30 <= imc < 40:
  print(f'{imc:.1f} Obese')
else:
  print(f'{imc:.1f} extremely Obese')