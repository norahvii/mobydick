text = open('stop-words.txt').read().lower()
biglist = []

for line in text.split('\n'):
    if line and not line.startswith("#") and not line.startswith(' '):
        biglist.append(line)

print(biglist)
