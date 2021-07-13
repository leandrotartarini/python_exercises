words = ('learn', 'programming', 'language', 'python', 'course', 'free', 'study', 'practice', 'work', 'store', 'future')

for pos in words:
  print(f'\nIn word {pos.upper()} there is ', end='')
  for letter in pos:
    if letter.lower() in 'aeiou':
      print(letter, end='')