phrase = str(input('Insert a phrase: ')).strip().lower()
print(f'Letter A appears {phrase.count("a")} times')
print(f'Letter A appears for the first time in position {phrase.find("a") + 1}')
print(f'The last letter A appear in position {phrase.rfind("a") + 1}')