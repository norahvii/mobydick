stop_words_file = []

with open('stop-words.txt', 'r') as text_file:
    for line in text_file.read().lower().splitlines():
        stop_words_file.append(line)

print(stop_words_file)
print(len(stop_words_file))
