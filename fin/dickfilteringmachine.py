import collections
import re

# Create a list for all the stop words and not new lines / commented lines
stop_words_file = open('stop-words.txt').read().lower()
stop_words_list = []

for line in stop_words_file.split('\n'):
    if line and not line.startswith("#") and not line.startswith(' '):
        stop_words_list.append(line)

# Create a list for all the iterables in the book
book = re.findall(r'\w+',open('mobydick.txt').read().lower())

# Create a list for the book filtered by the stop word list
filtered_book = []

for elem in book:
    if elem not in stop_words_list:
        filtered_book.append(elem)

# List the most common words in the filtered book
most_common = collections.Counter(filtered_book).most_common(100)
# Print it
print(most_common)
