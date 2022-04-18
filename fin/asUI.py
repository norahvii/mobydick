# Project as a UI
import collections
import re
import PySimpleGUI as sg

sg.theme('Dark Grey 9')

layout = [[sg.Text('Add book')],
          [sg.Input(key='-bookIn-'), sg.FileBrowse()],
          [sg.Text('Add stop list')],
          [sg.Input(key='-stopIn-'), sg.FileBrowse()],
          [sg.Button('Run'), sg.Button('Quit')],
          [sg.Output(size=(50, 10))],
          ]

window = sg.Window('Add files', layout)

while True:
    event, values = window.read()
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break
    if event == 'Run':
        # Update path values based on input
        book_path['-bookOut-'].update(values['-bookIn-'])
        stop_path['-stopOut-'].update(values['-stopIn-'])
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
    else:
        break

windowclose()

# Need to fix NameError: 'book_path' is not defined
