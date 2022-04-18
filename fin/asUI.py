# Project as a UI

import collections
import re
import PySimpleGUI as sg

sg.theme('Dark Grey 9')

layout = [[sg.Text('Add book')],
          [sg.Input(key='-bookIn-'), sg.FileBrowse()],
          [sg.Text('Add stop list')],
          [sg.Input(key='-stopIn-'), sg.FileBrowse()],
          [sg.Button('Run'), sg.Button('Quit')]
          ]

window = sg.Window('Add files', layout)

while True:
    event, values = window.read()
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break
    book_path['-bookOut-'].update(values['-bookIn-'])
    stop_path['-stopOut-'].update(values['-stopIn-'])

windowclose()
