import re
import collections

text = open('stop-words.txt').read().lower()

stop_list = []

for line in text.split('\n'):
    if line and not line.startswith("#") and not line.startswith(' '):
        stop_list.append(line)

book = re.findall(r'\w+',open('shortdick.txt').read().lower())


final = []

for elem in book:
    if elem not in stop_list:
        final.append(elem)

most_common = collections.Counter(final).most_common(10)

print(most_common)
