import collections
import re
import sys

re_exp_list = [
    re.compile(r'\w+'),
]

words = []
most_common = []

def wordsort():
    with open('stop-words.txt','r') as book:
        while True:
            chunk = book.read(5096)
            if not chunk:
                break

            for re_exp in re_exp_list:
                if not(re_exp, tuple):
                    pass
                if isinstance(re_exp, tuple):
                    words.append(chunk)
        print(words)

#
#
#






if __name__ == '__main__':
    wordsort()
