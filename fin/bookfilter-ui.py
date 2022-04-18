# Project as a UI
import collections
import re

import PySimpleGUI as sg

sg.theme('Dark Grey 9')

layout = [[sg.Text('Add book')],
          [sg.InputText('', key='input_book'), sg.FileBrowse()],
          [sg.Text('Add stop list')],
          [sg.InputText('', key='input_stop'), sg.FileBrowse()],
          [sg.Button('Run'), sg.Button('Quit')],
          [sg.Output(size=(50, 10))],
          ]

window = sg.Window('Add files', layout)

def bookfilter():
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

while True:
    event, values = window.read()
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break
    if event == 'Run':
        book_path = str(values['input_book'])
        stop_path = str(values['input_stop'])
        bookfilter()
    else:
        break

windowclose()
