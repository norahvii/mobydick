text = open('stop-words.txt').read().lower()
biglist = []

for line in text.split('\n'):
    if not line.startswith("#"):
        biglist.append(line)

print(biglist)
