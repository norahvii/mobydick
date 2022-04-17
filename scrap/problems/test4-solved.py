import re

stop_words_file = []
valid = re.compile(r'^\b[a-z]+\b')

with open('stop-words.txt', 'r') as text_file:
    for line in text_file.read().lower().splitlines():
        if valid.match(line) != None:
            stop_words_file.append(line)

print(stop_words_file)
print(len(stop_words_file))
