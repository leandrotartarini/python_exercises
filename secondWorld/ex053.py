phrase = str(input('What is the phrase? ')).upper().strip()
word = phrase.split()
tog = ''.join(word)
reverse = ''
for letter in range(len(tog) -1, -1, -1):
  reverse += tog[letter]
print(f'The reverse of {tog} is {reverse}')
if reverse == tog:
  print('Palindrome')
else:
  print('Not a palindrome')