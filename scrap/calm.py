import re

text = open('stop-words.txt').read().lower()

biglist = []

for match in re.finditer(r'\w+', text):
    if match[0].startswith("#") is not True:
        biglist.append(match[0])

print(len(biglist))
