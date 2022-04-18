# Project as a hard coded script
import collections
import re

print('Add book:')
book_path = input()
print('Add stop list:')
stop_path = input()

def mdfilter():
    # Parse book
    book = re.findall(r'\w+', open(book_path, 'r',
                                encoding='utf8', errors='ignore')
                               .read().lower())
    # Parse stop words
    stop_words = []
    valid = re.compile(r'^\b[a-z]+\b')
    with open(stop_path, 'r',
           encoding='utf8',errors='ignore') as text_file:
           for line in text_file.read().lower().splitlines():
               if valid.match(line) != None:
                   stop_words.append(line)
    # Filter the book
    filtered_book = []
    for elem in book:
        if elem not in stop_words:
            filtered_book.append(elem)
    # Extract most common words
    most_common = collections.Counter(filtered_book).most_common(100)
    # Print result
    print(most_common)

mdfilter()
