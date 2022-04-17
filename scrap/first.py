import collections
import re

words = re.findall(r'\w+',open('shortdick.txt').read().lower())

most_common = collections.Counter(words).most_common(10)

print(most_common)
