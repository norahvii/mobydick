# Project as a hard coded script that asks for input
import collections
import re

print('Add book:')
book_path = input()
print('Add stop list:')
stop_path = input()

# Create a list for all the iterables in the book
book = re.findall(r'\w+', open(book_path, 'r',
                               encoding='utf8', errors='ignore')
                              .read().lower())

# Create a list for all stop words
stop_words = []
valid = re.compile(r'^\b[a-z]+\b')

with open(stop_path, 'r',
           encoding='utf8',errors='ignore') as text_file:
    for line in text_file.read().lower().splitlines():
        if valid.match(line) != None:
            stop_words.append(line)

# Create a list for the book filtered by the stop word list
filtered_book = []

for elem in book:
    if elem not in stop_words:
        filtered_book.append(elem)

# List the most common words in the filtered book
most_common = collections.Counter(filtered_book).most_common(100)

# Print it
print(most_common)
